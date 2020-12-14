# Generated by Django 3.1.3 on 2020-12-12 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20201209_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='age',
            new_name='player_age',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='birth_country',
            new_name='player_birth_country',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='birth_date',
            new_name='player_birth_date',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='birth_place',
            new_name='player_birth_place',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='firstname',
            new_name='player_firstname',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='height',
            new_name='player_height',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='id',
            new_name='player_id',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='injured',
            new_name='player_injured',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='lastname',
            new_name='player_lastname',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='player_name',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='nationality',
            new_name='player_nationality',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='photo',
            new_name='player_photo',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='weight',
            new_name='player_weight',
        ),
    ]
