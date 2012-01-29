# phorm views
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from drchrono.phorms.models import Survey, SurveyItem


# Show list of forms created so far no matter who created them
def list_form(request):
    all_surveys = Survey.objects.all()
    c = {'surveys': all_surveys}
    return render_to_response("phorms/list.html",
                              c, context_instance=RequestContext(request))

# Show survey details
def detail(request, survey_id):
    if request.POST:
        print "Posting something from detail page %s" % survey_id
        if 'send_email' in request.POST:
            print "Send email button clicked"
            url = "http://localhost:8000/phorms/survey/%s/" % survey_id
            email_address = request.POST.get('email_address')
            print "Send email to {0} with url {1}".format(email_address, url)
            send_email_helper(url, email_address)

        return HttpResponseRedirect("/admin/phorms/survey/")

    # Get Survey
    s = get_object_or_404(Survey, pk=survey_id)
    si = SurveyItem.objects.filter(survey = survey_id)
    
    return render_to_response('phorms/detail.html',
                              {'survey': s , 'surveyitem':si},
                              context_instance=RequestContext(request))


# Take Survey URL and send email 
def send_email_helper(survey_url, email_address):
    email = EmailMessage('Form to print and bring', survey_url,
                         to=[email_address])
    try:
        email.send()
    except:
        print "Error sending email message"
        

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
