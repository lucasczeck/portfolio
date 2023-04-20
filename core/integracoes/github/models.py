from django.db import models
import core.models


class Repositories(core.models.Log):
    name = models.CharField(max_length=200, null=True)
    is_private = models.BooleanField(null=True)
    commits_url = models.URLField(null=True)
    created_date = models.DateTimeField(null=True)
    pushed_date = models.DateTimeField(null=True)


class Commits(core.models.Log):
    sha = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(null=True)
    message = models.TextField(null=True)
    url = models.URLField(null=True)
    parents_sha = models.CharField(max_length=200, null=True)
