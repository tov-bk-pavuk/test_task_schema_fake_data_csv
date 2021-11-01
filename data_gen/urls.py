from data_gen import views

from django.urls import path


urlpatterns = [
    path('', views.data_sets, name='data_sets'),
    path('data_gen', views.data_gen, name='data_gen'),
]
