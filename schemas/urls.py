from django.contrib import admin
from django.urls import include, path

from schemas import views

urlpatterns = [
    path('create', views.create_schema, name='new_schema'),
    path('update/<int:pk>', views.update_schema, name='upd_schema'),
    path('detail/<int:pk>', views.detail_schema, name='detail_schema'),
    path('delete_cls_bsd/<int:pk>', views.SchemaDeleteView.as_view(), name='dlt_schema'),
]
