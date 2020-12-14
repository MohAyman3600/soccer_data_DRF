"""Scrapper to get data from API."""
from api.models import League
import logging
from django.forms.models import model_to_dict
from requests.compat import urljoin, quote
from requests import request
from requests.exceptions import (
    HTTPError,
    ConnectionError,
    Timeout,
    RequestException,
)

from api.serializers import LeagueSerializer

from .boundary import ModelBuilder, ModelInfoExtractor

logger = logging.getLogger(__name__)


def nested_get(dic, keys):
    """Get value from nested dictionary, provided a list of keys."""
    for idx, key in enumerate(keys):
        try:
            dic = dic[key]
        except KeyError:
            try:
                dic = dic[key+"_"+keys[idx+1]]
            except KeyError:
                dic = dic[key+"_"+keys[idx+1]+"_"+keys[idx+2]]
                del keys[idx+2]
            del keys[idx+1]
    return dic


class BaseScraper(object):
    """
    Scrapper fetches appropriate data from API using ModelInfoExtractor,
    then saves the model object using ModelBuilder Class.
    """

    def __init__(self, API_url, API_headers):
        """Set API URL and request headers-> API keys."""
        self.API_url = API_url
        self.API_headers = API_headers

    def send_request(self, endpoint,  querystring, retries=2):
        """Send single request to API and return response or error."""
        url = urljoin(
            self.API_url,
            quote(endpoint)
        )
        try:
            response = request(
                'GET', url=url, headers=self.API_headers, params=querystring
            )
            response.raise_for_status()
        except HTTPError as e:
            logger.exception(f"scraper request: HTTP ERROR, {e}")
            raise Exception(e)
        except ConnectionError as e:
            logger.exception(f"scrapper request: CONNECTION ERROR, {e}")
            raise Exception(e)
        except Timeout as e:
            logger.exception(f"scrapper request: TIMEOUT ERROR, {e}")
            if retries > 0:
                self.send_request(endpoint, querystring, retries=0)
            else:
                raise Exception(e)
        except RequestException as e:
            logger.exception(f"scrapper request: REQUEST EXCEPTION, {e}")
            raise Exception(e)
        else:
            return response.json()

    def fetch_objects(self, endpoint=None, querystring=None):
        """
        Fetch objects form the API.
        On succes requests:
            Return dictionary with object ids as keys and value
            as tuple (True|False, 'updated'|'created') indicating operation
            type and if object is saved or not.
        On failed requests: return False.
        """
        assert hasattr(self, 'Meta'), (
            'Class {scraper_class} missing "Meta" attribute'.format(
                scraper_class=self.__class__.__name__
            )
        )
        if endpoint is None:
            assert hasattr(self.Meta, 'endpoint'), (
                'Class {scraper_class} missing "Meta.endpoint" attribute'
                .format(scraper_class=self.__class__.__name__)
            )
            endpoint = getattr(self.Meta, 'endpoint')
        if querystring is None:
            assert hasattr(self.Meta, 'querystring'), (
                'Class {scraper_class} missing "Meta.querystring" attribute'
                .format(scraper_class=self.__class__.__name__)
            )
            querystring = getattr(self.Meta, 'querystring')
        response = self.send_request(endpoint, querystring)
        if response.get('results') > 0:
            logger.info(f"{response.get('results')} objects fetched")
            response_objects = response.get('response')
            return response_objects
        else:
            if response.get('errors'):
                logger.error(
                    f"Request Failed: Erros->{response.get('errors')}")
                return False

