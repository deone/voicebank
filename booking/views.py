from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from booking.forms import BookingForm
from events.models import Event

@login_required
def booking(request, template='booking/index.html', form=BookingForm):
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
	'events': Event.objects.later_than_now()
	}, context_instance=RequestContext(request))
