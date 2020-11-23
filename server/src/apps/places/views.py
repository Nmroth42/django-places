from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)
# Create your views here.

class PlacesListView(ListView):
    """Return list of articles."""
    pass
    # model = test
    # paginate_by = 2
