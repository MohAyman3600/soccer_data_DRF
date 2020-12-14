"""API database models."""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class League(models.Model):
    """Database Model for league."""
    league_id = models.PositiveIntegerField(_("ID"), primary_key=True)
    league_name = models.CharField(_("name"), max_length=50)
    league_type = models.CharField(_("type"), max_length=50)
    league_logo = models.URLField(_("logo"), max_length=200)
    country_name = models.CharField(_("country"), max_length=50)
    country_code = models.CharField(_("country_code"), max_length=5)
    country_flag = models.URLField(_("country_flag"), max_length=200)

    class Meta:
        verbose_name = _("league")
        verbose_name_plural = _("leagues")

    def __str__(self):
        return str(self.league_name)+"-"+str(self.country_name)


class Season(models.Model):
    """Database Model for league season."""
    year = models.PositiveIntegerField(_("year"))
    start = models.DateField(_("start"), auto_now=False, auto_now_add=False)
    end = models.DateField(_("end"), auto_now=False, auto_now_add=False)
    current = models.BooleanField(_("current"))
    coverage_fixtures_events = models.BooleanField(_("Events Coverage"))
    coverage_fixtures_lineups = models.BooleanField(_("fixtures lineups"))
    coverage_fixtures_statistics_fixtures = models.BooleanField(
        _("fixtures stats"))
    coverage_fixtures_statistics_players = models.BooleanField(
        _("fixture player stats"))
    coverage_standings = models.BooleanField(_("standings coverage"))
    coverage_players = models.BooleanField(_("players coverage"))
    coverage_top_scorers = models.BooleanField(
        _("top scorers coverage"), null=True, blank=True,)
    coverage_predictions = models.BooleanField(_("predictions coverage"))
    coverage_odds = models.BooleanField(_("odds coverage"))
    league = models.ForeignKey(
        League,
        verbose_name=_("league"),
        on_delete=models.CASCADE,
        related_name="seasons"
    )

    class Meta:
        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'

    def __str__(self):
        return str(self.year)+"-"+str(self.league.league_name)+"-" +\
            str(self.league.country_name)


class Team(models.Model):
    """Database model for team."""
    team_id = models.PositiveIntegerField(_("ID"), primary_key=True)
    team_name = models.CharField(_("name"), max_length=50)
    team_country = models.CharField(_("country"), max_length=50, null=True)
    team_founded = models.PositiveIntegerField(_("founded"), null=True)
    team_national = models.BooleanField(_("national"), null=True)
    team_logo = models.URLField(_("logo"), max_length=200)
    seasons = models.ManyToManyField(
        Season, verbose_name=_("seasons"), through="TeamStats")

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return str(self.team_name)+"-"+str(self.team_country)


class Player(models.Model):
    """database model for player."""
    player_id = models.PositiveIntegerField(_("ID"), primary_key=True)
    player_name = models.CharField(_("name"), max_length=50)
    player_firstname = models.CharField(_("first name"), max_length=50)
    player_lastname = models.CharField(_("last name"), max_length=50)
    player_age = models.PositiveIntegerField(_("age"))
    player_birth_country = models.CharField(_("birth country"), max_length=50)
    player_birth_date = models.DateField(
        _("birth date"),
        auto_now=False,
        auto_now_add=False
    )
    player_birth_place = models.CharField(_("birth place"), max_length=50)
    player_height = models.CharField(_("height"), max_length=50)
    player_nationality = models.CharField(_("nationality"), max_length=50)
    player_weight = models.CharField(
        _("weight"), max_length=50, null=True)
    player_photo = models.URLField(_("photo"), max_length=200)
    player_injured = models.BooleanField(_("injured"))
    seasons = models.ManyToManyField(
        Season, verbose_name=_("seasons"), through="PlayerStats")

    class Meta:
        verbose_name = 'player'
        verbose_name_plural = 'players'

    def __str__(self):
        return str(self.player_firstname)+" "+str(self.player_lastname)


class TeamStats(models.Model):
    """
    Database model for Team Statistics for one season.
    Also, acts as the ManyToMany relationship table
    between Team and Season.
    """
    biggest_goals_against_home = models.PositiveIntegerField(
        _("biggest home goals conceded"))
    biggest_goals_against_away = models.PositiveIntegerField(
        _("biggest away goals conceded"))
    biggest_goals_for_home = models.PositiveIntegerField(
        _("biggest home goals scored"))
    biggest_goals_for_away = models.PositiveIntegerField(
        _("biggest away goals scored"))
    biggest_loses_away = models.CharField(
        _("biggest loses away"), max_length=10, null=True, blank=True,)
    biggest_loses_home = models.CharField(
        _("biggest loses home"), max_length=10, null=True, blank=True,)
    biggest_wins_away = models.CharField(
        _("biggest wins away"), max_length=10, null=True, blank=True,)
    biggest_wins_home = models.CharField(
        _("biggest wins home"), max_length=10, null=True, blank=True,)
    biggest_streak_draws = models.PositiveIntegerField(
        _("biggest streak draws"), null=True, blank=True,)
    biggest_streak_wins = models.PositiveIntegerField(
        _("biggest streak wins"), null=True, blank=True,)
    biggest_streak_loses = models.PositiveIntegerField(
        _("biggest streak loses"), null=True, blank=True,)
    clean_sheet_home = models.PositiveIntegerField(_("clean sheets home"))
    clean_sheet_away = models.PositiveIntegerField(_("clean sheets away"))
    failed_to_score_home = models.PositiveIntegerField(
        _("failed to score home"))
    failed_to_score_away = models.PositiveIntegerField(
        _("failed to score away"))
    fixtures_draws_away = models.PositiveIntegerField(_("draws away"))
    fixtures_draws_home = models.PositiveIntegerField(_("draws home"))
    fixtures_loses_away = models.PositiveIntegerField(_("loses away"))
    fixtures_loses_home = models.PositiveIntegerField(_("loses home"))
    fixtures_wins_away = models.PositiveIntegerField(_("wins away"))
    fixtures_wins_home = models.PositiveIntegerField(_("wins home"))
    goals_against_average_away = models.CharField(
        _("goals against average home"), max_length=10)
    goals_against_average_home = models.CharField(
        _("goals against average home"), max_length=10)
    goals_against_total_away = models.PositiveIntegerField(
        _("goals against total home"))
    goals_against_total_home = models.PositiveIntegerField(
        _("goals against total home"))
    goals_for_average_away = models.CharField(
        _("goals scored average away"), max_length=10)
    goals_for_average_home = models.CharField(
        _("goals scored average home"), max_length=10)
    goals_for_total_away = models.PositiveIntegerField(
        _("goals scored average away"))
    goals_for_total_home = models.PositiveIntegerField(
        _("goals scored total home"))
    team = models.ForeignKey(
        Team, verbose_name=_("team"), on_delete=models.CASCADE
    )
    season = models.ForeignKey(
        Season, verbose_name=_("season"), on_delete=models.CASCADE
    )

    class Meta:
        """
        Define Meta info.
        PrimaryKey->team and season fields.
        """
        unique_together = (("team", "season"),)

    def __str__(self):
        return str(self.team.team_name)+"-"+str(self.season.year)


