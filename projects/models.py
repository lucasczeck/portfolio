from django.db import models

import core.models


class Projects(core.models.Log):
    created_date = models.DateTimeField(null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    is_finished = models.BooleanField(null=True)
    is_professional = models.BooleanField(null=True)
    is_approved = models.BooleanField(default=False)
    is_published = models.BooleanField(null=True)
    repository_url = models.URLField(null=True)
    project_url = models.URLField(null=True)
