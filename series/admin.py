from django.contrib import admin
from .models import Series


class SeriesAdmin(admin.ModelAdmin):
    list_display = ('make',  'name', 'image', 'hover_image', 'banner')

admin.site.register(Series, SeriesAdmin)
