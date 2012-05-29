from django.shortcuts import render_to_response, get_list_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

from vbank.forms import * 
from vbank.models import VoiceClip

@login_required
def voiceclips(request, template='vbank/voiceclips.html', form=VoiceClipForm):
    if request.method == "POST":
	form = form(request.POST, request.FILES)
	if form.is_valid():
	    form.save()
	    messages.success(request, "Audio clip uploaded successfully.")
    else:
	form = form(initial={'user': request.user.id})

    try:
	# Use model_utils here.
	voice_clips = get_list_or_404(VoiceClip, user=request.user,
		is_active=True)
    except Http404:
	voice_clips = None
    
    return render_to_response(template, {
	    'form': form,
	}, context_instance=RequestContext(request))
