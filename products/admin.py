from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',  'image', 'banner', 'description')

admin.site.register(Product, ProductAdmin)
