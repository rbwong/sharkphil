from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from promos.views import PromoPage

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^promos/$', PromoPage.as_view(), name='promo_page'),
                       )
