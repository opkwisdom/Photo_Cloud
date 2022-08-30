from django.db import models
from django.conf import settings
from django.utils import timezone
from hashlib import sha256
#from apps import pilling
from PIL import Image
import os
from random import random
import pillow_heif
import googlemaps

#now testing

def set_path(instance):
    return "%s"%instance.album_id

class ShareFile(models.Model):

    #__new__
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    album_id = models.ForeignKey(models.ShareAlbum,on_delte=models.CASCADE)
    name = models.CharField(max_length=40)
    upload_date = models.DateTimeField(default=timezone.now)

    def set_upload(self):
        return "share/"+self.album_id

    class Meta:
        abstract = True


class Photo(ShareFile):
    # field (author room name upload_date gps)
    photo = models.ImageField(upload_to = "share/"+set_path+"/photo/")
    gps = models.CharField()

    pass
class File(ShareFile):
    file=models.FileField(upload_to="share/"+set_path+"/photo/")
    ext = models.CharField(max_length=8)






class Video(ShareFile):
    video = models.FileField(upload_to = "share/"+set_path+"/video")

class ShareAlbum(models.Model):
    album_id = models.CharField(max_length=20)






# Create your models here.
