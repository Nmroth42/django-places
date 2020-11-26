from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('accounts/', include('apps.users.urls')),
    path('place/', include('apps.places.urls')),
    path('admin/', admin.site.urls),
    path(
        '',
        TemplateView.as_view(
            template_name='places/landing.html'),
        name='place-landing'
    ),
]
