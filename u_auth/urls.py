from django.urls import path

from . import views

urlpatterns = [
    path('u_login', views.user_login, name='u_login'),
    path('logout', views.user_logout, name='u_logout')
]
