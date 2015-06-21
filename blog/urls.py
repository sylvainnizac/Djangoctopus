# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from django.views.generic import ListView
from blog.models import Article

urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(model=Article, context_object_name="articles", template_name="blog/index.html")),
    url(r'^article/(?P<id_article>\d+)-(?P<slug>.+)$', 'view_article', name="afficher article"),
    url(r'^comment/(?P<id_article>\d+)-(?P<slug>.+)$', 'leave_comments', name="commentaire"),
)

