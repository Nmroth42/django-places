from django.views import View
from django.views.generic import TemplateView
from django.urls import path, include
from django.views.generic import TemplateView

# from users import views as users
from places import views as places

urlpatterns = [
    path(
        'list/',
        places.PlaceListView.as_view(),
        name='place-list'
    ),
    path('create/', places.PlaceCreateView.as_view(), name='place-create'),
    path('<int:pk>/delete/', places.PlaceDeleteView.as_view(), name='place-delete'),

]
