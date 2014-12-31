import random

from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    template = 'cevido/intro.html'

    list_wallpapers = [
        # 'tonight-situation-with-lamp.jpg',
        'modern-dining-room2.jpg',
    ]

    dictionary = {'wallpaper': random.choice(list_wallpapers)}

    context_instance = RequestContext(request)

    response = render_to_response(template, dictionary, context_instance)
    return response


def contact(request):
    template = 'cevido/contact.html'

    list_wallpapers = [
        'tonight-situation-with-lamp.jpg',
        # 'modern-dining-room2.jpg',
    ]

    dictionary = {'wallpaper': random.choice(list_wallpapers)}

    context_instance = RequestContext(request)

    response = render_to_response(template, dictionary, context_instance)
    return response
