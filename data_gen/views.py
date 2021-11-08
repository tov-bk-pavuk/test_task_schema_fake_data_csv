from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from . models import DataSetFile


@login_required(login_url='/users/u_login')
def data_sets(request):
    return render(request, 'data_gen/data_sets.html')


class DataSetListView(ListView):
    model = DataSetFile
    template_name = 'data_gen/data_sets.html'
