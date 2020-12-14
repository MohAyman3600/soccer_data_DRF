"""API URL configration."""
from api.views import (
    LeagueViewSet,
    TeamViewSet,
    PlayerViewSet,
    TeamStatsViewSet,
    PlayerStatsViewSet
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=False)
router.register(r'league/', LeagueViewSet)
router.register(r'team/', TeamViewSet)
router.register(r'player/', PlayerViewSet)
router.register(r'teamstats/', TeamStatsViewSet)
router.register(r'playerstats/', PlayerStatsViewSet)

urlpatterns = router.urls
