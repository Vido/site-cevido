# -*- coding: utf-8 -*-

import sys
import json
import random

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import Http404

from photologue.models import Photo

from real_estate.models import Property


def re_index(request):
    
    if request.method == "POST":
        raise Http404

    context_instance = RequestContext(request)
    template = 'real_estate/base_filter.html'

    response = render_to_response(template, {}, context_instance)
    return response


def re_filter(request):

    if request.method == "POST":
        raise Http404


    lte_arg = int(request.GET.get('price__lte', sys.maxint))
    gte_arg = int(request.GET.get('price__gte', 0))
    
    properties = Property.objects.all().order_by('timestamp')
    properties = properties.filter(price__lte=lte_arg)
    properties = properties.filter(price__gte=gte_arg)

    # Workaround to show thumbnail
    for p in properties:
        p.thumbnail = p.photo_gallery.photos.all()[0].get_thumbnail_url

    dictionary = {
       'property_list': properties,
    }

    context_instance = RequestContext(request)
    template = 'real_estate/filtered_list.html'

    response = render_to_response(template, dictionary, context_instance)
    return response


def re_details(request, property_pk):

    try:
        property = Property.objects.get(pk=property_pk)
    except:
        raise Http404

    
    context_descr = {
        'address': property.address,
    }
    template_descr = "Olá, tenho interesse no imovel {address}"
    description = template_descr.format(**context_descr)
   
    thumbnail_list = property.photo_gallery.photos.all()

    dictionary = {
        'property': property,
        'description': description,
        'thumbnails_list': thumbnail_list,
    }

    context_instance = RequestContext(request)
    template = 'real_estate/base_details.html'

    response = render_to_response(template, dictionary, context_instance)
    return response


def re_contact(request, property_pk):

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


def re_photos(request, photo_pk):
 
    if request.method == 'POST':
        raise Http404

    photo = Photo.objects.get(pk=photo_pk)
    
    dictionary = {
        'get_display_url': photo.get_display_url(),
    }

    response = HttpResponse(
        json.dumps(dictionary),
        content_type="application/json"
    )

    return response
