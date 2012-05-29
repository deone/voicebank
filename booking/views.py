from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from booking.forms import BookingForm

@login_required
def index(request, template='booking/index.html', form=BookingForm):
    if request.method == "POST":
	form = form(request.POST)
	if form.is_valid():
	    form.save()
	    messages.success(request, """Your booking was submitted
	    successfully.""")
	    return redirect('booking.views.index')
    else:
	form = form(initial={'user': request.user.id})

	return render_to_response(template, {
	    'form': form,
	}, context_instance=RequestContext(request))
