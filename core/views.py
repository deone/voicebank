from django.shortcuts import render_to_response, redirect, get_list_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.conf import settings

from core.forms import * 
from core.models import VoiceClip, Category
from events.models import Event

class VoiceClipListView(ListView):

    queryset = VoiceClip.objects.active()
    paginate_by = settings.VOICECLIP_LIST_PAGINATE_BY

    def get_context_data(self, **kwargs):
	context = super(VoiceClipListView, self).get_context_data(**kwargs)
	context['events'] = Event.objects.later_than_now()
	return context


class CategoryDetailView(DetailView):

    model = Category

    def get_context_data(self, **kwargs):
	context = super(CategoryDetailView, self).get_context_data(**kwargs)
	context['events'] = Event.objects.later_than_now()
	return context

@login_required
def voiceclips(request, template='core/voiceclips.html', form=VoiceClipForm):
    if request.method == "POST":
	form = form(request.POST, request.FILES)
	if form.is_valid():
	    form.save()
	    messages.success(request, "Audio clip uploaded successfully.")
    else:
	form = form(initial={'user': request.user.id})

    try:
	voice_clips = get_list_or_404(VoiceClip, user=request.user,
		is_active=True)
    except Http404:
	voice_clips = None
    
    return render_to_response(template, {
	    'form': form,
	    'clips': voice_clips,
	    'events': Event.objects.later_than_now()
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
	    'form': form,
	    'events': Event.objects.later_than_now()
	}, context_instance=RequestContext(request))
