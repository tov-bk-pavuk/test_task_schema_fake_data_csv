from data_gen import views

from django.urls import include, path


urlpatterns = [
    path('', views.data_sets, name='data_sets'),
    path('', views.data_gen, name='data_gen'),
]
