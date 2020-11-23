from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.users.urls')),
    path('', include('apps.places.urls')),
    path('admin/', admin.site.urls),
]
