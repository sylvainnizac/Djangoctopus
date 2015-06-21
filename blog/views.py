# -*- coding: utf8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from blog.models import Article, Categorie, Comments
from blog.forms import NewCom

# Create your views here.

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
    comments = Comments.objects.filter(article = article_id, commentaire_visible=True).order_by('-date')
    
    return comments

def leave_comments(request, id_article, slug):
    """path for new comment creation"""
    #POST is used to return form data
    if request.method == 'POST':
        name_article = get_object_or_404(Article, id = id_article)
        form = NewCom(request.POST, article=name_article)
        if form.is_valid():
            form.save()
            return redirect(view_article, id_article, slug)
    #no POST data so certainly first instance of the page
    else:
        form = NewCom()
        
    article = recov_articles(id_article, slug)
    comments = view_comments(id_article)

    return render(request, "blog/commentaire.html", {'article' : article, 'comments' : comments, 'formu' : form})
