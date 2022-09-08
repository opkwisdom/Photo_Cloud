from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from .models import Photo, Video, File


class HomeView(ListView):
    template_name = 'home.html'




