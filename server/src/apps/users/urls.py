from django.views import View
from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from users import views as users
from places import views as places

urlpatterns = [
    path('accounts/',include('allauth.urls')),
    path('accounts/logout/', LogoutView.as_view(next_page='home'),name='logout'),
]
