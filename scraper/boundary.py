"""Module for boundary classes interacting with Django classes."""
from api.models import PlayerStats, TeamStats
import logging

logger = logging.getLogger(__name__)


class ModelInfoExtractor(object):
    """Boundary class to extract model info from django."""

    def get_fields(self, serializer_class):
        """Get serializer class defined fields."""
        fields = serializer_class.Meta.fields.copy()
        return fields

    def get_foreign_keys_info(self, serializer_class):
        """Get foreign keys info -> fields, model, and bool many,"""
        keys = serializer_class._declared_fields.copy()
        ret = {}
        for key in keys:
            value = keys[key]
            ret[key] = {'fields': [], 'many': getattr(value, 'many', False)}
            if ret[key]['many']:
                fields = value.child.Meta.fields
                ret[key]['model'] = value.child.Meta.model
            else:
                fields = value.Meta.fields
                ret[key]['model'] = value.Meta.model
            for field in fields:
                ret[key]['fields'].append(field)
        return ret

    def get_non_relational_fields(self, serializer_class):
        """Get core model fields, excluding relation fields."""
        fields = self.get_fields(serializer_class)
        rel_fields = self.get_foreign_keys_info(serializer_class).keys()
        return [field for field in fields if field not in rel_fields]


class ModelBuilder(object):
    """Boundary class to build model data from scraped data."""

    def create_or_update(self, serializer_class, data, instance=None):
        """Create object using serializer class."""
        if instance is None:
            serializer = serializer_class(data=data)
        else:
            serializer = serializer_class(instance, data=data)
        if serializer.is_valid():
            instance = serializer.save()
            return instance
        else:
            logger.error(
                f"Serializer '{serializer_class}' error-> {serializer.errors}")
            return False

    def perform_operation(self, serializer_class, non_rel_fields, data):
        """Perform update or create operation for one object."""
        non_rel_data = {x: data[x] for x in non_rel_fields}
        model_class = serializer_class.Meta.model
        primary_key_field = model_class._meta.pk.name
        if primary_key_field in non_rel_fields:
            primary_key_Value = non_rel_data[primary_key_field]
            obj = model_class.objects.filter(pk=primary_key_Value).first()
        elif model_class is TeamStats:
            obj = model_class.objects.filter(
                team=data['team']['team_id'], season=data['season']['id']).first()
        elif model_class is PlayerStats:
            obj = model_class.objects.filter(
                player=data['player']['player_id'],
                team=data['team']['team_id'],
                season=data['season']['id']).first()
        else:
            obj = None
        if obj:
            logger.info(
                f"Object: {non_rel_data} already exists")
            logger.info("Updataing Object")
            instance = self.create_or_update(
                serializer_class=serializer_class,
                data=data,
                instance=obj
            )
            operation = 'update'
        else:
            instance = self.create_or_update(
                serializer_class=serializer_class,
                data=data
            )
            operation = 'creation'
        if instance:
            logger.info(
                f"Object {non_rel_data} {operation} succeded.")
            return (instance, operation)
        else:
            logger.error(
                f"Object {non_rel_data} {operation} failed.")
            return (False, operation)
