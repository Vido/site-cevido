# Create your views here.

from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from newsletter.models import Subscriber


def subscribe(request):
    try:
        email_addr = request.GET.get('email', None)
        s = Subscriber(email=email_addr)
        s.clean()
    except:
        pass
    else:
        s.save()

    return redirect(reverse('cevido.views.contact', kwargs={}))


def unsubscribe(request):
    return redirect(reverse('cevido.views.contact', kwargs={}))
