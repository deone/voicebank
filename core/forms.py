from django import forms

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


class BookingForm(forms.Form):
    pass


class ContactForm(forms.Form):
    pass
