import csv

from celery import shared_task

from data_gen.models import DataSetFile

from faker import Faker

from schemas import models


fake = Faker()


@shared_task
def data_gen_new(pk, amount):
    name = models.Schema.objects.get(pk=pk).name + str(amount)
    sep = models.Schema.objects.get(pk=pk).separator
    str_char = models.Schema.objects.get(pk=pk).string_character
    columns = models.Schema.objects.get(pk=pk).column_set.all().order_by('order', 'name')
    instance = models.Schema.objects.get(pk=pk)
    DataSetFile.objects.get_or_create(url=f'static/media/{name}.csv', schema=instance)  # , schema=instance

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

    with open(f'static/media/{name}.csv', 'w') as f:
        writer = csv.writer(f, delimiter=sep, quotechar=str_char)
        writer.writerow([f'{columns[i]}' for i in range(len(columns))])
        for _ in range(amount):
            writer.writerow([f'{col_type(columns[i].field_type)}' for i in range(len(columns))])
