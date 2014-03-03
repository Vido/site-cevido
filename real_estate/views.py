#Create your views here.

import sys
import random

from django.shortcuts import render_to_response
from django.template import RequestContext

from real_estate.models import Property
from django.http import Http404


def re_index(request):
    template = 'real_estate/base_filter.html'

    dictionary = {
#        'property_list': properties,
    }

    context_instance = RequestContext(request)

    response = render_to_response(template, dictionary, context_instance)
    return response


def re_filter(request):

    if request.method == "POST":
        raise Http404

    template = 'real_estate/filtered_list.html'

    lte_arg = int(request.GET.get('price__lte', sys.maxint))
    gte_arg = int(request.GET.get('price__gte', 0))
    
    properties = Property.objects.all().order_by('timestamp')
    properties = properties.filter(price__lte=lte_arg)
    properties = properties.filter(price__gte=gte_arg)

    dictionary = {
       'property_list': properties,
    }

    context_instance = RequestContext(request)

    response = render_to_response(template, dictionary, context_instance)
    return response


def re_details(request, property_pk):
    template = 'real_estate/base_details.html'

    try:
        property = Property.objects.get(pk=property_pk)
    except:
        raise Http404

    dictionary = {
        'property': property,
    }

    context_instance = RequestContext(request)

    response = render_to_response(template, dictionary, context_instance)
    return response