class PlayerStats(models.Model):
    statistics_cards_red = models.PositiveIntegerField(
        _("red cards"), null=True, blank=True,)
    statistics_cards_yellow = models.PositiveIntegerField(
        _("yellow cards"), null=True, blank=True,)
    statistics_cards_yellowred = models.PositiveIntegerField(
        _("yellowred cards"), null=True, blank=True,)
    statistics_dribbles_attempts = models.PositiveIntegerField(
        _("dribble attempts"), null=True, blank=True,)
    statistics_dribbles_past = models.PositiveIntegerField(
        _("dribbles past"), null=True, blank=True,)
    statistics_dribbles_success = models.PositiveIntegerField(
        _("successful dribbles"), null=True, blank=True,)
    statistics_duels_total = models.PositiveIntegerField(
        _("total duels"), null=True, blank=True,)
    statistics_duels_won = models.PositiveIntegerField(
        _("duels won"), null=True, blank=True,)
    statistics_fouls_committed = models.PositiveIntegerField(
        _("fouls committed"), null=True, blank=True,)
    statistics_fouls_drawn = models.PositiveIntegerField(
        _("fouls drawn"), null=True, blank=True,)
    statistics_games_appearences = models.PositiveIntegerField(
        _("appearances"), null=True, blank=True,)
    statistics_games_captain = models.BooleanField(
        _("captain games"), null=True, blank=True,)
    statistics_games_lineups = models.PositiveIntegerField(
        _("lineups"), null=True, blank=True,)
    statistics_games_minutes = models.PositiveIntegerField(
        _("played minutes"), null=True, blank=True,)
    statistics_games_number = models.PositiveIntegerField(
        _("shirt number"), null=True, blank=True,)
    statistics_games_position = models.CharField(
        _("position"), max_length=50, null=True, blank=True,)
    statistics_games_rating = models.FloatField(
        _("rating"), null=True, blank=True,)
    statistics_goals_assists = models.PositiveIntegerField(
        _("assists"), null=True, blank=True,)
    statistics_goals_total = models.PositiveIntegerField(
        _("goals scored"), null=True, blank=True,)
    statistics_goals_conceded = models.PositiveIntegerField(
        _("goals conceded"), null=True, blank=True,)
    statistics_goals_saves = models.PositiveIntegerField(
        _("goals saves"), null=True, blank=True,)
    player = models.ForeignKey(
        Player, verbose_name=_("player"), on_delete=models.CASCADE,
    )
    season = models.ForeignKey(
        Season, verbose_name=_("season "), on_delete=models.CASCADE,
    )
    team = models.ForeignKey(Team, verbose_name=_(
        "team"),
        on_delete=models.CASCADE,
        related_name="players",
        null=True, blank=True,
    )

    class Meta:
        unique_together = (('player', 'season', 'team'),)

    def __str__(self):
        return str(self.player.player_name)+"-"+str(self.team) +\
            "_"+str(self.season.year)


class TaskResult(models.Model):
    CREATED = 'created'
    UPDATED = 'updated'
    STATUS_CHOICES = (
        (CREATED, 'created'),
        (UPDATED, 'updated'),
    )
    status = models.CharField(
        max_length=7, choices=STATUS_CHOICES)
    object_type = models.CharField(_("object type"), max_length=50)
    object_id = models.CharField(_("object ID"), max_length=50)


class AsyncActionReport(models.Model):
    PENDING = 'pending'
    OK = 'ok'
    FAILED = 'failed'
    STATUS_CHOICES = (
        (PENDING, 'pending'),
        (OK, 'ok'),
        (FAILED, 'failed')
    )
    status = models.CharField(
        max_length=7, choices=STATUS_CHOICES, default=PENDING)
    error_message = models.TextField(null=True, blank=True)
    error_traceback = models.TextField(null=True, blank=True)
    result_objects = models.ForeignKey(TaskResult, verbose_name=_(
        "objects"), on_delete=models.CASCADE, related_name='report')

    def __str__(self):
        return self.action
