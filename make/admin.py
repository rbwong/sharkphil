from django.contrib import admin
from .models import Make


class MakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')

admin.site.register(Make, MakeAdmin)
