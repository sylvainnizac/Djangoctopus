from django.shortcuts import redirect, render
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
        s = MiniURL.generer(6)
        pass
    #donc si pas de données POST c'est qu'on arrive pour la première fois sur la page
    else:
        form = AskToShort()

    return render(request, "urlshortner/new_short_url.html", locals())
