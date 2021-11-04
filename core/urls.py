import debug_toolbar

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path

# from schemas.views import home

from schemas.views import SchemasListView


urlpatterns = [
    path('', login_required(SchemasListView.as_view(), login_url='/users/u_login'), name='home'),
    path('__debug__/', include(debug_toolbar.urls)),
    # path('', home, name='home'),
    path('schemas/', include('schemas.urls')),
    path('data_gen/', include('data_gen.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('u_auth.urls')),
]
