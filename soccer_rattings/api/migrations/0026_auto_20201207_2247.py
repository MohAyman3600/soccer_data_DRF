# Generated by Django 3.1.3 on 2020-12-07 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20201207_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerstats',
            old_name='statistics_crads_yellowred',
            new_name='statistics_cards_yellowred',
        ),
    ]