from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  UpdateView,
                                  DeleteView)
from django.views.generic.list import MultipleObjectMixin

from .models import Schema, Column


class SchemasListView(ListView):
    model = Schema
    template_name = 'schemas/home_data_schemas.html'
    fields = ['name', 'separator', 'string_character', 'column']


class SchemaCreateView(MultipleObjectMixin, CreateView):
    SchemeFormSet = inlineformset_factory(Schema, Column,
                                          fields=('name',
                                                  'field_type',
                                                  'order'))
    formset = SchemeFormSet()
    extra_context = {'formset': formset}
    model = Schema
    template_name = 'schemas/new_schema_cls_bsd.html'
    fields = ['name', 'separator', 'string_character']
    success_url = '/'
    object_list = Column.objects.all()
    # extra_context = Column.objects.all()


class SchemaUpdateView(UpdateView):
    model = Schema
    pk_url_kwarg = 'id'
    template_name = 'schemas/new_schema_cls_bsd.html'
    fields = ['name', 'separator', 'string_character', 'column']
    success_url = '/'


class SchemaDeleteView(DeleteView):
    model = Schema
    pk_url_kwarg = 'id'
    template_name = 'schemas/del_obj.html'
    success_url = '/'


@login_required(login_url='/users/u_login')
def new_schema(request):
    return render(request, 'schemas/new_schema.html')
