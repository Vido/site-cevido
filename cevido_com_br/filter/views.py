import os
import sys
import random

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

from real_estate.models import Property
from real_estate.models import Photo
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


def generic_boundary_filter(request, boundaries=[],
        template_filename='f_generic_list.html'):

    filter_kwargs = parse_filter_args(request.GET, boundaries)

    properties = Property.objects.all().order_by('timestamp')
    properties = properties.filter(**filter_kwargs)

    dictionary = {
       'property_list': properties,
    }

    context_instance = RequestContext(request)
    template = os.path.join('filter', template_filename)

    response = render_to_response(template, dictionary, context_instance)
    return response


def f_no_filter(request):
    if not request.method == "GET":
        raise Http404

    return generic_boundary_filter(request)

# apartment
def f_ap_filter(request):
    if not request.method == "GET":
        raise Http404

    boundaries = [
        'price__lte', 'price__gte',
        'rooms__lte', 'rooms__gte',
        # ETC ...
    ]

    return generic_boundary_filter(request, boundaries)

# land lot
def f_ll_filter(request):
    if not request.method == "GET":
        raise Http404

    boundaries = [
        'price__lte', 'price__gte',
        'area__lte', 'area__gte',
    ]

    return generic_boundary_filter(request, boundaries)

