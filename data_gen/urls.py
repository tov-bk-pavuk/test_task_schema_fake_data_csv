from django.contrib import admin
from django.urls import include, path

from data_gen import views


urlpatterns = [
    path('', views.data_sets, name='data_sets'),
    path('', views.data_gen, name='data_gen'),
]
