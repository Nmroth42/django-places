from django.views import View
from django.views.generic import TemplateView
from django.urls import path, include
from django.views.generic import TemplateView

# from users import views as users
from places import views as places

urlpatterns = [
    path(
        'place-list',
        places.PlaceListView.as_view(),
        name='list'
    ),
    path('place-create/', places.PlaceCreateView.as_view(), name='place-create'),
    path('', TemplateView.as_view(template_name="places/landing.html"), name='place-landing'),
    path('place/<int:pk>/delete/', places.PlaceDeleteView.as_view(), name='place-delete'),

]
