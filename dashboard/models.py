from django.db import models
from django.db.models import DO_NOTHING

import core.models


class HardSkills(core.models.Log):
    name = models.CharField(max_length=100, primary_key=True)
    descriptive_name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    parent_skill = models.ForeignKey('self', on_delete=DO_NOTHING, null=True)


class SoftSkill(core.models.Log):
    name = models.CharField(max_length=100, primary_key=True)
    descriptive_name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    parent_skill = models.ForeignKey('self', on_delete=DO_NOTHING, null=True)


class Experience(core.models.Log):
    company = models.CharField(max_length=100, null=True)
    started = models.DateField(null=True)
    end = models.DateField(null=True)
    position = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)


class Personal(core.models.Log):
    photo = models.FileField(upload_to='summary', null=True)
    title = models.CharField(max_length=100, null=True)
    last_experience = models.ForeignKey('Experience', on_delete=DO_NOTHING, null=True)
