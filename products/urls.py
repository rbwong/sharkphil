from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from products.views import ProductPage

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^product/([\w-]+)/$', ProductPage.as_view(), name='product_page'),
                       )
