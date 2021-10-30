from django.contrib.auth.decorators import login_required
from django.shortcuts import render


#@login_required(login_url='/users/u_login')
def home(request):  # Schemas list
    return render(request, 'schemas/home_data_schemas.html')


#@login_required(login_url='/users/u_login')
def new_schema(request):
    return render(request, 'schemas/new_schema.html')
