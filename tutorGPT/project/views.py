from django.shortcuts import render
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from .models import *
from django.core import serializers
from .forms import *
import random
import string

def generate_unique_id():
    length = 8
    while True:
        unique_id = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789", k=length))
        if not Bundle.objects.filter(key=unique_id).exists():
            return unique_id

# Create your views here.

def example_view(request):
    return render(request, "project/example.html")

def upload_notes(request):
    form = UploadNotes(request.POST or None, request.FILES or None)
    if request.method == "POST":
        print(form.errors)
        if form.is_valid():
            notes = form.cleaned_data["notes"]
            text = notes.read().decode('ascii')
            print(text)
            Bundle.objects.create(notes=text, key=generate_unique_id())
    return render(request, "project/example.html", {'form': form})
            # Bundle.objects.create(notes = text)
    

def get_questions(request, pk):
    bundle = get_object_or_404(Bundle, pk=pk)
    questions = MultipleChoiceQuestion.objects.filter(bundle=bundle)
    data = serializers.serialize('json', questions)
    return JsonResponse(data)

# def check_answer(request, pk):
