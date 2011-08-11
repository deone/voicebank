from django import forms

from core.models import VoiceClip

class VoiceClipForm(forms.ModelForm):

    class Meta:
	model = VoiceClip
	exclude = ('listens',)

    def clean(self):
	clip = self.cleaned_data.get('voice_clip', False)

	if clip:
	    if clip.content_type != 'audio/mp3':
		raise forms.ValidationError("Please upload an mp3 audio file")
	    if clip.name.split(".")[-1] != 'mp3':
		raise ValidationError("File does not have .mp3 extension")

	return self.cleaned_data
