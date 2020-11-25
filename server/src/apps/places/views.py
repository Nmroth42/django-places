from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)
from places.models import Memory
from .forms import MemoryForm
from django.conf import settings
from django.views.generic import View
from django.db import transaction
from django.shortcuts import redirect
from places.mixins import UserAuthorMixinListView, AuthRequiredMixin

class PlacesListView(UserAuthorMixinListView, ListView):
    model = Memory


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
