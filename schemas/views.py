from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from . models import Schema


class SchemasListView(ListView):
    model = Schema
    template_name = 'schemas/home_data_schemas.html'


@login_required(login_url='/users/u_login')
def new_schema(request):
    return render(request, 'schemas/new_schema.html')
