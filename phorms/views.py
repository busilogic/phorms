from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

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
    return render_to_response('phorms/create_survey.html')

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

    return render_to_response('phorms/auth.html', {'state':state, 'username': username})