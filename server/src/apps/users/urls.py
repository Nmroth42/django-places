from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from django.views import View
from django.views.generic import TemplateView

urlpatterns = [
    path(
        'accounts/logout/',
        LogoutView.as_view(
            next_page='place-landing'),
        name='logout'
    ),
    path('accounts/', include('allauth.urls')),
]
