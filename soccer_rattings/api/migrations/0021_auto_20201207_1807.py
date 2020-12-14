# Generated by Django 3.1.3 on 2020-12-07 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20201204_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamstats',
            old_name='bgst_goals_against_away',
            new_name='biggest_goals_against_away',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='bgst_goals_against_home',
            new_name='biggest_goals_against_home',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='bgst_goals_for_away',
            new_name='biggest_goals_for_away',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='bgst_goals_for_home',
            new_name='biggest_goals_for_home',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='bgst_loses_away',
            new_name='biggest_loses_away',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='bgst_loses_home',
            new_name='biggest_loses_home',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='bgst_streak_draws',
            new_name='biggest_streak_draws',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='bgst_streak_loses',
            new_name='biggest_streak_loses',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='bgst_streak_wins',
            new_name='biggest_streak_wins',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='bgst_wins_away',
            new_name='biggest_wins_away',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='bgst_wins_home',
            new_name='biggest_wins_home',
        ),
    ]
