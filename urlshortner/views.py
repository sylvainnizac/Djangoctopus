# -*- coding: utf8 -*-
from django.shortcuts import redirect, render, get_object_or_404
from urlshortner.models import MiniURL
from urlshortner.forms import AskToShort

# Create your views here.

def short_url_list(request):
    """retourne la liste complète des short URL créées dans l'ordre décroissant d'utilisation"""
    surls = MiniURL.objects.order_by('-nbacces')
    return render(request, "urlshortner/short_url_list.html", {'surls' : surls})

def new_short_url(request):
    """formulaire de création d'URL courte"""
    #methode post est celle utilisée pour renvoyer les données du formulaire
    if request.method == 'POST':
        form = AskToShort(request.POST)
        if form.is_valid():
            form.save()
        pass
    #donc si pas de données POST c'est qu'on arrive pour la première fois sur la page
    else:
        form = AskToShort()

    return render(request, "urlshortner/new_short_url.html", locals())
    
def url_redirection(request, short):
    """make the redirection and increase the counter"""
    url = get_object_or_404(MiniURL, shorturl = short)
    url.nbacces += 1
    url.save()
    
    return redirect(url.longurl)
