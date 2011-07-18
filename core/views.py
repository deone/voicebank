from django.shortcuts import render_to_response, redirect, get_list_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404

from core.forms import VoiceClipForm
from core.models import VoiceClip

@login_required
def upload(request, template='core/index.html', form=VoiceClipForm):

    if request.method == "POST":
	form = form(request.POST, request.FILES)
	if form.is_valid():
	    form.save()
	    messages.success(request, "Audio clip uploaded")
	    return redirect('core.views.upload')
    else:
	form = form(auto_id='%s', initial={'user': request.user.id})

    try:
	voice_clips = get_list_or_404(VoiceClip, user=request.user)
    except Http404:
	voice_clips = None
    
    return render_to_response(template, {
	    'form': form,
	    'clips': voice_clips
	}, context_instance=RequestContext(request))
