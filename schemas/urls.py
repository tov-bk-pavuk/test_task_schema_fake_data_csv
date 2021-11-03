from django.contrib import admin
from django.urls import include, path

from schemas import views

urlpatterns = [
    path('', views.new_schema, name='new_schema'),
    path('create_cls_bsd', views.SchemaCreateView.as_view(), name='new_schema'),
    path('update_cls_bsd/<int:id>', views.SchemaUpdateView.as_view(), name='upd_schema'),
    path('delete_cls_bsd/<int:id>', views.SchemaDeleteView.as_view(), name='dlt_schema'),
]
