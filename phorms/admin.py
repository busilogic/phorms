#admin.py
from phorms.models import Survey, SurveyItem
from django.contrib import admin

# Construct rest url /phorms/id/view and email that link
# to specified user using gmail as SMTP
def email_the_client(modeladmin, request, queryset):
    print 'Inside send preview email'
    email_the_client.short_description = 'Send Email'
    email_the_client.allow_tags = True
    for obj in queryset:
        print 'Id of %s is %d' % (obj, obj.id)
    
    # Print id of email address
    print 'request %s ' % request.POST['email_address']

    
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

