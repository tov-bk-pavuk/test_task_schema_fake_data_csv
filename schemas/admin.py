from django.contrib import admin

from . import models


@admin.register(models.Schema)
class SchemaAdmin(admin.ModelAdmin):
    list_filter = ('name', 'column')
    list_display = ['name', 'modified']
    # filter_horizontal = ['column']


@admin.register(models.Column)
class ColumnAdmin(admin.ModelAdmin):
    list_filter = ('order', 'name', 'field_type')
    list_display = ['name', 'order']
