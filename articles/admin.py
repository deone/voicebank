from django.contrib import admin
from django import forms
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site

from models import Article

class ArticleForm(FlatpageForm):

    class Meta:
	model = Article

    def __init__(self, *args, **kwargs):
	super(ArticleForm, self).__init__(*args, **kwargs)
	self.fields['url'].required = False
	self.fields['sites'].required = False

    def clean_url(self):
	return self.cleaned_data['url']

class ArticleAdmin(FlatPageAdmin):
    form = ArticleForm
    fieldsets = (
        (None, {'fields': ('title', 'image', 'content', 'sites')}),
        # (('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required')}),
    )

# Excluded fields
# url - use this as slug
# template_name, sites - do this programmatically when saving, enter the full URL /articles/slugified-title/
# enable_comments - default:False
# registration_required - default:False

admin.site.unregister(FlatPage)
admin.site.register(Article, ArticleAdmin)
