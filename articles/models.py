from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.template.defaultfilters import slugify
from django.contrib.sites.models import Site

from datetime import datetime

ARTICLE_TYPE_CHOICES = (
    ("News", "News"),
    ("Voice Tips", "Voice Tips"),
    ("Radio Connect", "Radio Connect"),
    ("Others", "Others"),
)

class Article(FlatPage):
    image = models.ImageField(upload_to="article_images")
    featured = models.BooleanField()
    article_type = models.CharField(max_length=15, choices=ARTICLE_TYPE_CHOICES)
    date_created = models.DateTimeField(default=datetime.now, editable=False)
    date_featured = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-date_featured']

    def save(self, *args, **kwargs):
	self.url = '/' + slugify(self.title) + '/'
        try:
	    orig = Article.objects.get(pk=self.pk)
	except Article.DoesNotExist:
	    pass
	else:
	    if not orig.featured and self.featured:
		self.date_featured = datetime.now()

        featured_articles = Article.objects.filter(featured=True).filter(article_type=self.article_type)
        if featured_articles and self.featured:
            featured_article = featured_articles[0]
            featured_article.featured = False
            featured_article.save()

	super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
	return '/articles' + self.url
