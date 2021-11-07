from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DeleteView, ListView

from .forms import SchemaModelForm
from .models import Column, Schema


class SchemasListView(ListView):
    model = Schema
    template_name = 'schemas/home_data_schemas.html'
    fields = ['name', 'separator', 'string_character', 'column']


def create_schema(request):
    scheme_form_set = inlineformset_factory(Schema, Column,
                                            fields=('name', 'field_type', 'order'), extra=1)
    if request.method == 'POST':
        form = SchemaModelForm(request.POST)  # первичное создание объекта при нажатии на  ADD
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            instance = Schema.objects.get(name=name)
            pk = instance.pk
            formset = scheme_form_set(request.POST, request.FILES, instance=instance)
            if formset.is_valid():
                formset.save()
                if request.POST.get('save_schema'):
                    return HttpResponseRedirect(reverse('home'))
                if request.POST.get('add_column'):
                    return HttpResponseRedirect(reverse('upd_schema', args=[pk]))
    form = SchemaModelForm()  # первый случай загрузки формы при нажатии на ссылку
    formset = scheme_form_set()
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
            formset = scheme_form_set(request.POST, request.FILES, instance=instance)
            if formset.is_valid():
                formset.save()
                if 'save_schema' in request.POST:
                    return HttpResponseRedirect(reverse('home'))
    instance = Schema.objects.get(id=pk)
    formset = scheme_form_set(instance=instance)
    form = SchemaModelForm(instance=instance)
    context = {'formset': formset, 'form': form}
    return render(request, 'schemas/new_schema.html', context)


class SchemaDeleteView(DeleteView):
    model = Schema
    pk_url_kwarg = 'pk'
    template_name = 'schemas/del_obj.html'
    success_url = '/'


@login_required(login_url='/users/u_login')
def new_schema(request):
    return render(request, 'schemas/new_schema.html')
