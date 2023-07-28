# Generated by Django 4.2 on 2023-07-18 13:08

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_mensage_logerror_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logerror',
            options={'managed': True},
        ),
        migrations.AlterModelManagers(
            name='logerror',
            managers=[
                ('normal_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='logerror',
            name='dat_delete',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='logerror',
            name='dat_edicao',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='logerror',
            name='dat_insercao',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='logerror',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
