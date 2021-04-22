from django.shortcuts import render
from .models import *
from django.views.generic import ListView
# Create your views here.


class Home(ListView):
    model = AboutMe
    template_name = 'testapp/index.html'
    context_object_name = 'about'
