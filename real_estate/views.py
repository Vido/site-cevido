# -*- coding: utf-8 -*-

import sys
import random

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect

from real_estate.models import Property
from django.http import Http404


def re_index(request):
    
    if request.method == "POST":
        raise Http404
    
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

    # Workaround to show thumbnail
    for p in properties:
        p.thumbnail = p.photo_gallery.photos.all()[0].get_thumbnail_url
        print p.thumbnail

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

    template_descr = "Olá, tenho interesse no imovel {address}"
    context_descr = {
        'address': property.address,
    }
    description = template_descr.format(**context_descr)

    dictionary = {
        'property': property,
        'description': description,
    }

    context_instance = RequestContext(request)

    response = render_to_response(template, dictionary, context_instance)

    return response


def re_contact(request):

    if request.method == "POST":
        raise Http404

    try:
        property_pk = int(request.GET.get('pk', None))
        property = Property.objects.get(pk=property_pk)
    except:
        raise Http404

    description = request.GET.get('description', None)
    name = request.GET.get('name', None)
    email = request.GET.get('email', None)
    phone = request.GET.get('phone', None)
    newsletter = request.GET.get('newsletter', True)

    # TODO: Send an email or something
    return redirect(property.get_absolute_url())
 
