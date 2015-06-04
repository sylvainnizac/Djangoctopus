# -*- coding: utf8 -*-

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    """Message d'accueil basique, pas de paramètre en entrée, juste le message en sortie"""

    message = "<h1>Bienvenue sur mon blog!</1>"    
    return HttpResponse(message)

def view_article(request, id_article):
    """ Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
        Son ID est le second paramètre de la fonction (pour rappel, le premier
        paramètre est TOUJOURS la requête de l'utilisateur) """

    text = "Vous avez demandé l'article #{0} !".format(id_article)
    return HttpResponse(text)

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """

    text = "Vous avez demandé les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)
