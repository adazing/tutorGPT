from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import *
from django.core import serializers
from django.middleware.csrf import get_token
from .forms import *
import random
import json
from .gpt import get_questions_from_notes

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
            # question1 = MultipleChoiceQuestion.objects.create(bundle=bundle, question="""this is a question <img src="http://www.nyan.cat/images/Collection11-20.gif"></img>!!!!!""", option1="""<img src="https://www.nyan.cat/cats/original.gif"></img>""", option2="""<img src="https://www.nyan.cat/images/thumbs/jacksnyan.gif"></img>""", option3="""<img src="https://www.nyan.cat/images/thumbs/pirate.gif"></img>""", option4="""hi""", answer=2)
            # question2 = MultipleChoiceQuestion.objects.create(bundle=bundle, question="""this is a second question !!!!!""", option1="""123123123123""", option2="""no""", option3="""asfvasdf""", option4="""ssssss""", answer=3)
            questions_text = get_questions_from_notes(text).split("\n")
            print(questions_text)
            for q in questions_text:
                _, question, _, option1, _, option2, _, option3, _, option4, _, answer = q.split("|")
                question_obj = MultipleChoiceQuestion.objects.create(bundle=bundle, question=question, option1=option1, option2=option2, option3=option3, option4=option4, answer=int(answer))
                data.append({"id": str(question_obj.id), "text":question_obj.question, "choices":[question_obj.option1, question_obj.option2, question_obj.option3, question_obj.option4]})
            # data = serializers.serialize('json', questions)
            # print(data)
            # print(json.dumps(data))
    return JsonResponse({"response": data}, status=200)

# def check_answer(request, pk):

def check_answer(request):
    form = CheckForm(request.POST or None)
    if request.method == "POST":
        print("check_answer_recieves:", form)
        if form.is_valid():
            question = MultipleChoiceQuestion.objects.get(id=form.cleaned_data["q"])
            print(question.answer, form.cleaned_data["a"])
            if question.answer == form.cleaned_data["a"]:
                return JsonResponse({"response":True}, safe=True)
            else:
                return JsonResponse({"response":False}, safe=True)
    return JsonResponse({"response":404}, safe=True)