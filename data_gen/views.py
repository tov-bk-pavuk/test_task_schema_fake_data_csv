import csv

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from faker import Faker

from schemas import models

from . models import DataSetFile


@login_required(login_url='/users/u_login')
def data_sets(request):
    return render(request, 'data_gen/data_sets.html')


def data_upload(request):
    return


class DataSetListView(ListView):
    model = DataSetFile
    template_name = 'data_gen/data_sets.html'


@login_required(login_url='/users/u_login')
def data_gen(request):
    # Create the HttpResponse object with the appropriate CSV header.
    id_pk = 2  # Временные переменные нужно поулчать из ссылки
    amount = 1000  # Временные переменные

    name = models.Schema.objects.get(pk=id_pk).name
    # response = HttpResponse(
    #     content_type='text/csv',
    #     headers={'Content-Disposition': f'attachment; filename="{name}.csv"'},
    # )

    sep = models.Schema.objects.get(pk=id_pk).separator
    str_char = models.Schema.objects.get(pk=id_pk).string_character
    columns = models.Schema.objects.get(pk=id_pk).column.all().order_by('order', 'name')

    fake = Faker()

    def col_type(a: str):  # Функция определяет тип поля для Faker-a
        if a == 'FN':
            return fake.name()
        elif a == 'JB':
            return fake.job()
        elif a == 'EM':
            return fake.ascii_email()
        elif a == 'DN':
            return fake.domain_name()
        elif a == 'PN':
            return fake.phone_number()
        elif a == 'CN':
            return fake.company()

    # writer = csv.writer(response, delimiter=sep, quotechar=str_char)
    # writer.writerow([f'{columns[i]}' for i in range(len(columns))])
    # for _ in range(amount):
    #     writer.writerow([f'{col_type(columns[i].field_type)}' for i in range(len(columns))])
    DataSetFile.objects.get_or_create(url=f'static/media/{name}.csv')

    with open(f'static/media/{name}.csv', 'w') as f:
        writer = csv.writer(f, delimiter=sep, quotechar=str_char)
        writer.writerow([f'{columns[i]}' for i in range(len(columns))])
        for _ in range(amount):
            writer.writerow([f'{col_type(columns[i].field_type)}' for i in range(len(columns))])
        # myfile = File(f)
        # myfile.write(str(response))

    # messages.success(request, ('Данные генерируются'))
    return render(request, 'data_gen/data_sets.html')
