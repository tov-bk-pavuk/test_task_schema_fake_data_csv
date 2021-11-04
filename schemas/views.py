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
                                            fields=('name', 'field_type', 'order'), max_num=1)
    if request.method == 'POST':
        formset = scheme_form_set(request.POST)
        form = SchemaModelForm(request.POST)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return '/'
    formset = scheme_form_set()
    form = SchemaModelForm()
    context = {'formset': formset, 'form': form}
    return render(request, 'schemas/new_schema.html', context)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def update_schema(request, pk):
    scheme_form_set = inlineformset_factory(Schema, Column,
            fields=('name', 'field_type', 'order'))
    schema = Schema.objects.get(id=pk)
    formset = scheme_form_set(instance=schema)
    if request.method == 'POST':
        formset = scheme_form_set(request.POST, schema)
        if formset.is_valid():
            formset.save()
            return '/'
    context = {'formset': formset}
    return render(request, 'schemas/new_schema.html', context)


class SchemaDeleteView(DeleteView):
    model = Schema
    pk_url_kwarg = 'pk'
    template_name = 'schemas/del_obj.html'
    success_url = '/'


@login_required(login_url='/users/u_login')
def new_schema(request):
    return render(request, 'schemas/new_schema.html')
