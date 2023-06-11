from django.db import models
import core.models


class Infos(core.models.Log):
    who_am_i = models.TextField(null=True)
    career = models.TextField(null=True)


class Highlights(core.models.Log):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
