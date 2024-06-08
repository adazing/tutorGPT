from django.db import models

# Create your models here.

class Bundle(models.Model):
    notes = models.TextField(max_length=15000)
    key = models.CharField(max_length=8, unique=True)

class MultipleChoiceQuestion(models.Model):
    bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    question = models.TextField(max_length=1000)
    option1 = models.TextField(max_length=1000)
    option2 = models.TextField(max_length=1000)
    option3 = models.TextField(max_length=1000)
    option4 = models.TextField(max_length=1000)
    answer = models.CharField(max_length=1, choices = (("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")), default="A")
    # index = models.IntegerField()

