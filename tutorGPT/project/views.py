from django.shortcuts import render
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from .models import *
from django.core import serializers
from django.middleware.csrf import get_token
from .forms import *
import random
import json


# Create your views here.

def example_view(request):
    csrf_token = get_token(request)
    return render(request, "project/example.html", {"csrfmiddlewaretoken": csrf_token})

# def upload_notes(request):
#     form = UploadNotes(request.POST or None, request.FILES or None)
#     if request.method == "POST":
#         print(form.errors)
#         if form.is_valid():
#             notes = form.cleaned_data["notes"]
#             text = notes.read().decode('ascii')
#             # print(text)
#             Bundle.objects.create(notes=text)
#             # ask chatgpt to generate questions here
#     return render(request, "project/example.html", {'form': form})
#             # Bundle.objects.create(notes = text)
    

def get_questions(request):
    print("jksdhfksdjhfksjf")
    form = UploadNotes(request.POST or None, request.FILES or None)
    data = []
    if request.method == "POST":
        print("data", form, form.is_valid())
        if form.is_valid():
            text = form.cleaned_data["notes"]
            # print(text)
            bundle = Bundle.objects.create(notes=text)
            # ask chatgpt to generate questions here
            # return render(request, "project/example.html", {'form': form})
            # bundle = get_object_or_404(Bundle, pk=pk)
            question1 = MultipleChoiceQuestion.objects.create(bundle=bundle, question="""this is a question <img src="http://www.nyan.cat/images/Collection11-20.gif"></img>!!!!!""", option1="""<img src="https://www.nyan.cat/cats/original.gif"></img>""", option2="""<img src="https://www.nyan.cat/images/thumbs/jacksnyan.gif"></img>""", option3="""<img src="https://www.nyan.cat/images/thumbs/pirate.gif"></img>""", option4="""<img src="https://www.nyan.cat/images/thumbs/pikanyan.gif"></img>""", answer=2)
            questions = MultipleChoiceQuestion.objects.filter(bundle=bundle)
            for x in range(len(questions)):
                data.append({"id": str(questions[x].id), "text":questions[x].question, "choices":[questions[x].option1, questions[x].option2, questions[x].option3, questions[x].option4]})
            # data = serializers.serialize('json', questions)
            # print(data)
            # print(json.dumps(data))
    return JsonResponse({"response": data}, status=200)

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