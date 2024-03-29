# Generated by Django 4.2 on 2023-07-28 16:57

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0005_rename_career_summary_infos_career'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('instagram_user', models.CharField(max_length=200, null=True)),
                ('instagram_url', models.CharField(max_length=200, null=True)),
                ('github_user', models.CharField(max_length=200, null=True)),
                ('github_url', models.CharField(max_length=200, null=True)),
                ('linkedin_user', models.CharField(max_length=200, null=True)),
                ('linkedin_url', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
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
