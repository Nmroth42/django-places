from django.views import View
from django.views.generic import TemplateView
from django.urls import path, include

# from users import views as users
from places import views as places

urlpatterns = [
    path(
        'home',
        places.PlacesListView.as_view(
            template_name='places/home.html'
        ),
        name='home'
    ),
]
