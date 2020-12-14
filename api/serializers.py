"""Serilaizers for daatabase models."""
import logging
from django.forms.models import model_to_dict
from api.models import League, Player, PlayerStats, Season, Team, TeamStats
from rest_framework import serializers

logger = logging.getLogger(__name__)


def update_or_create(model, data, id_field):
    try:
        obj = model.objects.get(pk=data[id_field])
    except model.DoesNotExist:
        obj = model.objects.create(**data)
        return obj
    data.pop(id_field)
    model.objects.filter(pk=obj.pk).update(**data)
    return obj


class SeasonSerializer(serializers.ModelSerializer):
    """Serializer for Season model."""

    class Meta:
        model = Season
        fields = [
            'year',
            'start',
            'end',
            'current',
            'coverage_fixtures_events',
            'coverage_fixtures_lineups',
            'coverage_fixtures_statistics_fixtures',
            'coverage_fixtures_statistics_players',
            'coverage_standings',
            'coverage_players',
            'coverage_top_scorers',
            'coverage_predictions',
            'coverage_odds',
            'league_id',
        ]


class LeagueSerializer(serializers.ModelSerializer):
    """Serilaizer for League model."""
    seasons = SeasonSerializer(many=True)

    class Meta:
        model = League
        fields = [
            'league_id',
            'league_name',
            'league_type',
            'league_logo',
            'country_name',
            'country_code',
            'country_flag',
            'seasons',
        ]

    def create(self, validated_data):
        """Create league and it's seasons."""
        seasons_data = validated_data.pop('seasons')
        league = League.objects.get_or_create(**validated_data)[0]
        for season_data in seasons_data:
            Season.objects.create(league=league, **season_data)
        return league

    def update(self, instance, validated_data):
        seasons = validated_data.pop('seasons', [])
        instance = super().update(instance, validated_data)
        for season_data in seasons:
            season = Season.objects.get_or_create(
                league=instance, **season_data)
            if season[1]:
                logger.info(f"Added new season: {season_data}")
            else:
                season_dict = model_to_dict(season[0])
                season_dict.pop('id')
                season_dict.pop('league')
                if season_dict != dict(season_data):
                    season.objects.update(**season_data)
                    logger.info(f"Updated season: {season_data}")
        logger.info("Object updated")
        return instance


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model."""

    class Meta:
        model = Team
        fields = [
            'team_id',
            'team_name',
            'team_country',
            'team_founded',
            'team_national',
            'team_logo',
        ]
        extra_kwargs = {
            'team_id': {'validators': []}
        }


class PlayerSerailizer(serializers.ModelSerializer):
    """Serializer for Player model."""

    class Meta:
        model = Player
        fields = [
            'player_id',
            'player_name',
            'player_firstname',
            'player_lastname',
            'player_age',
            'player_birth_country',
            'player_birth_date',
            'player_birth_place',
            'player_height',
            'player_nationality',
            'player_weight',
            'player_photo',
            'player_injured',
        ]

        extra_kwargs = {
            'player_id': {'validators': []}
        }


class TeamStatsSerializer(serializers.ModelSerializer):
    """Serializer for Team Statistics model."""
    team = TeamSerializer()
    season = SeasonSerializer()

    class Meta:
        model = TeamStats
        fields = [
            'biggest_goals_against_home',
            'biggest_goals_against_away',
            'biggest_goals_for_home',
            'biggest_goals_for_away',
            'biggest_loses_away',
            'biggest_loses_home',
            'biggest_wins_away',
            'biggest_wins_home',
            'biggest_streak_draws',
            'biggest_streak_wins',
            'biggest_streak_loses',
            'clean_sheet_home',
            'clean_sheet_away',
            'failed_to_score_home',
            'failed_to_score_away',
            'fixtures_draws_away',
            'fixtures_draws_home',
            'fixtures_loses_away',
            'fixtures_loses_home',
            'fixtures_wins_away',
            'fixtures_wins_home',
            'goals_against_average_away',
            'goals_against_average_home',
            'goals_against_total_away',
            'goals_against_total_home',
            'goals_for_average_away',
            'goals_for_average_home',
            'goals_for_total_away',
            'goals_for_total_home',
            'team',
            'season',
        ]

    def create(self, validated_data):
        team_data = validated_data.pop('team')
        season_data = validated_data.pop('season')
        season = Season.objects.get_or_create(**season_data)[0]
        team = update_or_create(Team, team_data, 'team_id')
        team_stats = TeamStats.objects.create(
            team=team, season=season, **validated_data)
        return team_stats

    def update(self, instance, validated_data):
        team_data = validated_data.pop('team')
        season_data = validated_data.pop('season')
        season = Season.objects.get_or_create(**season_data)[0]
        team = update_or_create(Team, team_data, 'team_id')
        TeamStats.objects.filter(id=instance.id).update(
            team=team, season=season, **validated_data)
        return instance


class PlayerStatsSerializer(serializers.ModelSerializer):
    """Serializer for Team Statistics model."""
    player = PlayerSerailizer()
    season = SeasonSerializer()
    team = TeamSerializer()

    class Meta:
        model = PlayerStats
        fields = [
            'statistics_cards_red',
            'statistics_cards_yellow',
            'statistics_cards_yellowred',
            'statistics_dribbles_attempts',
            'statistics_dribbles_past',
            'statistics_dribbles_success',
            'statistics_duels_total',
            'statistics_duels_won',
            'statistics_fouls_committed',
            'statistics_fouls_drawn',
            'statistics_games_appearences',
            'statistics_games_captain',
            'statistics_games_lineups',
            'statistics_games_minutes',
            'statistics_games_number',
            'statistics_games_position',
            'statistics_games_rating',
            'statistics_goals_assists',
            'statistics_goals_total',
            'statistics_goals_conceded',
            'statistics_goals_saves',
            'player',
            'season',
            'team',
        ]

    def create(self, validated_data):
        player_data = validated_data.pop('player')
        season_data = validated_data.pop('season')
        team_data = validated_data.pop('team')
        player = update_or_create(Player, player_data, 'player_id')
        season = Season.objects.get_or_create(**season_data)[0]
        team = update_or_create(Team, team_data, 'team_id')
        instance = PlayerStats.objects.create(
            player=player, season=season, team=team, **validated_data)
        return instance

    def update(self, instance, validated_data):
        player_data = validated_data.pop('player')
        season_data = validated_data.pop('season')
        team_data = validated_data.pop('team')
        player = update_or_create(Player, player_data, 'player_id')
        season = Season.objects.get_or_create(**season_data)[0]
        team = update_or_create(Team, team_data, 'team_id')
        PlayerStats.objects.filter(id=instance.id).update(player=player,
                                                          season=season,
                                                          team=team,
                                                          **validated_data)
        return instance
