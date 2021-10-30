from django.contrib import admin
from django.urls import include, path

from schemas.views import home


urlpatterns = [
    path('', home, name='home'),
    path('schemas/', include('schemas.urls')),
    path('data_gen', include('data_gen.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('u_auth.urls')),
]
