from django.db import models
import core.models


class Infos(core.models.Log):
    who_am_i = models.TextField(null=True)
    career = models.TextField(null=True)


class Highlights(core.models.Log):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)


class ContactInfo(core.models.Log):
    instagram_user = models.CharField(max_length=200, null=True)
    instagram_url = models.CharField(max_length=200, null=True)
    github_user = models.CharField(max_length=200, null=True)
    github_url = models.CharField(max_length=200, null=True)
    linkedin_user = models.CharField(max_length=200, null=True)
    linkedin_url = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
