from django.contrib import admin
from django.urls import include, path

from schemas import views

urlpatterns = [
    # path('', views.new_schema, name='new_schema'),
    path('create', views.create_schema, name='new_schema'),
    path('formsets', views.formsets, name='formsets'),
    path('update/<int:pk>', views.update_schema, name='upd_schema'),
    path('delete_cls_bsd/<int:pk>', views.SchemaDeleteView.as_view(), name='dlt_schema'),
]
