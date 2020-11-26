from django.test import TestCase
from django.contrib.auth.models import User

from places.models import Place


class PlaceTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('foo', 'testemail@gmail.com', 'bar')

    def test_place_str(self):
        name, comment = 'Test Place', 'Test Comment'
        place = Place.objects.create(
            owner=self.user,
            name=name,
            comment=comment,
            latitude=2.22,
            longitude=2.22)
        self.assertEqual(str(place), name)
