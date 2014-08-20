from django.contrib import admin
from .models import Profile


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'banner')

admin.site.register(Profile, CompanyAdmin)
