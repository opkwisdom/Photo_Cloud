from .models import Photo, File, Video
from django import forms

class PhotoForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = File
        fields = ["name", "photo", "gps_addr", "tag",]
class FileForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Photo
        fields = ["name", "file", "ext", ]
class VideoForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))

    class Meta:
        model = Video
        fields = ["name", "video","gps_addr", ]

