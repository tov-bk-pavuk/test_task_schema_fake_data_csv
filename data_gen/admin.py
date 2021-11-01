from django.contrib import admin

from . import models


@admin.register(models.DataSetFile)
class DataSetFileAdmin(admin.ModelAdmin):
    list_filter = ('created', 'status')
    list_display = ['created', 'status', 'url']
