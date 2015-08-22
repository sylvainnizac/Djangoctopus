__author__ = 'Sylvain'
# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from blog.views import List_Articles, Single_Article

urlpatterns = patterns('blog.views',
    url(r'^$', , name="carousel"),
)