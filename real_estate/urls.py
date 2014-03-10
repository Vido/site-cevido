from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'real_estate.views.re_index', name='index'),
    url(r'^filter$', 'real_estate.views.re_filter', name='filter'),
    url(r'^details/(\d+)$', 'real_estate.views.re_details', name='details'),
    url(r'^photos/(\d+)$', 'real_estate.views.re_photos', name='photos'),
    url(r'^contact/$', 'real_estate.views.re_contact', name='contact'),
)
