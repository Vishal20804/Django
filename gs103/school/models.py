from django.db import models

# Create your models here.
class ExamCentre(models.Model):
    cname=models.CharField(max_length=100)
    city=models.CharField(max_length=100)


class Student(ExamCentre):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
