from django.shortcuts import render_to_response, redirect, get_list_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404

from core.forms import * 
from core.models import VoiceClip

@login_required
def index(request, template='core/index.html'):
    return render_to_response(template, {}, context_instance=RequestContext(request))

@login_required
def dashboard(request, template='core/dashboard.html'):
    return render_to_response(template, {}, context_instance=RequestContext(request))

@login_required
def voiceclips(request, template='core/voiceclips.html', form=VoiceClipForm):
    if request.method == "POST":
	form = form(request.POST, request.FILES)
	if form.is_valid():
	    form.save(request)
	    messages.success(request, "Audio clip uploaded")
	    return redirect('core.views.voiceclips')
    else:
	form = form(initial={'user': request.user.id})

    try:
	voice_clips = get_list_or_404(VoiceClip, user=request.user,
		is_active=True)
    except Http404:
	voice_clips = None
    
    return render_to_response(template, {
	    'form': form,
	    'clips': voice_clips
	}, context_instance=RequestContext(request))

def booking(request, template='booking.html', form=BookingForm):
    if request.method == "POST":
	form = form(request.POST)
	if form.is_valid():
	    form.save()
	    messages.success(request, """Your booking was submitted
	    successfully.""")
    else:
	form = form(initial={'user': request.user.id})

    return render_to_response(template, {
	'form': form,
	}, context_instance=RequestContext(request))

def contact(request, template='contact.html', form=ContactForm):
    if request.method == "POST":
	form = form(request.POST)
	if form.is_valid():
	    form.save()
	    messages.success(request, """Your enquiry was submitted successfully.
	    We would reply as soon as possible.""")
    else:
	form = form()
	    
    return render_to_response(template, {
	'form': form
	}, context_instance=RequestContext(request))
