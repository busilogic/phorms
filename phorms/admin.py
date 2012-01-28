#admin.py
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.core.mail import EmailMessage
from drchrono.phorms.models import Survey, SurveyItem

# Before emailing form, take user to preview page
# Construct rest url /phorms/id/view and email that link
# to specified user using gmail as SMTP
def email_form(modeladmin, request, queryset):
    print 'Inside send preview email'
    email_form.short_description = 'Email phorm'
    email_form.allow_tags = True

    # Get Email address first
    #email_address = request.POST['email_address']
    for obj in queryset:
        print 'Id of %s is %d' % (obj, obj.id)
        url = "http://localhost:8000/phorms/survey/%d/" % obj.id
        return HttpResponseRedirect("/phorms/survey/%d/" % obj.id)
        #send_email_helper(url, email_address)


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
    fieldsets = [
        ('Survey Title', {'fields': ['title']}),
        ('describe', {'fields': ['description']}),
    ]

    inlines = [SurveyItemInline]


# Register site with admin
admin.site.register(Survey, SurveyAdmin)

admin.site.add_action(email_form, 'Email form')
