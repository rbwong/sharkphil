from django.contrib import admin
from .models import Promo


class PromoAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')

admin.site.register(Promo, PromoAdmin)
