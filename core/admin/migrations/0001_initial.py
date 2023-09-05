# Generated by Django 4.2 on 2023-09-05 00:27

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('name', models.CharField(max_length=200, unique=True)),
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
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('access', models.CharField(max_length=200, null=True)),
                ('url', models.CharField(max_length=200, null=True)),
                ('module', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='admin.module')),
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
