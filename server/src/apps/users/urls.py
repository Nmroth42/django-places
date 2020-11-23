from django.views import View
from django.views.generic import TemplateView
from django.urls import path, include

from users import views as users

urlpatterns = [
    path("login/", users.login, name="login"),
    path('accounts/',include('allauth.urls')),
    # path('oauth/', include('social_django.urls', namespace='social')),     
]
