from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from vbank.models import *
from accounts.models import GENDER_CHOICES

LANGUAGES = (
	('', 'Select Language'),
	('English', 'English'),
	('Pidgin English', 'Pidgin English'),
	('Yoruba', 'Yoruba'),
	('Igbo', 'Igbo'),
	('Hausa', 'Hausa'),
	)

AGE_GROUP_CHOICES = (
	('', 'Select Age Group'),
	('K', 'Kid (0 - 15)'),
	('A', 'Adult (16+)'),
	)

class ClipSearchForm(forms.Form):
    # from accounts import calculate_age
    # 'age': calculate_age(request.user.profile.birthday),
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False,
	    empty_label="Select Category", widget=forms.Select(attrs={'class': 'form-control'}))
    language = forms.ChoiceField(choices=LANGUAGES, required=False,
	    widget=forms.Select(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False,
	    widget=forms.Select(attrs={'class': 'form-control'}))
    age_group = forms.ChoiceField(choices=AGE_GROUP_CHOICES, required=False,
	    widget=forms.Select(attrs={'class': 'form-control'}))

class VoiceClipForm(forms.Form):
    user = forms.CharField(max_length=5)
    voice_clip = forms.FileField()
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    language = forms.ChoiceField(choices=LANGUAGES,
	    widget=forms.Select(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
	    empty_label="Category", widget=forms.Select(attrs={'class': 'form-control'}))

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
