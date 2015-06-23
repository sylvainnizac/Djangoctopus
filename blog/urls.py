# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from blog.views import List_Articles, Single_Article, Leave_Comments

urlpatterns = patterns('blog.views',
    url(r'^$', List_Articles.as_view(), name="list_articles"),
    url(r'^categorie/(?P<id_categorie>\d+)$', List_Articles.as_view(), name="blog_categorie"),
    url(r'^article/(?P<pk>\d+)$', Single_Article.as_view(), name="lire_article"),
    url(r'^comment/(?P<pk>\d+)-(?P<slug>.+)$', Leave_Comments.as_view(), name="commentaire"),
)

