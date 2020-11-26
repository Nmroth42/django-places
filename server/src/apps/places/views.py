from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView, DeleteView)
from places.models import Place
from .forms import PlaceForm
from django.conf import settings
from django.views.generic import View
from django.db import transaction
from django.shortcuts import redirect
from places.mixins import UserAuthorMixinListView, AuthRequiredMixin
from django.urls import reverse_lazy, reverse

class PlaceListView(UserAuthorMixinListView, ListView):
    model = Place
    template_name='places/place_list.html'

    def get_queryset(self):
        queryset = super(PlaceListView, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class PlaceCreateView(AuthRequiredMixin, View):
    def get(self, request):
        place_form = PlaceForm(initial={
        "lat":settings.DEFAULT_COORDINATES['latitude'],
        "lng":settings.DEFAULT_COORDINATES['longitude'],
        'GOOGLE_MAPS_API_KEY':settings.GOOGLE_MAPS_API_KEY
        })

        return render(request, 'places/place_create.html', {'place_form': place_form})

    @transaction.atomic
    def post(self, request):
        place_form = PlaceForm(request.POST)
        if place_form.is_valid():
            new_place = place_form.save(request)
            return redirect(reverse('place-list'), permanent=True)

        return render(request, 'places/place_create.html', {'place_form': place_form})


class PlaceDeleteView(UserAuthorMixinListView, DeleteView):
    model = Place
    template_name='places/place_delete.html'
    success_url = reverse_lazy('place-list')
