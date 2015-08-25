__author__ = 'Sylvain'
# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from galery.views import Main_carousel

urlpatterns = patterns('galery.views',
    url(r'^$', Main_carousel.as_view(), name="carousel"),
)
