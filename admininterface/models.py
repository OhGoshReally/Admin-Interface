from django.db import models
from django.contrib.auth import User


class SabConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    apikey = models.CharField()
    visible = models.BooleanField()
