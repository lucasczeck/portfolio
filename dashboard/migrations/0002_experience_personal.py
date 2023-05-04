# Generated by Django 4.2 on 2023-05-04 14:55

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('started', models.DateField(null=True)),
                ('end', models.DateField(null=True)),
                ('position', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
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
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat_insercao', models.DateTimeField(auto_now_add=True, null=True)),
                ('dat_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('dat_delete', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('photo', models.FileField(null=True, upload_to='summary')),
                ('title', models.CharField(max_length=100, null=True)),
                ('last_experience', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.experience')),
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
