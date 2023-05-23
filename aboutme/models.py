from django.db import models

import core.models


class PersonalInfos(core.models.Log):
    who_am_i = models.TextField(null=True)


class Hobbies(core.models.Log):
    descriptive_name = models.CharField(max_length=200, null=True)


class ProfessionalInfos(core.models.Log):
    career_summary = models.TextField(null=True)


class Stacks(core.models.Log):
    descriptive_name = models.CharField(max_length=200, null=True)


class Highlights(core.models.Log):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
