# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from blog.views import List_Articles, Single_Article

urlpatterns = patterns('blog.views',
    url(r'^$', List_Articles.as_view(), name="list_articles"),
    url(r'^categorie/(?P<id_categorie>\d+)$', List_Articles.as_view(), name="blog_categorie"),
    url(r'^article/(?P<pk>\d+)-(?P<slug>.+)$', Single_Article.as_view(), name="lire_article"),
    url(r'^comment/(?P<id_article>\d+)-(?P<slug>.+)$', 'leave_comments', name="commentaire"),
)

