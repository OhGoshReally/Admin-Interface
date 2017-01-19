from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    username = models.CharField('username', max_length=10, unique=True, db_index=True)
    email = models.EmailField('email address', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


class BaseConnect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    apikey = models.CharField()
    visible = models.BooleanField()


class SabConfig(BaseConnect):
    pass


class SonarrConfig(BaseConnect):
    pass


class CouchPotatoConfig(BaseConnect):
    pass
