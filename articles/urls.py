from django.conf.urls import url, patterns

from articles.views import ArticleListView

urlpatterns = patterns('articles.views',
    url(r'^$', ArticleListView.as_view(), name='articles_home'),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
