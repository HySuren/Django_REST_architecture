from django.contrib import admin
from . import models

admin.site.register(models.Newsletter)
admin.site.register(models.Client)
admin.site.register(models.Message)
