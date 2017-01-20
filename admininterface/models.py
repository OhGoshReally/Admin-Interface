from django.db import models
from django.contrib.auth.models import User


class BaseConnect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    apikey = models.CharField(max_length=100)
    visible = models.BooleanField()

    def __str__(self):
        return self.user.__str__() + " - " + self.url

    class Meta:
        abstract = True


class SabConfig(BaseConnect):
    pass


class SonarrConfig(BaseConnect):
    pass


class CouchPotatoConfig(BaseConnect):
    pass
