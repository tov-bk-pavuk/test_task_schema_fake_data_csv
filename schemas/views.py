from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.forms import formset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  UpdateView,
                                  DeleteView)
from django.views.generic.list import MultipleObjectMixin

from .models import Schema, Column
from .forms import ColumnModelForm, SchemaModelForm


class SchemasListView(ListView):
    model = Schema
    template_name = 'schemas/home_data_schemas.html'
    fields = ['name', 'separator', 'string_character', 'column']


# class SchemaCreateView(MultipleObjectMixin, CreateView):
#     SchemeFormSet = inlineformset_factory(Schema, Column,
#         fields=('name', 'field_type', 'order'))
#     formset = SchemeFormSet()
#     extra_context = {'formset': formset}
#     model = Schema
#     template_name = 'schemas/new_schema.html'  # 'schemas/new_schema_cls_bsd.html'
#     fields = ['name', 'separator', 'string_character']
#     success_url = '/'
#     object_list = Column.objects.all()


def create_schema(request):
    scheme_form_set = inlineformset_factory(Schema, Column,
                                            fields=('name', 'field_type', 'order'), extra=1)
    formset = scheme_form_set()
    form = SchemaModelForm()
    if request.method == 'POST':
        form = SchemaModelForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            instance = Schema.objects.get(name=name)
            formset = scheme_form_set(request.POST, request.FILES, instance=instance)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect(reverse('home'))
    context = {'formset': formset, 'form': form}
    return render(request, 'schemas/new_schema.html', context)


def update_schema(request, pk):
    scheme_form_set = inlineformset_factory(Schema, Column,
                                            fields=('name', 'field_type', 'order'), extra=1)
    if request.method == 'POST':
        instance = Schema.objects.get(id=pk)
        form = SchemaModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            # instance = Schema.objects.get(id=pk)
            formset = scheme_form_set(request.POST, request.FILES, instance=instance)
            if formset.is_valid():
                formset.save()
                if 'save' in request.POST:
                    return HttpResponseRedirect(reverse('home'))
    instance = Schema.objects.get(id=pk)
    formset = scheme_form_set(instance=instance)
    form = SchemaModelForm(instance=instance)
    col = 1
    context = {'formset': formset, 'form': form, 'col': col, 'instance': instance}
    return render(request, 'schemas/new_schema.html', context)


class SchemaDeleteView(DeleteView):
    model = Schema
    pk_url_kwarg = 'pk'
    template_name = 'schemas/del_obj.html'
    success_url = '/'


@login_required(login_url='/users/u_login')
def new_schema(request):
    return render(request, 'schemas/new_schema.html')
