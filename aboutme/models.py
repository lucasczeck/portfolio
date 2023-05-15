from django.db import models

import core.models


class PersonalInfos(core.models.Log):
    who_am_i = models.TextField(null=True)
    hobbies = models.TextField(null=True)
    studies = models.TextField(null=True)
