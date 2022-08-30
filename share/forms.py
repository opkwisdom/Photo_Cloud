from .models import Photo, File, Video
from django import forms

class PhotoForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

