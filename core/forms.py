from django import forms

from core.models import VoiceClip

class VoiceClipForm(forms.ModelForm):

    class Meta:
	model = VoiceClip

    def clean(self):
	clip = self.cleaned_data.get('voice_clip', False)

	if clip:
	    if clip.content_type not in ['audio/mp3', 'audio/wav']:
		raise forms.ValidationError("File not valid audio clip")
	    if clip.name.split(".")[-1] not in ['mp3', 'wav']:
		raise ValidationError("File does not have proper extension")

	return self.cleaned_data
