from django.shortcuts import render


def home(request):  # Schemas list
    return render(request, 'schemas/home_data_schemas.html')


def new_schema(request):
    return render(request, 'schemas/new_schema.html')
