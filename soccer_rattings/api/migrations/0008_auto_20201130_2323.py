# Generated by Django 3.1.3 on 2020-11-30 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201129_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamstats',
            name='goals_against_average_away',
            field=models.CharField(max_length=10, verbose_name='goals against average home'),
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='goals_against_average_home',
            field=models.CharField(max_length=10, verbose_name='goals against average home'),
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='goals_for_average_away',
            field=models.CharField(max_length=10, verbose_name='goals scored average away'),
        ),
        migrations.AlterField(
            model_name='teamstats',
            name='goals_for_average_home',
            field=models.CharField(max_length=10, verbose_name='goals scored average home'),
        ),
        migrations.AlterUniqueTogether(
            name='teamstats',
            unique_together={('team', 'season')},
        ),
    ]
