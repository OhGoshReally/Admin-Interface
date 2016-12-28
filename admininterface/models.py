from django.db import models
from django.contrib.auth import User


class SabConfig(models.Model):
    user = models.ForeignKey(User)
    url = models.URLField()
    apikey = models.CharField()
    visible = models.BooleanField()
