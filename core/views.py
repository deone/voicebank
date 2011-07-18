from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from core.forms import VoiceClipForm

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
    
    return render_to_response(template, {'form': form},
	    context_instance=RequestContext(request))
