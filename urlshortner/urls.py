# -*- coding: utf8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('urlshortner.views',
    url(r'^$', 'short_url_list', name="liste"),
    url(r'^new/$', 'new_short_url', name="new"),
    url(r'^nouveau/$', MiniURLCreate.as_view(), name="url_nouveau"),
    url(r'^(?P<short>\w{6})/$', 'url_redirection', name="redirection"),
)
