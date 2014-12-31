from django.conf.urls import url
from django.conf.urls import patterns

urlpatterns = patterns('',  # noqa
    url(r'^$', 'real_estate.views.re_index', name='index'),
    url(r'^details/(\d+)$', 'real_estate.views.re_details', name='details'),
    url(r'^photos/(\d+)$', 'real_estate.views.re_photos', name='photos'),
    url(r'^contact/(\d+)$', 'real_estate.views.re_contact', name='contact'),
)
