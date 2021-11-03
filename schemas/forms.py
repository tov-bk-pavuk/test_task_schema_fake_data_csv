from django import forms

from . import models


class SchemaModelForm(forms.ModelForm):
    class Meta:
        model = models.Schema
        #fields = []


class ColumnModelForm(forms.ModelForm):
    class Meta:
        model = models.Column
        #fields = []