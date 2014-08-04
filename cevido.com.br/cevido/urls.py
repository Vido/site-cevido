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
)

if not settings.PRODUCTION:
    from django import get_version
    if int(get_version().split('.')[1]) >= 6:
        urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT}),
            url(r'^admin/static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT}),
        )
    else:
        urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT,
                 'show_indexes' : True}),
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT,
                 'show_indexes' : True}),
            url(r'^admin/static/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT,
                 'show_indexes' : True}),
        )

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
