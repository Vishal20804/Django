from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=100)
    stuemail=models.EmailField(max_length=100)
    stupass=models.CharField(max_length=100)


    #3rd step
    def __str__(self):
        return self.stuname