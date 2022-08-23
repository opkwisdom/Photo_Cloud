from django.db import models
from django.conf import settings
from django.utils import timezone

#now testing

class ShareFile(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=40)
    upload_date = models.DateTimeField(default=timezone.now)


class Photo(ShareFile):
    photo = models.ImageField(upload_to="/")
    pass
class File(ShareFile):
    pass

class Video(ShareFile):
    pass

class ShareAlbum(models.Model):
    model=models.ForeignKey(ShareFile,on_delte=models.CASCADE)





# Create your models here.
