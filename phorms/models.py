from django.db import models
from django import forms
from django.forms import ModelForm

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

    def __unicode__(self):
        return "Survey item: %s choice: %s option: %s" %(self.surveyItem, self.choice, self.option)
        
