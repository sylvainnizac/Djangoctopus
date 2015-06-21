# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from blog.views import List_Articles

urlpatterns = patterns('blog.views',
    url(r'^$', List_Articles.as_view(), name="liste articles"),
    url(r'^categorie/(?P<id_categorie>\d+)$', List_Articles.as_view(), name="blog_categorie"),
    url(r'^article/(?P<id_article>\d+)-(?P<slug>.+)$', 'view_article', name="afficher article"),
    url(r'^comment/(?P<id_article>\d+)-(?P<slug>.+)$', 'leave_comments', name="commentaire"),
)

