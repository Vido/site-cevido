import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cevido.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cevido.views.home', name='home'),
    url(r'^home/$', 'cevido.views.home', name='home'),
    url(r'^contact/$', 'cevido.views.contact', name='contact'),
    url(r'^photologue/', include('photologue.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^real_estate/', include('real_estate.urls')),
    url(r'^filter/', include('filter.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': settings.STATIC_ROOT}),
)
