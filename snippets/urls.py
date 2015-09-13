# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('snippets.views',
    url(r'^$', "snippet_list", name="sniplist"),
    url(r'^(?P<pk>[0-9]+)/json$', "snippet_detail", name="snipdetail"),
    url(r'^(?P<pk>[0-9]+)/$', "snip_det_temp", name="snipdettemp"),
)

# ajout de format en fin d'url
urlpatterns = format_suffix_patterns(urlpatterns)
