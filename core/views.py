from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from core.forms import VoiceClipForm

@login_required
def upload(request, template='core/index.html', form=VoiceClipForm):
    """ """

    if request.method == "POST":
	form = form(request.POST, request.FILES)
	if form.is_valid():
	    form.save()
	    redirect('core.views.index')
    else:
	form = form()
    
    return render_to_response(template, {'form': form},
	    context_instance=RequestContext(request))
