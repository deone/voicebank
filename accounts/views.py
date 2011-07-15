from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login

from accounts.forms import UserJoinForm

def join(request, template='accounts/index.html', form=UserJoinForm):
    if request.method == "POST":
	form = form(request.POST)
	if form.is_valid():
	    form.save(request)

	    # Authenticate and log user in.
	    username = request.POST['username']
	    password = request.POST['password1']

	    user = authenticate(username=username, password=password)
	    if user is not None:
		if user.is_active:
		    login(request, user)
		else:
		    pass
	    
	    return redirect('core.views.upload')
    else:
	form = form()

    return render_to_response(template, {'form': form},
	    context_instance=RequestContext(request))
