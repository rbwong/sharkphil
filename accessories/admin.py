from django.contrib import admin
from .models import Accessory


class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('series', 'name', 'image', 'description')

admin.site.register(Accessory, AccessoryAdmin)
