from django.views.generic import ListView

from articles.models import Article

class ArticleListView(ListView):

    model = Article
