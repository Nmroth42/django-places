from django.views import View
from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from users import views as users
from places import views as places

urlpatterns = [
    path('accounts/logout/', LogoutView.as_view(next_page='place-landing'),name='logout'),
    path('accounts/', include('allauth.urls')),
]
