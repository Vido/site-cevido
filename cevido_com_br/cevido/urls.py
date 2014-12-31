import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.sites.models import Site

admin.autodiscover()
admin.site.unregister(Site)

urlpatterns = patterns('',  # noqa
    # Examples:
    # url(r'^$', 'cevido.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'cevido.views.home', name='home'),
    url(r'^home/$', 'cevido.views.home', name='home'),
    url(r'^contact/$', 'cevido.views.contact', name='contact'),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^real_estate/', include('real_estate.urls')),
    url(r'^filter/', include('filter.urls')),
)

if not settings.PRODUCTION:
    from django import get_version
    if int(get_version().split('.')[1]) >= 6:
        urlpatterns += patterns('',  # noqa
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT}),
            url(r'^admin/static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT}),
        )
    else:
        urlpatterns += patterns('',  # noqa
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT,
                  'show_indexes': True}),
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT,
                  'show_indexes': True}),
            url(r'^admin/static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT,
                  'show_indexes': True}),
        )

urlpatterns += patterns('',  # noqa
    url(r'^admin/', include(admin.site.urls)),
)
