# -*- coding: utf8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from blog.models import Article, Categorie

# Create your views here.

def home(request):
    """génération de la page d'accueil'"""
    return home_articles(request)
    
def home_articles(request):
    """Retourne la liste des articles du plus récent au plus ancien"""
    articles = Article.objects.order_by('-date')
    return render(request, "blog/index.html", {'articles' : articles})

def view_article(request, id_article, slug):
    """ Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
        Son ID est le second paramètre de la fonction (pour rappel, le premier
        paramètre est TOUJOURS la requête de l'utilisateur) """
        
    article = get_object_or_404(Article, id = id_article, slug = slug)
        
    return render(request, "blog/article.html", {'article' : article})
    
def view_comments(request, id_article, slug):
    """
    return an article with it comments
    """
    article = get_object_or_404(Article, id = id_article, slug = slug)
    comments = Comments.objects.filter().order_by('-date)
    
    return render(request, "blog/article_comments.html", {'article' : article, 'comments' : comments})

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """

    text = "Vous avez demandé les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
