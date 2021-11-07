from data_gen import views

from django.contrib.auth.decorators import login_required
from django.urls import path


urlpatterns = [
    path('', login_required(views.DataSetListView.as_view(),
                            login_url='/users/u_login'), name='data_sets'),
]
