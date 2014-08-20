from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="%Y/%m/%d", default='banner-default.jpg')
    banner = models.ImageField(upload_to="%Y/%m/%d", default='banner-default.jpg')
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
