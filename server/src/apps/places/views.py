from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView, DeleteView)
from places.models import Memory
from .forms import MemoryForm
from django.conf import settings
from django.views.generic import View
from django.db import transaction
from django.shortcuts import redirect
from places.mixins import UserAuthorMixinListView, AuthRequiredMixin
from django.urls import reverse_lazy

class PlacesListView(UserAuthorMixinListView, ListView):
    model = Memory

    def get_queryset(self):
        queryset = super(PlacesListView, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class MemoryCreateView(AuthRequiredMixin, View):
    def get(self, request):
        memory_form = MemoryForm(initial={
        "lat":settings.DEFAULT_COORDINATES['latitude'],
        "lng":settings.DEFAULT_COORDINATES['longitude'],
        'GOOGLE_MAPS_API_KEY':settings.GOOGLE_MAPS_API_KEY
        })

        return render(request, 'places/memory_edit.html', {'memory_form': memory_form})

    @transaction.atomic
    def post(self, request):
        memory_form = MemoryForm(request.POST)
        if memory_form.is_valid():
            new_memory = memory_form.save(request)
            return redirect('/list', permanent=True)

        return render(request, 'places/memory_edit.html', {'memory_form': memory_form})

class PlaceDeleteView(DeleteView):
    model = Memory
    template_name = 'place_delete.html'
    success_url = reverse_lazy('list')
