# Generated by Django 4.2 on 2023-07-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0013_alter_repositories_is_project_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='repositories',
            name='repository_url',
            field=models.URLField(null=True),
        ),
    ]
