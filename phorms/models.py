from django.contrib import admin
from django.db import models
from django import forms


def send_preview(modeladmin, request, queryset):
    print 'Inside send preview email'
    for obj in queryset:
        print(obj)

#Forms
class SurveyForm(forms.Form):
    title = forms.CharField(max_length=200)
    question = forms.CharField(max_length=200)

    def __unicode__(self):
        return self.title    

# Models
class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title


class SurveyItem(models.Model):
    survey = models.ForeignKey(Survey)
    question = models.CharField(max_length=200)
    is_boolean = models.BooleanField()

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    surveyItem = models.ForeignKey(SurveyItem)
    choice = models.CharField(max_length=200)
    option = models.BooleanField()
    
