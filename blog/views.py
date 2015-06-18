# -*- coding: utf8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from blog.models import Article, Categorie, Comments
from blog.forms import NewCom

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
        
    article = recov_articles(id_article, slug)
    comments = view_comments(id_article)
        
    return render(request, "blog/article.html", {'article' : article, 'comments' : comments})

def recov_articles(id_article, slug):
    """
    recover the concerned article
    """
    article = get_object_or_404(Article, id = id_article, slug = slug)
    
    return article

def view_comments(article_id):
    """
    return comments of an article
    """
    comments = Comments.objects.filter(article = article_id).order_by('-date')
    
    return comments

def leave_comments(request, id_article, slug):
    """form for new comment creation"""
    #POST is used to return form data
    if request.method == 'POST':
        form = NewCom(request.POST, article=id_article)
        if form.is_valid():
            form.save()
            return redirect(view_article)
    #no POST data so certainly first instance of the page
    else:
        form = NewCom()
        
    article = recov_articles(id_article, slug)
    comments = view_comments(id_article)

    return render(request, "blog/commentaire.html", {'article' : article, 'comments' : comments, 'formu' : form})

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """

    text = "Vous avez demandé les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
