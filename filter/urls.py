from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^no_filter$', 'filter.views.f_no_filter', name='no_filter'),
    url(r'^ap_filter$', 'filter.views.f_ap_filter', name='ap_filter'),
    url(r'^select_form$', 'filter.views.f_select_form', \
            name='select_form'),
)

