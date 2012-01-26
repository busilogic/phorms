from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from drchrono.phorms.models import Survey, SurveyForm

# Show list of forms created so far no matter who created them
def list_form(request):
    all_surveys = Survey.objects.all()
    c = {'surveys': all_surveys}
    return render_to_response("phorms/list.html",
                              c, context_instance=RequestContext(request))

# Show survey details
def detail(request, survey_id):
    return HttpResponse("You're looking at survey %s" % survey_id)

# Handle login
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

# Create a form
def create_form(request):
    if request.method == "POST":
        #Save the form
        return render_to_response("phorms/list.html", {}, context_instance=RequestContext(request))

    else:
        form = SurveyForm()
        
    return render_to_response('phorms/create_survey.html', {'form': form},
                              context_instance=RequestContext(request))
