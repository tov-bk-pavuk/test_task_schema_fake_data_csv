from data_gen.forms import AmountForm

from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DeleteView, ListView

from schemas.tasks import data_gen_new

from .forms import SchemaModelForm
from .models import Column, Schema


class SchemasListView(ListView):
    model = Schema
    template_name = 'schemas/home_data_schemas.html'
    fields = ['name', 'separator', 'string_character', 'column']


@login_required(login_url='/users/u_login')
def detail_schema(request, pk):
    if request.method == 'POST':
        form = AmountForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['data_gen_amount']
            data_gen_new.apply_async((pk, amount))
            schema = Schema.objects.get(id=pk)
            context = {'schema': schema, 'form': form}
            # messages.success(request, ('Данные генерируются'))
            return HttpResponseRedirect(reverse('detail_schema', kwargs={'pk': pk}))
            # return render(request, 'schemas/schema_data_sets.html', context)
    form = AmountForm()
    schema = Schema.objects.get(id=pk)
    context = {'schema': schema, 'form': form}
    return render(request, 'schemas/schema_data_sets.html', context)


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
