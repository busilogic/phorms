from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login

# Show list of forms created so far no matter who created them
def list_form(request):
    c = {}
    return render_to_response("phorms/list.html", context_instance=RequestContext(request))
    
def add_question(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SurveyForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
        # Process the data in form.cleaned_data
        # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = SurveyForm() # An unbound form

    return render_to_response('contact.html', {'form': form,})
    

    
def create_form(request):
    return render_to_response('phorms/create_survey.html', context_instance=RequestContext(request))

def login_user(request):
    state = "Please log in ..."
    username = ''
    password = ''

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Login successful!"

            else:
                state = "login inactive, please try logging in again"

        else:
            state = "Incorrect username and/or password!"

    return render_to_response('phorms/auth.html', {'state':state, 'username': username},
                              context_instance=RequestContext(request))