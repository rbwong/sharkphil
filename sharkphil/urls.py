from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('company.urls')),
    url(r'^', include('series.urls')),
    url(r'^', include('products.urls')),
    url(r'^', include('promos.urls')),
)
