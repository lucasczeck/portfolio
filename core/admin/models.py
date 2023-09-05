from django.db import models
from django.db.models import DO_NOTHING

import core.models


class Module(core.models.Log):
    name = models.CharField(max_length=200, unique=True)


class Cards(core.models.Log):
    module = models.OneToOneField(Module, on_delete=DO_NOTHING)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    access = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
