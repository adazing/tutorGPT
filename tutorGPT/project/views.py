from django.shortcuts import render
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from .models import *
from django.core import serializers
from .forms import *
import random
import json


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
            # print(text)
            Bundle.objects.create(notes=text)
            # ask chatgpt to generate questions here
    return render(request, "project/example.html", {'form': form})
            # Bundle.objects.create(notes = text)
    

def get_questions(request, pk):
    bundle = get_object_or_404(Bundle, pk=pk)
    questions = MultipleChoiceQuestion.objects.filter(bundle=bundle)
    data = dict()
    for x in range(len(questions)):
        data[str(questions[x].id)] = {"text":questions[x].question, "choices":[questions[x].option1, questions[x].option2, questions[x].option3, questions[x].option4]}
    # data = serializers.serialize('json', questions)
    # print(data)
    # print(json.dumps(data))
    return JsonResponse(data, safe=True)

# def check_answer(request, pk):

def check_answer(request):
    form = CheckForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            question = MultipleChoiceQuestion.objects.get(form.cleaned_data["q"])
            if question.answer == form.cleaned_data["a"]:
                return JsonResponse({"response":True}, safe=True)
            else:
                return JsonResponse({"response":False}, safe=True)
    JsonResponse({"response":404}, safe=True)