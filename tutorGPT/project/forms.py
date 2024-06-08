from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *
import io
import csv

class UploadNotes(forms.Form):
    notes = forms.FileField(required=True)
