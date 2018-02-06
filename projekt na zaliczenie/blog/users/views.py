
from django.shortcuts import render
from django.views.generic.edit import UpdateView, FormView

# Create your views here.
from users.models import BlogUser


def auth(request):
    return render(request, 'auth.html')



