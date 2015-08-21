# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from st_pages.views import *

urlpatterns = patterns('st_pages.views',
        url(r'^CV$', 'CV', name="CV"),
)