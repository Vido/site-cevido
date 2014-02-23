#Create your views here.

import sys
import random

from django.shortcuts import render_to_response
from django.template import RequestContext

from real_estate.models import Property
from django.http import Http404

def re_index(request):
    template = 'real_estate/base_filter.html'

    dictionary = {}

    context_instance = RequestContext(request)

    response = render_to_response(template, dictionary, context_instance)
    return response


#def re_form(request):
#    template = 'real_estate/base_filter.html'
#
#    dictionary = {}
#
#    context_instance = RequestContext(request)
#
#    response = render_to_response(template, dictionary, context_instance)
#    return response
#
#

def re_filter(request):

    if request.method == "POST":
        raise Http404

    template = 'real_estate/filtered_list.html'

    lte_arg = int(request.GET.get('price__lte', sys.maxint))
    gte_arg = int(request.GET.get('price__gte', 0))
    
    properties = Property.objects.all()
    properties = properties.filter(price__lte=lte_arg)
    properties = properties.filter(price__gte=gte_arg)

    dictionary = {
       'property_list': properties,
    }

    context_instance = RequestContext(request)

    response = render_to_response(template, dictionary, context_instance)
    return response

