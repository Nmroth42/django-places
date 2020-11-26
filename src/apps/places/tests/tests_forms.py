from django.test import TestCase

from places.forms import PlaceForm


class TestForms(TestCase):
    def test_place_form_valid_data(self):
        form = PlaceForm(data={
            'name': 'testName',
            'latitude': 20.013333,
            'longitude': 92.852333,
            'comment': 'testComment'
        })
        self.assertFalse(form.is_valid())

    def test_place_form_incorrect_latitude_invalid_data(self):
        form = PlaceForm(data={
            'name': 'testName',
            'latitude': -200.013333,
            'longitude': 92.852333,
            'comment': 'testComment'
        })
        self.assertFalse(form.is_valid())
