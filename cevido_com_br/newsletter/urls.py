from django.conf.urls import patterns
# from django.conf.urls import include
from django.conf.urls import url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',  # noqa
    url(r'^subscribe/$', 'newsletter.views.subscribe', name='subscribe'),
    url(r'^unsubscribe/$', 'newsletter.views.unsubscribe', name='unsubscribe'),
)
