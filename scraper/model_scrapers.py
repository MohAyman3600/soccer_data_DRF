"""League scraper subclass."""
from .scraper import Scraper, StatsSraper
from api.models import League, Player, PlayerStats, Team, TeamStats
from api.serializers import (
    LeagueSerializer, PlayerSerailizer, PlayerStatsSerializer,
    TeamSerializer,
    TeamStatsSerializer
)


class LeagueScraper(Scraper):
    """
    Scarper for League data.
    Get league data in json format
    Query paramters can be set as a dictionary
    of the fofllowing pparamters are :-
        team:NUMBER, type:STRING(league|cup), name:STRING,
        current:STRING(true|false), last:NUMBER, id:NUMBER, search:STRING,
        season:NUMBER(YYYY), code:STRING, and country:STRING.
    """

    class Meta:
        model = League
        serializer_class = LeagueSerializer
        endpoint = 'leagues'
        querystring = {"id": "39"}


class TeamScraper(Scraper):
    """
    Scarper for Team data.
    Get Team data in json format.
    Query paramters can be set as a dictionary
    of the fofllowing pparamters are :-
        league:NUMBER, name:STRING, id:NUMBER, search:STRING,
        season:STRING(YYYY), and country:STRING.
    """

    class Meta:
        model = Team
        serializer_class = TeamSerializer
        endpoint = 'teams'
        querystring = {"league": "39", "season": "2020"}


class PlayerScraper(Scraper):
    """
    Scarper for Player data.
    Get Player data in json format.
    Query paramters can be set as a dictionary
    of the fofllowing pparamters are :-
        league:NUMBER, team:NUMBER page:STRING, id:NUMBER,
        search:STRING, season:STRING(YYYY), and country:STRING.
    """

    class Meta:
        model = Player
        serializer_class = PlayerSerailizer
        endpoint = 'players'
        querystring = {"league": "39", "season": "2020"}


class TeamStatsScraper(StatsSraper):
    """
    Scarper for Team statistics data.
    Get team season statistics.
        team_id:NUMBER, season:YYYY and league_id:NUMBER
        are required paramters.
        date:YYYY-MM-DD is optional.
    """
    class Meta:
        model = TeamStats
        serializer_class = TeamStatsSerializer
        endpoint = 'teams/statistics'
        querystring = {"team": "33", "league": "39", "season": "2020"}


class PlayerStatsScraper(StatsSraper):
    """
    Scarper for Player statistics data.
    Get Player season statistics.
    Query paramters can be set as a dictionary
    of the fofllowing pparamters are: -
        league: NUMBER, team: NUMBER page: STRING, id: NUMBER,
        search: STRING, season: STRING(YYYY), and country: STRING.
    """
    class Meta:
        model = PlayerStats
        serializer_class = PlayerStatsSerializer
        endpoint = 'players'
        querystring = {"team": "33", "league": "39", "season": "2020"}
