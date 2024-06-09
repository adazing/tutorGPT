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


def example_view(request):
    csrf_token = get_token(request)
    return render(request, "project/example.html", {"csrfmiddlewaretoken": csrf_token})

def get_questions(request):
    print("jksdhfksdjhfksjf")
    form = UploadNotes(request.POST or None, request.FILES or None)
    data = []
    if request.method == "POST":
        print("data", form, form.is_valid())
        if form.is_valid():
            text = form.cleaned_data["notes"]
            bundle = Bundle.objects.create(notes=text)
            questions_text = get_questions_from_notes(text).split("\n")
            while True:
                try:
                    questions_text = get_questions_from_notes(text).split("\n")
                    for q in questions_text:
                        _, question, _, option1, _, option2, _, option3, _, option4, _, answer = q.split("|")
                        question_obj = MultipleChoiceQuestion.objects.create(bundle=bundle, question=question, option1=option1, option2=option2, option3=option3, option4=option4, answer=int(answer))
                        data.append({"id": str(question_obj.id), "text":question_obj.question, "choices":[question_obj.option1, question_obj.option2, question_obj.option3, question_obj.option4]})
                    break
                except:
                    continue
    return JsonResponse({"response": data}, status=200)

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
