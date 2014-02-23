from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^subscribe/$', 'newsletter.views.subscribe', name='subscribe'),
    url(r'^unsubscribe/$', 'newsletter.views.unsubscribe', name='unsubscribe'),
)
