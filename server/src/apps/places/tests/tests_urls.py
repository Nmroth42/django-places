from django.test import SimpleTestCase
from django.urls import resolve, reverse

from places.views import *


class TestUrls(SimpleTestCase):
    def test_place_list_url_is_resolved(self):
        url = reverse('place-list')
        self.assertEquals(resolve(url).func.view_class, PlaceListView)

    def test_place_delete_url_is_resolved(self):
        url = reverse('place-delete', kwargs={'pk': '0'})
        self.assertEquals(resolve(url).func.view_class, PlaceDeleteView)

    def test_place_create_url_is_resolved(self):
        url = reverse('place-create')
        self.assertEquals(resolve(url).func.view_class, PlaceCreateView)
