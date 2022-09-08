from django.db import models
from django.conf import settings
from django.utils import timezone

def set_path(instance):
    return "%s" %(instance.album_id)


class ShareFile(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    room = models.ForeignKey(models.ShareAlbum, on_delte=models.CASCADE)
    name = models.CharField(max_length=40)
    upload_date = models.DateTimeField(default=timezone.now)
    file_size = models.IntegerField(max_length=10)

    class Meta:
        abstract = True


class Photo(ShareFile):
    # field (author room name upload_date gps)
    photo = models.ImageField(upload_to="share/photo/")
    gps_addr = models.CharField(max_length=20, blank=True)
    pixel = models.CharField(max_length=20)
    ocr_tag = models.SlugField(blank=True)

class File(ShareFile):
    file = models.FileField(upload_to="share/file/")
    ext = models.CharField(max_length=8)

class Video(ShareFile):
    video = models.FileField(upload_to="share/video/")
    gps_addr = models.CharField(max_length=20, blank=True)

class ShareAlbum(models.Model):
    album_admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    share_id = models.CharField(max_length=20)
    storage = models.IntegerField(max_length=10)





# Create your models here.
