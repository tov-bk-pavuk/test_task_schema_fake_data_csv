from data_gen import views

from django.contrib.auth.decorators import login_required
from django.urls import path


urlpatterns = [
    # path('', views.data_sets, name='data_sets'),
    path('', login_required(views.DataSetListView.as_view(), login_url='/users/u_login'), name='data_sets'),
    path('data_gen', views.data_gen, name='data_gen'),
    path('data_upload', views.data_upload, name='data_upload'),
]
