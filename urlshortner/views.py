# -*- coding: utf8 -*-
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from urlshortner.models import MiniURL
from urlshortner.forms import AskToShort

# Create your views here.

class MiniURLCreate(CreateView):
    model = MiniURL
    template_name = 'urlshortner/new_short_url.html'
    form_class = AskToShort
    success_url = reverse_lazy('liste')

def short_url_list(request):
    """return the list of URLs ordered by number of call"""
    surls = MiniURL.objects.order_by('-nbacces')
    return render(request, "urlshortner/short_url_list.html", {'surls' : surls})

def new_short_url(request):
    """form for short URL creation"""
    #POST is used to return form data
    if request.method == 'POST':
        form = AskToShort(request.POST)
        if form.is_valid():
            form.save()
            return redirect(short_url_list)
    #no POST data so certainly first instance of the page
    else:
        form = AskToShort()

    return render(request, "urlshortner/new_short_url.html", locals())
    
def url_redirection(request, short):
    """make the redirection and increase the counter"""
    url = get_object_or_404(MiniURL, shorturl = short)
    url.nbacces += 1
    url.save()
    
    return redirect(url.longurl)
