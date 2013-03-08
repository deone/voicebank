from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.template.defaultfilters import slugify
from django.contrib.sites.models import Site

class Article(FlatPage):
    image = models.ImageField(upload_to="article_images")

    def save(self, *args, **kwargs):
	self.url = '/' + slugify(self.title) + '/'
	self.enable_comments = False
	self.registration_required = False
	super(Article, self).save(*args, **kwargs)
