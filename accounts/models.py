from django.contrib.auth.models import AbstractUser
from django.db import models
import csv
from django.core.management.base import BaseCommand



class CustomUser(AbstractUser):
    

    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True,default="2000-01-01")
    username = models.EmailField(unique=True) 

    # Add any additional fields as needed

    def __str__(self):
        return self.email

class QuizResult(models.Model):
    username = models.EmailField(unique=True)
    job_role = models.CharField(max_length=100, default='Data Annotation Specialist')
    years_of_experience = models.PositiveIntegerField(default=0)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.username
    
class QuizQuestion(models.Model):
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    marks = models.IntegerField()
    correct = models.BooleanField(default=False)


class QuizSession(models.Model):
    current_question = models.ForeignKey(QuizQuestion, on_delete=models.SET_NULL, null=True)