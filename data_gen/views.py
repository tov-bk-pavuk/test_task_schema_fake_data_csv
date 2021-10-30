from django.contrib.auth.decorators import login_required
from django.shortcuts import render


#@login_required(login_url='/users/u_login')
def data_sets(request):
    return render(request, 'data_gen/data_sets.html')


#@login_required(login_url='/users/u_login')
def data_gen(request):
    pass
