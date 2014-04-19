import sys
import random

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

from real_estate.models import Property


def f_get_form(request):
    pass


def f_no_filter(request):

    if request.method == "POST":
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
    template = 'filter/filtered_list.html'

    response = render_to_response(template, dictionary, context_instance)
    return response


def f_ap_filter(request):

    if request.method == "POST":
        raise Http404


    _price_lte = int(request.GET.get('price__lte', sys.maxint))
    _price_gte = int(request.GET.get('price__gte', 0))

    _rooms_lte = int(request.GET.get('rooms__lte', sys.maxint))
    _rooms_gte = int(request.GET.get('rooms__gte', 0))

    #TODO: Find a smarter way

    properties = Property.objects.all().order_by('timestamp')

    properties = properties.filter(price__lte=_price_lte)
    properties = properties.filter(price__gte=_price_gte)

    properties = properties.filter(rooms__lte=_rooms_lte)
    properties = properties.filter(rooms__gte=_rooms_gte)


    # Workaround to show thumbnail
    for p in properties:
        p.thumbnail = p.photo_gallery.photos.all()[0].get_thumbnail_url

    dictionary = {
       'property_list': properties,
    }

    context_instance = RequestContext(request)
    template = 'filter/filtered_list.html'

    response = render_to_response(template, dictionary, context_instance)
    return response

