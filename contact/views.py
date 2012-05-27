from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.contrib import messages

from events.models import Event
from contact.forms import ContactForm


def index(request, template='contact/index.html', form=ContactForm):
    if request.method == "POST":
	form = form(request.POST)
	if form.is_valid():
	    form.save()
	    messages.success(request, """Your enquiry was submitted successfully.
	    We would reply as soon as possible.""")
	    return redirect('contact.views.index')
    else:
	form = form()
	    
	return render_to_response(template, {
	    'form': form,
	    'events': Event.objects.later_than_now()
	}, context_instance=RequestContext(request))
