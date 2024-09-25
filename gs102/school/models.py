from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract=True

class Student(CommonInfo):
    fee=models.IntegerField()
    date=None

class Teacher(CommonInfo):

    date=models.DateField()
    salary=models.IntegerField()

class Contractor(CommonInfo):

    date=models.DateTimeField()
    payment=models.IntegerField()

