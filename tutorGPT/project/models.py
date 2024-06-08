from django.db import models

# Create your models here.

class Group(models.Model):
    notes = models.TextField()
    # key = models.CharField(max_length=8, primary_key=True)

class Question(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

