from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.template.defaultfilters import slugify
from django.contrib.sites.models import Site

from datetime import datetime

ARTICLE_TYPE_CHOICES = (
    ("News", "News"),
    ("Voice Tips", "Voice Tips"),
    ("Others", "Others"),
    ("Radio Connect", "Radio Connect"),
)

class Article(FlatPage):
    image = models.ImageField(upload_to="article_images")
    featured = models.BooleanField()
    article_type = models.CharField(max_length=15, choices=ARTICLE_TYPE_CHOICES)
    date_created = models.DateTimeField(default=datetime.now, editable=False)
    date_featured = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
	self.url = '/' + slugify(self.title) + '/'
	if self.featured:
	    self.date_featured = datetime.now()
	super(Article, self).save(*args, **kwargs)
