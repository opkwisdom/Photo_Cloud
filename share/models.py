from django.db import models
from django.conf import settings
from django.utils import timezone
from hashlib import sha256
#from apps import pilling
from PIL import Image
import pyheif
import googlemaps

#now testing

class ShareFile(models.Model):

    #__new__
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    room = models.ForeignKey(models.ShareAlbum,on_delte=models.CASCADE)
    name = models.CharField(max_length=40)
    upload_date = models.DateTimeField(default=timezone.now)


class Photo(ShareFile):
    # __new__
    # field (author room name upload_date gps)
    gps = models.CharField()

    #init def
    def __init__(self):
        #field init & img init
        photo = models.ImageField(upload_to="share/"+self.room.locate+"/image/")
        img_p = Image(photo)
        self.name = img_p.filename
        self.gps = img_p._getexif()


    pass
class File(ShareFile):
    def __init__(self):
        file=models.FileField(upload_to="share/"+self.room.locate+"/file/")
    pass

class Video(ShareFile):
    def __init__(self):
        video=models.FileField(upload_to="share/"+self.room.locate+"/video")
    pass

class ShareAlbum(models.Model):
    pass





# Create your models here.
