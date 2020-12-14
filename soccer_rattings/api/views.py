"""Views for interacting with model serializers."""
from api.serializers import (
    LeagueSerializer,
    PlayerSerailizer,
    PlayerStatsSerializer,
    TeamSerializer,
    TeamStatsSerializer
)
from api.models import League, Team, Player, TeamStats, PlayerStats

from rest_framework.viewsets import ModelViewSet


class LeagueViewSet(ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamStatsViewSet(ModelViewSet):
    queryset = TeamStats.objects.all()
    serializer_class = TeamStatsSerializer


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerailizer


class PlayerStatsViewSet(ModelViewSet):
    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer
