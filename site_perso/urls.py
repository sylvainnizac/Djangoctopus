"""site_perso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name="admin"),
    url(r'^blog/', include('blog.urls')),
]

handler404 = 'blog.views.my_custom_page_not_found_view'
handler500 = 'blog.views.my_custom_error_view'
handler403 = 'blog.views.my_custom_permission_denied_view'
handler400 = 'blog.views.my_custom_bad_request_view'
