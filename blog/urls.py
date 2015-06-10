from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'home', name="accueil"),
    url(r'^article/(?P<id_article>\d+)$', 'view_article', name="afficher article"),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', 'list_articles', name="afficher liste articles"),
    url(r'^dateactu/)$', 'date_actuelle', name="date actuelle"),
)
