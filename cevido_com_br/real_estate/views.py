# -*- coding: utf-8 -*-

import json
import random

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import Http404

from real_estate.models import Property
from real_estate.models import Photo
from filter.models import FilterKind
from filter.forms import KindForm


def re_index(request):

    if request.method == "POST":
        raise Http404

    dictionary = {
        'form': KindForm(),
    }

    context_instance = RequestContext(request)
    template = 'real_estate/base_filter.html'

    response = render_to_response(template, dictionary, context_instance)
    return response


def re_details(request, property_pk):
    try:
        this_property = Property.objects.get(pk=property_pk)
    except:
        raise Http404

    context_descr = { 'address': this_property.address, }
    template_descr = u"Olá, tenho interesse no imovel {address}"
    description = template_descr.format(**context_descr)

    photo_list = Photo.objects.filter(fk_property=this_property)

    dictionary = {
        'property': this_property,
        'description': description,
        'photo_list': photo_list,
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
        'get_display_url': photo.image_file.url,
    }

    response = HttpResponse(
        json.dumps(dictionary),
        content_type="application/json"
    )

    return response
