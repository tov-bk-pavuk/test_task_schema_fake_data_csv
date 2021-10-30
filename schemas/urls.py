from django.contrib import admin
from django.urls import include, path

from schemas import views

urlpatterns = [
    path('', views.new_schema, name='new_schema'),
]
