from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Autor
# Create your views here.

class AutorListView(ListView):
    model = Autor


class AutorDetailView(DeleteView):
    model = Autor