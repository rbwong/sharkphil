from django.db import models

from make.models import Make


class Series(models.Model):
    make = models.ForeignKey(Make)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="%Y/%m/%d", default='banner-default.jpg')
    hover_image = models.ImageField(upload_to="%Y/%m/%d", default='banner-default.jpg')
    banner = models.ImageField(upload_to="%Y/%m/%d", default='banner-default.jpg')

    def __unicode__(self):
        return self.name
