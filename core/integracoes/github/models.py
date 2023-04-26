from django.db import models
from django.db.models import DO_NOTHING

import core.models


class Repositories(core.models.Log):
    name = models.CharField(max_length=200, null=True)
    is_private = models.BooleanField(null=True)
    commits_url = models.URLField(null=True)
    created_date = models.DateTimeField(null=True)
    pushed_date = models.DateTimeField(null=True)
    is_finished = models.BooleanField(null=True)
    is_professional = models.BooleanField(null=True)
    title = models.CharField(max_length=200, null=True)
    is_approved = models.BooleanField(default=False)
    is_published = models.BooleanField(null=True)


class Commits(core.models.Log):
    sha = models.CharField(max_length=200, primary_key=True)
    date = models.DateTimeField(null=True)
    message = models.TextField(null=True)
    url = models.URLField(null=True)
    repository = models.ForeignKey('Repositories', on_delete=DO_NOTHING, null=True)
