# -*- coding: utf8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
#generic views are ready to use standardsviews
from django.views.generic import ListView
from datetime import datetime
from blog.models import Article, Categorie, Comments
from blog.forms import NewCom

# Create your views here.

class List_Articles(ListView):
    """
    This class allows to quickly call the article list. and return  other useful data for the page
    """
    model=Article
    context_object_name="articles"
    template_name="blog/index.html"
    paginate_by = 5

    def get_queryset(self):
        """Allows (under conditions) to sort articles by categorie"""
        if len(self.kwargs)>0:
            return Article.objects.filter(categorie__id=self.kwargs['id_categorie'])
        else:
            return Article.objects.all()

    def get_context_data(self, **kwargs):
        """recover and modify the context data"""
        context = super(List_Articles, self).get_context_data(**kwargs)
        #add the new context data
        context['categories'] = Categorie.objects.all()
        return context

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
