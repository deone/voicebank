from django.contrib import admin
from django import forms

from musicbox.models import *

class AlbumAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
	formfield = super(AlbumAdmin, self).formfield_for_dbfield(db_field,
		**kwargs)
	if db_field.name == 'info':
	    formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
	return formfield

admin.site.register(Album, AlbumAdmin)
admin.site.register(Track)
