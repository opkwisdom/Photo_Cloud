from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, FormView
from .forms import FileForm, PhotoForm, VideoForm
from .models import Photo, Video, File, ShareAlbum
from PIL import Image
import os
class FileFieldFormView(LoginRequiredMixin, FormView):
    form_class = FileForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = ''#reverse()  # Replace with your URL or reverse(). #album redirect
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                pf = Image.open(f.)


                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class PhotoFieldFormView(LoginRequiredMixin, FormView):
    form_class = PhotoForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = ''#reverse()  # Replace with your URL or reverse(). #album redirect
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                name=f
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
# Create your views here.
class AlbumView(LoginRequiredMixin, ListView):
    model = ShareAlbum
    template_name = 'sharer.html'