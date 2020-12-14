# Generated by Django 3.1.3 on 2020-11-29 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201129_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='seasons',
        ),
        migrations.RemoveField(
            model_name='team',
            name='seasons',
        ),
        migrations.AddField(
            model_name='season',
            name='players',
            field=models.ManyToManyField(through='api.PlayerStats', to='api.Player', verbose_name='players'),
        ),
        migrations.AddField(
            model_name='season',
            name='teams',
            field=models.ManyToManyField(through='api.TeamStats', to='api.Team', verbose_name='teams'),
        ),
    ]