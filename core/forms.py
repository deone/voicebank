from django import forms

from core.models import VoiceClip

class VoiceClipForm(forms.ModelForm):

    class Meta:
	model = VoiceClip
