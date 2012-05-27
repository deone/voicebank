from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from core.models import *

LANGUAGES = (
	('', 'Language'),
	('English', 'English'),
	('Pidgin English', 'Pidgin English'),
	('Yoruba', 'Yoruba'),
	('Igbo', 'Igbo'),
	('Hausa', 'Hausa'),
	)

class VoiceClipForm(forms.Form):
    user = forms.CharField(max_length=5)
    voice_clip = forms.FileField()
    name = forms.CharField(max_length=30)
    language = forms.ChoiceField(choices=LANGUAGES,
	    widget=forms.Select(attrs={'class': 'choose'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
	    empty_label="Category", widget=forms.Select(attrs={'class': 'choose'}))

    def clean_voice_clip(self):
	clip = self.cleaned_data.get('voice_clip', False)

	if clip:
	    if clip.content_type not in ['audio/mp3', 'audio/mpeg']:
		raise forms.ValidationError("Please upload an mp3 audio file.")
	    if clip.name.split(".")[-1] != 'mp3':
		raise forms.ValidationError("File does not have .mp3 extension.")

	return self.cleaned_data['voice_clip']

    def save(self):
	user = get_object_or_404(User, pk=self.cleaned_data['user'])
	voice_clip = VoiceClip.objects.create(user=user,
		name=self.cleaned_data['name'],
		voice_clip=self.cleaned_data['voice_clip'],
		language=self.cleaned_data['language'],
		category=self.cleaned_data['category'])

	return voice_clip


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    comment = forms.CharField(max_length=255, widget=forms.Textarea)

    def save(self):
	contact = Contact.objects.create(name=self.cleaned_data['name'],
		email=self.cleaned_data['email'],
		phone_number=self.cleaned_data['phone_number'],
		comment=self.cleaned_data['comment'])

	return contact
