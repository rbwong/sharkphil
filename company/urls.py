from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from company.views import IndexPage

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', IndexPage.as_view(), name='index_page'),
                       )
