from django.shortcuts import render


def data_sets(request):
    return render(request, 'data_gen/data_sets.html')


def data_gen(request):
    pass
