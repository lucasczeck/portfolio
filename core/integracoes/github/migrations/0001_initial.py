# Generated by Django 4.2 on 2023-04-20 04:05

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('sha', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('message', models.TextField(null=True)),
                ('url', models.URLField(null=True)),
                ('parents_sha', models.CharField(max_length=200, null=True)),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('normal_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Repositories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('is_private', models.BooleanField(null=True)),
                ('commits_url', models.URLField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('pushed_date', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
            managers=[
                ('normal_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
