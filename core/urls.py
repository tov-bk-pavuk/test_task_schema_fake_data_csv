from django.contrib import admin
from django.urls import include, path

from schemas import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('u_auth.urls')),
]
