# Generated by Django 3.1.3 on 2020-12-01 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201201_0224'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='playerstats',
            unique_together={('player', 'season')},
        ),
    ]