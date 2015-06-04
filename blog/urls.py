from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'home'),
    url(r'^article/(?P<id_article>\d+)$', 'view_article'),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', 'list_articles'),
)
