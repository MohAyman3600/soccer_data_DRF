# Generated by Django 3.1.3 on 2020-11-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201129_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='players',
        ),
        migrations.RemoveField(
            model_name='season',
            name='teams',
        ),
        migrations.AddField(
            model_name='player',
            name='seasons',
            field=models.ManyToManyField(through='api.PlayerStats', to='api.Season', verbose_name='seasons'),
        ),
        migrations.AddField(
            model_name='team',
            name='seasons',
            field=models.ManyToManyField(through='api.TeamStats', to='api.Season', verbose_name='seasons'),
        ),
    ]
