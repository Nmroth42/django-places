from django import forms
from .models import Place


class PlaceForm(forms.Form):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())
    zoom = forms.FloatField(widget=forms.HiddenInput())
    name = forms.CharField(max_length=100)
    comment = forms.CharField(widget=forms.Textarea, max_length=1000)

    def clean_latitude(self):
        latitude = self.cleaned_data["latitude"]
        if -90 <= latitude <= 90:
            return latitude
        else:
            raise ValidationError(code="invalid")

    def clean_longitude(self):
        longitude = self.cleaned_data["longitude"]
        if -180 <= longitude <= 180:
            return longitude
        else:
            raise ValidationError(code="invalid")

    def clean_zoom(self):
        zoom = self.cleaned_data["zoom"]
        if 0 <= zoom <= 21:
            return int(zoom)
        else:
            raise ValidationError(code="invalid")

    def save(self, request):
        new_place = Place.objects.create(
            **self.cleaned_data,
            owner = request.user
            )
        return new_place
