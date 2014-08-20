from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from series.views import SeriesPage

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^series/([\w-]+)/$', SeriesPage.as_view(), name='series_page'),
                       )
