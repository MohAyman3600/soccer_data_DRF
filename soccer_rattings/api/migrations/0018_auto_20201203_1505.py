# Generated by Django 3.1.3 on 2020-12-03 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20201203_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='season',
            old_name='coverage_fixtures_statistics',
            new_name='coverage_fixtures_statistics_fixtures',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='coverage_fixtures_player_stats',
            new_name='coverage_fixtures_statistics_players',
        ),
    ]