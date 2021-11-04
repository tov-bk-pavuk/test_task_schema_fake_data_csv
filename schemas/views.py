from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.forms import formset_factory
from django.http import HttpResponseRedirect
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

def formsets(request):
    column_forms = formset_factory(ColumnModelForm, extra=1)
    col_forms = column_forms(initial=[{
        'name': 'введите имя поля',
        'field_type': 'PN',
    }])
    if request.method == 'POST':
        col_forms(request.POST)
        if col_forms.is_valid():
            col_forms.save()
            return '/'
    # col_forms = column_forms()
    context = {'col_forms': col_forms}
    return render(request, 'schemas/formsets.html', context)


def create_schema(request):
    scheme_form_set = inlineformset_factory(Schema, Column,
                                            fields=('name', 'field_type', 'order'), extra=3)
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
    formset = scheme_form_set()
    form = SchemaModelForm()
    context = {'formset': formset, 'form': form}
    return render(request, 'schemas/new_schema.html', context)


def manage_articles(request):
    ArticleFormSet = formset_factory(ArticleForm)
    BookFormSet = formset_factory(BookForm)
    if request.method == 'POST':
        article_formset = ArticleFormSet(request.POST, request.FILES, prefix='articles')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if article_formset.is_valid() and book_formset.is_valid():
            # do something with the cleaned_data on the formsets.
            pass
    else:
        article_formset = ArticleFormSet(prefix='articles')
        book_formset = BookFormSet(prefix='books')
    return render(request, 'manage_articles.html', {
        'article_formset': article_formset,
        'book_formset': book_formset,
    })


def update_schema(request, pk):
    scheme_form_set = inlineformset_factory(Schema, Column,
                                            fields=('name', 'field_type', 'order', 'schema'), max_num=1)
    schema = Schema.objects.get(id=pk)
    formset = scheme_form_set(instance=schema)
    form = SchemaModelForm(instance=schema)
    if request.method == 'POST':
        formset = scheme_form_set(request.POST, schema)
        form = SchemaModelForm(request.POST, schema)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return '/'
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
