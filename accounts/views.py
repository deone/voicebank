from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from accounts.forms import UserJoinForm, UserProfileForm, SpanErrorList

def index(request, template='accounts/index.html', forms=[UserJoinForm, AuthenticationForm]):

    join_form = forms[0]()
    login_form = forms[1]()

    return render_to_response(template, {
	    'login_form': login_form,
	    'join_form': join_form
	}, context_instance=RequestContext(request))

@login_required
def profile(request, slug, template='accounts/profile.html'):
    return render_to_response(template, {
	}, context_instance=RequestContext(request))

@login_required
def profile_edit(request, template='accounts/profile_edit.html', form=UserProfileForm):
    if request.method == "POST":
	form = form(request.POST, request.FILES, error_class=SpanErrorList)
	if form.is_valid():
	    form.save()
    else:
	form = form(initial={
	    'user': request.user.id, 
	    'first_name': request.user.first_name,
	    'last_name': request.user.last_name,
	    'birthday': request.user.get_profile().birthday,
	    })

    return render_to_response(template, {
	    'form': form
	}, context_instance=RequestContext(request))

def join(request, template='accounts/join.html', form=UserJoinForm):
    if request.method == "POST":
	form = form(request.POST)
	if form.is_valid():
	    form.save()

	    # Authenticate and log user in.
	    email = request.POST['email']
	    password = request.POST['password']

	    user = auth.authenticate(username=email, password=password)

	    if user is not None:
		if user.is_active:
		    auth.login(request, user)
		else:
		    # Do something if we ever need to.
		    pass
	    
	    return redirect('core.views.index')
    else:
	form = form()

    return render_to_response(template, {'join_form': form},
	    context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return redirect('accounts.views.index')
