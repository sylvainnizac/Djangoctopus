# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from galery.views import Main_carousel, Main_galery

urlpatterns = patterns('galery.views',
    url(r'^$', Main_carousel.as_view(), name="carousel"),
    url(r'^photos/$', Main_galery.as_view(), name="galery"),
    url(r'^photos/json$', 'pics_list', name="photos_all"),
    url(r'^photos/F/(?P<faction>\d+)/json$', 'pics_list', name="photo_faction"),
    url(r'^photos/s/(?P<secto>\d+)/json$', 'pics_list', name="photo_sectorielle"),
    url(r'^photos/f/(?P<fig>\d+)/json$', 'pics_list', name="photo_figurine"),
)
