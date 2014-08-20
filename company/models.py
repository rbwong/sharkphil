from django.db import models

from geoposition.fields import GeopositionField


class Profile(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(blank=True)
    terms = models.TextField(blank=True)
    location = GeopositionField(blank=True)
    email = models.EmailField(blank=True)
    facebook = models.URLField(blank=True)
    phone_no1 = models.CharField(max_length=12, blank=True)
    phone_no2 = models.CharField(max_length=12, blank=True)
    phone_no3 = models.CharField(max_length=12, blank=True)
    phone_no4 = models.CharField(max_length=12, blank=True)
    phone_no5 = models.CharField(max_length=12, blank=True)
    phone_no6 = models.CharField(max_length=12, blank=True)
    logo = models.ImageField(upload_to="%Y/%m/%d", default='banner-default.jpg')
    banner = models.ImageField(upload_to="%Y/%m/%d", default='banner-default.jpg')
