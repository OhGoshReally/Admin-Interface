from django.contrib import admin
from . import models


@admin.register(models.SabConfig)
class SabConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SonarrConfig)
class SonarrConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CouchPotatoConfig)
class CouchPotatoConfigAdmin(admin.ModelAdmin):
    pass