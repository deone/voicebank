from django.contrib import admin
from django import forms

from sounds.models import *

class SoundAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
	formfield = super(SoundAdmin, self).formfield_for_dbfield(db_field,
		**kwargs)
	if db_field.name == 'info':
	    formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
	return formfield

admin.site.register(SoundCollection, SoundAdmin)
admin.site.register(Track)
