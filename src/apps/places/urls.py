from django.urls import path

from places import views as places


urlpatterns = [
    path(
        'list/',
        places.PlaceListView.as_view(),
        name='place-list'
    ),
    path(
        'create/',
        places.PlaceCreateView.as_view(),
        name='place-create'
    ),
    path(
        '<int:pk>/delete/',
        places.PlaceDeleteView.as_view(),
        name='place-delete'
    ),
]
