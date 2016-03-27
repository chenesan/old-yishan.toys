from django.contrib import admin
from . import models

admin.site.register(models.Article, admin.ModelAdmin)
admin.site.register(models.Tag, admin.ModelAdmin)
