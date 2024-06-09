from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *
import io
import csv

class UploadNotes(forms.Form):
    notes = forms.CharField(required=True)
    
    # def clean_notes(self):
    #     file = self.cleaned_data["notes"]
    #     if not file.name.endswith('.txt'):
    #         raise forms.ValidationError("Only .txt files are allowed!")
    #     if file.content_type != 'text/plain':
    #         raise forms.ValidationError("The uploaded file is not a valid text file!")
    #     return file

class CheckForm(forms.Form):
    q = forms.IntegerField(required=True, widget=forms.HiddenInput())
    # a = forms.CharField(required=True, choices = (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")))
    def clean_q(self):
        question_id = self.cleaned_data['q']
        if MultipleChoiceQuestion.objects.filter(id=question_id).exists():
            return question_id
        else:
            raise forms.ValidationError("This is not a valid id")