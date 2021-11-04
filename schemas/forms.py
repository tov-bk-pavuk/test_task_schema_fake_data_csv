from django import forms

from . import models


class SchemaModelForm(forms.ModelForm):
    class Meta:
        model = models.Schema
        fields = ['name', 'separator', 'string_character']


class ColumnModelForm(forms.ModelForm):
    class Meta:
        model = models.Column
        fields = ['name', 'field_type', 'order', 'schema']
