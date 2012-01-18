from django.db import models
from django import forms

#Forms
class SurveyForm(forms.Form):

    question = forms.CharField(max_length=100)
    answer = forms.CharField(max_length=200)    
    #cc_myself = forms.BooleanField(required=False)
    



# Models
class Survey(models.Model):
    title = models.CharField(max_length=100)
    def __unicode(self):
        return self.question


class SurveyItem(models.Model):
    survey = models.ForeignKey(Survey)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date activated')


class Choice(models.Model):
    survey = models.ForeignKey(SurveyItem)
    choice = models.CharField(max_length=200)
    option = models.BooleanField()
    