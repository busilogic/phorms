from phorms.models import Survey, SurveyItem
from django.contrib import admin


class SurveyItemInline(admin.StackedInline):
    model = SurveyItem
    extra = 3

class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Survey Title', {'fields': ['title']}),
        ('describe', {'fields': ['description']}),
    ]

    inlines = [SurveyItemInline]

admin.site.register(Survey, SurveyAdmin)

