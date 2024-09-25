from django.db import models
from .manager import CustomManager
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()

    objects=models.Manager()
    stu=CustomManager()
    