class Scraper(BaseScraper, ModelInfoExtractor, ModelBuilder):
    def get_fields_values(self, data_dict, field_names):
        """Get fields values from data Dict using field names."""
        fields = {}
        for field in field_names:
            field_keys = field.split('_')
            try:
                fields[field] = nested_get(
                    data_dict, field_keys)
            except IndexError:
                logger.info(
                    f"field {field} not included in repsone, will try to fetch\
                         from database.")
                continue
        return fields

    def format_foreign_data(self, key, key_data):
        """format data for foregin key."""
        formated_data = {}
        if key['many']:
            formated_data = []
            for data in key_data.values():
                for idx, item in enumerate(data):
                    formated_data.append({})
                    formated_data[idx] = self.get_fields_values(
                        item, key['fields'])
        else:
            formated_data = self.get_fields_values(
                key_data, key['fields'])
        return formated_data

    def format_data(self, data, serializer_class):
        """
        Defualt behaviour for formating response data,
        """
        formated_data = {}
        fields = self.get_non_relational_fields(serializer_class)
        foreign_keys = self.get_foreign_keys_info(serializer_class)
        for key in foreign_keys:
            foreign_data = {key: data.pop(key)}
            foreign_key = foreign_keys[key]
            formated_data[key] = self.format_foreign_data(
                foreign_key, foreign_data)
        for field in fields:
            field_keys = field.split('_')
            formated_data[field] = nested_get(data, field_keys)
        return formated_data

    def save_objects(self, response_objects=None, serializer_class=None):
        """Fetch objects form the API and save them."""
        assert hasattr(self, 'Meta'), (
            'Class {scraper_class} missing "Meta" attribute'.format(
                scraper_class=self.__class__.__name__
            )
        )
        if serializer_class is None:
            assert hasattr(self.Meta, 'serializer_class'), (
                'Class {scraper_class} missing "Meta.serializer_class" attribute'
                .format(scraper_class=self.__class__.__name__)
            )
            serializer_class = getattr(self.Meta, 'serializer_class')
        if response_objects is None:
            response_objects = self.fetch_objects()
        if type(response_objects) is dict:
            response_objects = [response_objects]
        return_dict = {}
        for obj_data in response_objects:
            obj_formated = self.format_data(obj_data, serializer_class)
            non_rel_fields = self.get_non_relational_fields(serializer_class)
            instance = self.perform_operation(
                serializer_class, non_rel_fields, data=obj_formated)
            if instance[1]:
                logger.info(
                    f"Object {instance[0]} has been {instance[1]}.")
                return_dict[instance[0]] = instance[1]
        return return_dict


class StatsSraper(Scraper):
    def get_season(self, data):
        """Get season data for specific league."""
        try:
            league_info = data['league']
        except KeyError:
            league_info = data['statistics']['league']
        league = League.objects.filter(pk=league_info['id']).first()
        if league:
            season = model_to_dict(
                league.seasons.get(year=league_info['season']))
            if season:
                season['league_id'] = league.pk
                return season
        league_data = self.fetch_objects(
            endpoint='leagues',
            querystring={
                'id': str(league_info['id']),
                'season': str(league_info['season'])
            }
        )
        formated_obj = super().format_data(
            league_data[0], LeagueSerializer)
        league_non_rel_fields = self.get_non_relational_fields(
            LeagueSerializer)
        league = self.perform_operation(
            LeagueSerializer, league_non_rel_fields, formated_obj)
        if league[0]:
            league = league[0]
        season = model_to_dict(league.seasons.get(year=league_info['season']))
        season['league_id'] = league.pk
        return season

    def format_data(self, data, serializer_class):
        """
        formating response data,
        add specific data handling  for statistics data.
        """
        for key, value in data.items():
            if type(value) is list:
                data[key] = value[0]
        formated_data = {}
        foreign_data = {}
        fields = self.get_non_relational_fields(serializer_class)
        foreign_keys = self.get_foreign_keys_info(serializer_class)
        for key in foreign_keys:
            if key == 'season':
                formated_data[key] = self.get_season(data)
                continue
            try:
                foreign_data = {key: data.pop(key)}
            except KeyError:
                foreign_data = {key: data['statistics'].pop(key)}
            foreign_key = foreign_keys[key]
            formated_data[key] = self.format_foreign_data(
                foreign_key, foreign_data)
        for field in fields:
            field_keys = field.split('_')
            formated_data[field] = nested_get(data, field_keys)
        return formated_data
