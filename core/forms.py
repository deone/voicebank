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
    voice_clip = forms.FileField()
    name = forms.CharField(max_length=30)
    language = forms.ChoiceField(choices=LANGUAGES,
	    widget=forms.Select(attrs={'class': 'chzn-select'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
	    empty_label="Category", widget=forms.Select(attrs={'class': 'chzn-select'}))

    def clean(self):
	clip = self.cleaned_data.get('voice_clip', False)

	if clip:
	    if clip.content_type not in ['audio/mp3', 'audio/mpeg']:
		raise forms.ValidationError("Please upload an mp3 audio file")
	    if clip.name.split(".")[-1] != 'mp3':
		raise forms.ValidationError("File does not have .mp3 extension")

	return self.cleaned_data

    def save(self, request):
	voice_clip = VoiceClip.objects.create(user=request.user,
		name=self.cleaned_data['name'],
		voice_clip=self.cleaned_data['voice_clip'],
		language=self.cleaned_data['language'],
		category=self.cleaned_data['category'])

	return voice_clip


class BookingForm(forms.Form):
    user = forms.CharField(max_length=5)
    name_on_teller = forms.CharField(max_length=30)
    date_of_payment = forms.DateField(('%m/%d/%Y',), help_text="Enter date in MM/DD/YYYY format")
    bank_name = forms.CharField(max_length=30)

    def save(self):
	user = get_object_or_404(User, pk=self.cleaned_data['user'])
	booking = Booking.objects.create(user=user, 
		name_on_teller=self.cleaned_data['name_on_teller'],
		date_of_payment=self.cleaned_data['date_of_payment'],
		bank_name=self.cleaned_data['bank_name'])

	return booking


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
