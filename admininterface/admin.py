from django.contrib import admin
from . import models


@admin.register(models.SabConfig)
class SabConfigAdmin(admin.ModelAdmin):
    pass
