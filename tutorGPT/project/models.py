from django.db import models
import random

# Create your models here.

def generate_unique_id():
    length = 8
    while True:
        unique_id = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789", k=length))
        if not Bundle.objects.filter(id=unique_id).exists():
            return unique_id

class Bundle(models.Model):
    # id = models.CharField(max_length=8, primary_key=True, default=generate_unique_id, editable=False)
    notes = models.TextField(max_length=15000)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.id = generate_unique_id()
    #     super(Bundle, self).save(*args, **kwargs)

class MultipleChoiceQuestion(models.Model):
    bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    question = models.TextField(max_length=1000)
    option1 = models.TextField(max_length=1000)
    option2 = models.TextField(max_length=1000)
    option3 = models.TextField(max_length=1000)
    option4 = models.TextField(max_length=1000)
    answer = models.IntegerField(choices = ((1, 1), (2, 2), (3, 3), (4, 4)), default=1)
    # index = models.IntegerField()

