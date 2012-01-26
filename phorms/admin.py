#admin.py
from phorms.models import Survey, SurveyItem
from django.contrib import admin
from django.core.mail import EmailMessage

# Construct rest url /phorms/id/view and email that link
# to specified user using gmail as SMTP
def email_the_client(modeladmin, request, queryset):
    print 'Inside send preview email'
    email_the_client.short_description = 'Send Email'
    email_the_client.allow_tags = True

    # Get Email address first
    email_address = request.POST['email_address']
    for obj in queryset:
        print 'Id of %s is %d' % (obj, obj.id)
        url = "http://localhost:8000/phorms/survey/%d/" % obj.id        
        send_email_helper(url, email_address)
    # Print id of email address
    #print 'request %s ' % request.POST['email_address']


# Take Survey URL and send email 
def send_email_helper(survey_url, email_address):
    email = EmailMessage('Form to print and bring', survey_url, to=[email_address])
    try:
        email.send()
    except:
        print "Error sending email message"

#Classes
class SurveyItemInline(admin.TabularInline):
    model = SurveyItem
    extra = 3

class SurveyAdmin(admin.ModelAdmin):
    actions = [email_the_client]

    fieldsets = [
        ('Survey Title', {'fields': ['title']}),
        ('describe', {'fields': ['description']}),
    ]

    inlines = [SurveyItemInline]


admin.site.register(Survey, SurveyAdmin)

