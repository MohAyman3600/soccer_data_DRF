# Generated by Django 3.1.3 on 2020-12-07 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20201207_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerstats',
            old_name='statistics_dibbles_success',
            new_name='statistics_dribbles_success',
        ),
    ]
