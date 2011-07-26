from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from accounts.forms import UserJoinForm

def index(request, template='accounts/index.html', forms=[UserJoinForm, AuthenticationForm]):

    join_form = forms[0]()
    login_form = forms[1]()

    return render_to_response(template, {
	    'login_form': login_form,
	    'join_form': join_form
	}, context_instance=RequestContext(request))

def join(request, template='accounts/join.html', form=UserJoinForm):
    if request.method == "POST":
	form = form(request.POST)
	if form.is_valid():
	    form.save()

	    # Authenticate and log user in.
	    username = request.POST['username']
	    password = request.POST['password']

	    user = authenticate(username=username, password=password)
	    if user is not None:
		if user.is_active:
		    login(request, user)
		else:
		    pass
	    
	    return redirect('core.views.welcome')
    else:
	form = form()

    return render_to_response(template, {'join_form': form},
	    context_instance=RequestContext(request))

def logout(request):
    request.session.flush()
    return redirect('accounts.views.index')
