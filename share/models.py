from django.db import models
from django.conf import settings
from django.utils import timezone

def set_path(instance):
    return "%s" %(instance.share_id)


class ShareFile(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    room = models.ForeignKey('ShareAlbum', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    upload_date = models.DateTimeField(default=timezone.now)
    file_size = models.IntegerField()

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
    storage = models.IntegerField()





# Create your models here.
