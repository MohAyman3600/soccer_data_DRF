# Generated by Django 3.1.3 on 2020-12-14 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('league_id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(max_length=50, verbose_name='name')),
                ('league_type', models.CharField(max_length=50, verbose_name='type')),
                ('league_logo', models.URLField(verbose_name='logo')),
                ('country_name', models.CharField(max_length=50, verbose_name='country')),
                ('country_code', models.CharField(max_length=5, verbose_name='country_code')),
                ('country_flag', models.URLField(verbose_name='country_flag')),
            ],
            options={
                'verbose_name': 'league',
                'verbose_name_plural': 'leagues',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=50, verbose_name='name')),
                ('player_firstname', models.CharField(max_length=50, verbose_name='first name')),
                ('player_lastname', models.CharField(max_length=50, verbose_name='last name')),
                ('player_age', models.PositiveIntegerField(verbose_name='age')),
                ('player_birth_country', models.CharField(max_length=50, verbose_name='birth country')),
                ('player_birth_date', models.DateField(verbose_name='birth date')),
                ('player_birth_place', models.CharField(max_length=50, verbose_name='birth place')),
                ('player_height', models.CharField(max_length=50, verbose_name='height')),
                ('player_nationality', models.CharField(max_length=50, verbose_name='nationality')),
                ('player_weight', models.CharField(max_length=50, null=True, verbose_name='weight')),
                ('player_photo', models.URLField(verbose_name='photo')),
                ('player_injured', models.BooleanField(verbose_name='injured')),
            ],
            options={
                'verbose_name': 'player',
                'verbose_name_plural': 'players',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(verbose_name='year')),
                ('start', models.DateField(verbose_name='start')),
                ('end', models.DateField(verbose_name='end')),
                ('current', models.BooleanField(verbose_name='current')),
                ('coverage_fixtures_events', models.BooleanField(verbose_name='Events Coverage')),
                ('coverage_fixtures_lineups', models.BooleanField(verbose_name='fixtures lineups')),
                ('coverage_fixtures_statistics_fixtures', models.BooleanField(verbose_name='fixtures stats')),
                ('coverage_fixtures_statistics_players', models.BooleanField(verbose_name='fixture player stats')),
                ('coverage_standings', models.BooleanField(verbose_name='standings coverage')),
                ('coverage_players', models.BooleanField(verbose_name='players coverage')),
                ('coverage_top_scorers', models.BooleanField(blank=True, null=True, verbose_name='top scorers coverage')),
                ('coverage_predictions', models.BooleanField(verbose_name='predictions coverage')),
                ('coverage_odds', models.BooleanField(verbose_name='odds coverage')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='api.league', verbose_name='league')),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
            },
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'created'), ('updated', 'updated')], max_length=7)),
                ('object_type', models.CharField(max_length=50, verbose_name='object type')),
                ('object_id', models.CharField(max_length=50, verbose_name='object ID')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50, verbose_name='name')),
                ('team_country', models.CharField(max_length=50, null=True, verbose_name='country')),
                ('team_founded', models.PositiveIntegerField(null=True, verbose_name='founded')),
                ('team_national', models.BooleanField(null=True, verbose_name='national')),
                ('team_logo', models.URLField(verbose_name='logo')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='TeamStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biggest_goals_against_home', models.PositiveIntegerField(verbose_name='biggest home goals conceded')),
                ('biggest_goals_against_away', models.PositiveIntegerField(verbose_name='biggest away goals conceded')),
                ('biggest_goals_for_home', models.PositiveIntegerField(verbose_name='biggest home goals scored')),
                ('biggest_goals_for_away', models.PositiveIntegerField(verbose_name='biggest away goals scored')),
                ('biggest_loses_away', models.CharField(blank=True, max_length=10, null=True, verbose_name='biggest loses away')),
                ('biggest_loses_home', models.CharField(blank=True, max_length=10, null=True, verbose_name='biggest loses home')),
                ('biggest_wins_away', models.CharField(blank=True, max_length=10, null=True, verbose_name='biggest wins away')),
                ('biggest_wins_home', models.CharField(blank=True, max_length=10, null=True, verbose_name='biggest wins home')),
                ('biggest_streak_draws', models.PositiveIntegerField(blank=True, null=True, verbose_name='biggest streak draws')),
                ('biggest_streak_wins', models.PositiveIntegerField(blank=True, null=True, verbose_name='biggest streak wins')),
                ('biggest_streak_loses', models.PositiveIntegerField(blank=True, null=True, verbose_name='biggest streak loses')),
                ('clean_sheet_home', models.PositiveIntegerField(verbose_name='clean sheets home')),
                ('clean_sheet_away', models.PositiveIntegerField(verbose_name='clean sheets away')),
                ('failed_to_score_home', models.PositiveIntegerField(verbose_name='failed to score home')),
                ('failed_to_score_away', models.PositiveIntegerField(verbose_name='failed to score away')),
                ('fixtures_draws_away', models.PositiveIntegerField(verbose_name='draws away')),
                ('fixtures_draws_home', models.PositiveIntegerField(verbose_name='draws home')),
                ('fixtures_loses_away', models.PositiveIntegerField(verbose_name='loses away')),
                ('fixtures_loses_home', models.PositiveIntegerField(verbose_name='loses home')),
                ('fixtures_wins_away', models.PositiveIntegerField(verbose_name='wins away')),
                ('fixtures_wins_home', models.PositiveIntegerField(verbose_name='wins home')),
                ('goals_against_average_away', models.CharField(max_length=10, verbose_name='goals against average home')),
                ('goals_against_average_home', models.CharField(max_length=10, verbose_name='goals against average home')),
                ('goals_against_total_away', models.PositiveIntegerField(verbose_name='goals against total home')),
                ('goals_against_total_home', models.PositiveIntegerField(verbose_name='goals against total home')),
                ('goals_for_average_away', models.CharField(max_length=10, verbose_name='goals scored average away')),
                ('goals_for_average_home', models.CharField(max_length=10, verbose_name='goals scored average home')),
                ('goals_for_total_away', models.PositiveIntegerField(verbose_name='goals scored average away')),
                ('goals_for_total_home', models.PositiveIntegerField(verbose_name='goals scored total home')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.season', verbose_name='season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.team', verbose_name='team')),
            ],
            options={
                'unique_together': {('team', 'season')},
            },
        ),
        migrations.AddField(
            model_name='team',
            name='seasons',
            field=models.ManyToManyField(through='api.TeamStats', to='api.Season', verbose_name='seasons'),
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistics_cards_red', models.PositiveIntegerField(blank=True, null=True, verbose_name='red cards')),
                ('statistics_cards_yellow', models.PositiveIntegerField(blank=True, null=True, verbose_name='yellow cards')),
                ('statistics_cards_yellowred', models.PositiveIntegerField(blank=True, null=True, verbose_name='yellowred cards')),
                ('statistics_dribbles_attempts', models.PositiveIntegerField(blank=True, null=True, verbose_name='dribble attempts')),
                ('statistics_dribbles_past', models.PositiveIntegerField(blank=True, null=True, verbose_name='dribbles past')),
                ('statistics_dribbles_success', models.PositiveIntegerField(blank=True, null=True, verbose_name='successful dribbles')),
                ('statistics_duels_total', models.PositiveIntegerField(blank=True, null=True, verbose_name='total duels')),
                ('statistics_duels_won', models.PositiveIntegerField(blank=True, null=True, verbose_name='duels won')),
                ('statistics_fouls_committed', models.PositiveIntegerField(blank=True, null=True, verbose_name='fouls committed')),
                ('statistics_fouls_drawn', models.PositiveIntegerField(blank=True, null=True, verbose_name='fouls drawn')),
                ('statistics_games_appearences', models.PositiveIntegerField(blank=True, null=True, verbose_name='appearances')),
                ('statistics_games_captain', models.BooleanField(blank=True, null=True, verbose_name='captain games')),
                ('statistics_games_lineups', models.PositiveIntegerField(blank=True, null=True, verbose_name='lineups')),
                ('statistics_games_minutes', models.PositiveIntegerField(blank=True, null=True, verbose_name='played minutes')),
                ('statistics_games_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='shirt number')),
                ('statistics_games_position', models.CharField(blank=True, max_length=50, null=True, verbose_name='position')),
                ('statistics_games_rating', models.FloatField(blank=True, null=True, verbose_name='rating')),
                ('statistics_goals_assists', models.PositiveIntegerField(blank=True, null=True, verbose_name='assists')),
                ('statistics_goals_total', models.PositiveIntegerField(blank=True, null=True, verbose_name='goals scored')),
                ('statistics_goals_conceded', models.PositiveIntegerField(blank=True, null=True, verbose_name='goals conceded')),
                ('statistics_goals_saves', models.PositiveIntegerField(blank=True, null=True, verbose_name='goals saves')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.player', verbose_name='player')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.season', verbose_name='season ')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='api.team', verbose_name='team')),
            ],
            options={
                'unique_together': {('player', 'season', 'team')},
            },
        ),
        migrations.AddField(
            model_name='player',
            name='seasons',
            field=models.ManyToManyField(through='api.PlayerStats', to='api.Season', verbose_name='seasons'),
        ),
        migrations.CreateModel(
            name='AsyncActionReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('ok', 'ok'), ('failed', 'failed')], default='pending', max_length=7)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('error_traceback', models.TextField(blank=True, null=True)),
                ('result_objects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='api.taskresult', verbose_name='objects')),
            ],
        ),
    ]
