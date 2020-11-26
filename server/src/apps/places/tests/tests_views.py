from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from places.models import Place


class TestLoginUser(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='TestUserName',
            password='TestPassword',
        )
        self.user.set_password('TestPassword')
        self.user.save()
        self.user = authenticate(
            username='TestUserName', password='TestPassword')
        login = self.client.login(
            username='TestUserName', password='TestPassword')

        self.places_url = reverse('place-list')
        self.place_create_url = reverse('place-create')
        self.place_delete_url = reverse('place-delete', kwargs={'pk': '0'})

    def test_places_GET(self):
        response = self.client.get(self.places_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'places/place_list.html')

    def test_create_place_GET(self):
        response = self.client.get(self.place_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'places/place_create.html')

    def test_create_place_POST(self):
        response = self.client.post(self.place_create_url, {
            'name': 'TestPlace',
            'latitude': '2.22',
            'longitude': '2.22',
            'comment': 'TestComment'
        })

        self.assertEquals(response.status_code, 200)


class TestUnauthorizedUser(TestCase):
    def setUp(self):
        self.client = Client()

        self.places_url = reverse('place-list')
        self.place_create_url = reverse('place-create')
        self.place_delete_url = reverse('place-delete', kwargs={'pk': '0'})

    def test_places_GET(self):
        response = self.client.get(self.places_url)
        self.assertEqual(response.status_code, 302)

    def test_create_place_GET(self):
        response = self.client.get(self.place_create_url)
        self.assertEqual(response.status_code, 302)

    def test_create_place_POST(self):
        response = self.client.get(self.place_delete_url)
        self.assertEqual(response.status_code, 302)
