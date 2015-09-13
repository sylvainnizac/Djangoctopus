# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('snippets.views',
    url(r'^$', TemplateView.as_view(template_name='snippets/snipaccueil.html'), name="snipaccueil"),
    url(r'^json$', "snippet_list", name="sniplist"),
    url(r'^(?P<pk>[0-9]+)/json$', "snippet_detail", name="snipdetail"),
    url(r'^(?P<pk>[0-9]+)/$', TemplateView.as_view(template_name='snippets/snipdetail.html')),
)

# ajout de format en fin d'url
urlpatterns = format_suffix_patterns(urlpatterns)