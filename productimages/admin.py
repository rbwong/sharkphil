from django.contrib import admin
from .models import ProductImage


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'image', 'description')

admin.site.register(ProductImage, ProductImageAdmin)
