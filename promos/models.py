from django.db import models


class Promo(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True)

    def __unicode__(self):
        return self.title
