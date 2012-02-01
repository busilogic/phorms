# phorm views
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from drchrono.phorms.models import Survey, SurveyItem, Choice

# Show list of forms created so far no matter who created them
def list_form(request):
    all_surveys = Survey.objects.all()
    c = {'surveys': all_surveys}
    return render_to_response("phorms/list.html",
                              c, context_instance=RequestContext(request))

# Preview page
def preview(request, survey_id):
    if request.POST:
        print "Posting something from detail page %s" % survey_id
        if 'send_email' in request.POST:
            complete_url = request.build_absolute_uri()
            
            base_url = complete_url[0:complete_url.find(request.get_full_path())]
            print "Base url: {0}".format(base_url)
            url = "%s/phorms/survey/%s/" % (base_url, survey_id)
            #url = "http://localhost:8000/phorms/survey/%s/" % survey_id
            email_address = request.POST.get('email_address')
            print "Send email to {0} with url {1}".format(email_address, url)
            send_email_helper(url, email_address)
            
        return HttpResponseRedirect("/admin/phorms/survey/")

    if request.GET:
        print "Get request -- don't show actions or preview header"
    # Get Survey
    s = get_object_or_404(Survey, pk=survey_id)
    si = SurveyItem.objects.filter(survey = survey_id)
    
    return render_to_response('phorms/preview.html',
                              {'survey': s , 'surveyitem':si},
                              context_instance=RequestContext(request))


    
# Show survey details
def detail(request, survey_id):
    # Get Survey
    s = get_object_or_404(Survey, pk=survey_id)
    si_lst = SurveyItem.objects.filter(survey = survey_id)
    if request.POST:
        print "Posting something from detail page %s" % survey_id
        if 'save_survey' in request.POST:
            print "Need to save that survey"
            print request.POST
            # Get si_<si.id> variable from dict
            for si in si_lst:
                form_name = "si_%d" % si.id
                print request.POST.get(form_name)
                if si.is_boolean:
                    if 'True' == request.POST.get(form_name): 
                        c = Choice( surveyItem=si,
                                option='True')
                    else:
                        c = Choice( surveyItem=si, option = 'False')

                else:
                    c = Choice( surveyItem=si, choice= request.POST.get(form_name))
                    c.save()
    return render_to_response("phorms/detail.html",{'survey':s,'surveyitem':si_lst },context_instance=RequestContext(request))


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
