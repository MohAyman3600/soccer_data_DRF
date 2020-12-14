# Generated by Django 3.1.3 on 2020-12-08 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20201207_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'created'), ('updated', 'updated')], max_length=7)),
                ('object_type', models.CharField(max_length=50, verbose_name='object type')),
                ('object_id', models.CharField(max_length=50, verbose_name='object ID')),
            ],
        ),
        migrations.CreateModel(
            name='AsyncActionReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('ok', 'ok'), ('failed', 'failed')], default='pending', max_length=7)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('error_traceback', models.TextField(blank=True, null=True)),
                ('result_objects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='api.taskresult', verbose_name='objects')),
            ],
        ),
    ]
