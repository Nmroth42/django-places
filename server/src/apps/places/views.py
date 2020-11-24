from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)
from places.models import Memory
from .forms import MemoryForm
from django.conf import settings
from django.views.generic import View
from django.shortcuts import redirect

class PlacesListView(ListView):
    """Return list of Mem."""

    model = Memory
    paginate_by = 2


class MemoryCreateView(View):
    def get(self, request):
        memory_form = MemoryForm(initial={
        "lat":"56.0183900",
        "lng":"92.8671700",
        'GOOGLE_MAPS_API_KEY':settings.GOOGLE_MAPS_API_KEY
        })

        return render(request, 'places/memory_edit.html', {'memory_form': memory_form})

    def post(self, request):
        memory_form = MemoryForm(request.POST)

        if memory_form.is_valid():
            new_memory = memory_form.save(request)
            return redirect('/memories/', permanent=True)

        return render(request, 'places/memory_edit.html', {'memory_form': memory_form})
