from django import forms

from core.models import *

LANGUAGES = (
	('English', 'English'),
	('Pidgin English', 'Pidgin English'),
	('Yoruba', 'Yoruba'),
	('Igbo', 'Igbo'),
	('Hausa', 'Hausa'),
	)

class VoiceClipForm(forms.Form):
    voice_clip = forms.FileField()
    name = forms.CharField(max_length=30)
    language = forms.ChoiceField(choices=LANGUAGES)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
	    empty_label="Select...")

    def clean(self):
	clip = self.cleaned_data.get('voice_clip', False)

	if clip:
	    if clip.content_type != 'audio/mp3':
		raise forms.ValidationError("Please upload an mp3 audio file")
	    if clip.name.split(".")[-1] != 'mp3':
		raise ValidationError("File does not have .mp3 extension")

	return self.cleaned_data

    def save(self, request):
	voice_clip = VoiceClip.objects.create(user=request.user,
		name=self.cleaned_data['name'],
		voice_clip=self.cleaned_data['voice_clip'],
		language=self.cleaned_data['language'])

	VoiceClipCategory.objects.create(voice_clip=voice_clip,
		category=self.cleaned_data['category'])
