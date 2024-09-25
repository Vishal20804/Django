from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    #by default objects is model manager i.e  stu_data=Student.objects.all()
    #to change
    stu=models.Manager()
    