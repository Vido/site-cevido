import os
import sys
import random

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

from real_estate.models import Property
from filter.models import FilterKind


def parse_filter_args(GET, boundaries=[], options=[]):

    values = [
        GET.get(boundary, sys.maxint)
        if '__lte' in boundary
        else GET.get(boundary, 0)
        for boundary in boundaries
    ]

    filter_kwargs = {
        boundary: int(value)
        for boundary, value in zip(boundaries, values)
    }

    return filter_kwargs


def f_select_form(request):
    if not request.method == "GET":
        raise Http404

    filter_pk = request.GET.get("kind", 0)
    f_kind = FilterKind.objects.get(pk=filter_pk)

    template = os.path.join('filter', f_kind.form_template)

    dictionary = {
        'list_template': f_kind.list_template,
    }

    context_instance = RequestContext(request)
    response = render_to_response(template, dictionary, context_instance)
    return response


def f_no_filter(request):

    if not request.method == "GET":
        raise Http404

    properties = Property.objects.all()

    # Workaround to show thumbnail
    for p in properties:
        p.thumbnail = p.photo_gallery.photos.all()[0].get_thumbnail_url

    #random.shuffle(list(properties))

    dictionary = {
       'property_list': properties,
    }

    context_instance = RequestContext(request)
    template = os.path.join('filter', 'f_generic_list.html')

    response = render_to_response(template, dictionary, context_instance)
    return response


def f_ap_filter(request):

    if not request.method == "GET":
        raise Http404

    boundaries = [
        'price__lte', 'price__gte',
        'rooms__lte', 'rooms__gte',
        # ETC ...
    ]

    filter_kwargs = parse_filter_args(request.GET, boundaries)

    properties = Property.objects.all().order_by('timestamp')
    properties = properties.filter(**filter_kwargs)

    # Workaround to show thumbnail
    for p in properties:
        p.thumbnail = p.photo_gallery.photos.all()[0].get_thumbnail_url

    dictionary = {
       'property_list': properties,
    }

    context_instance = RequestContext(request)
    template = 'filter/f_generic_list.html'

    response = render_to_response(template, dictionary, context_instance)
    return response


# land lot
def f_ll_filter(request):

    if not request.method == "GET":
        raise Http404

    boundaries = [
        'price__lte', 'price__gte',
        'area__lte', 'area__gte',
    ]

    filter_kwargs = parse_filter_args(request.GET, boundaries)

    properties = Property.objects.all().order_by('timestamp')
    properties = properties.filter(**filter_kwargs)

    # Workaround to show thumbnail
    for p in properties:
        p.thumbnail = p.photo_gallery.photos.all()[0].get_thumbnail_url

    dictionary = {
       'property_list': properties,
    }

    context_instance = RequestContext(request)
    template = 'filter/f_generic_list.html'

    response = render_to_response(template, dictionary, context_instance)
    return response

