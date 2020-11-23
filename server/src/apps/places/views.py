from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)
from places.models import Memory

class PlacesListView(ListView):
    """Return list of Mem."""

    model = Memory
    paginate_by = 2
    # model = test
    # paginate_by = 2
