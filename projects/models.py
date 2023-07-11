from django.db import models

from core.integracoes.github.models import Repositories

import core.models


class Projects(core.models.Log):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    is_finished = models.BooleanField(null=True)
    is_professional = models.BooleanField(null=True)
    is_approved = models.BooleanField(default=False)
    is_published = models.BooleanField(null=True)
    project_url = models.URLField(null=True)
    repository = models.ForeignKey(Repositories, on_delete=models.DO_NOTHING, null=True)
