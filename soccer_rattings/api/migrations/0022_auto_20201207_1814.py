# Generated by Django 3.1.3 on 2020-12-07 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20201207_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamstats',
            old_name='fixture_loses_away',
            new_name='fixtures_loses_away',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='fixture_loses_home',
            new_name='fixtures_loses_home',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='fixture_wins_away',
            new_name='fixtures_wins_away',
        ),
        migrations.RenameField(
            model_name='teamstats',
            old_name='fixture_wins_home',
            new_name='fixtures_wins_home',
        ),
    ]
