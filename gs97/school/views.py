from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    # student_data=Student.objects.get(pk=1) 
    # student_data=Student.objects.get(name='Vishal')
    # student_data=Student.objects.first()
    # student_data=Student.objects.last()
    # student_data=Student.objects.latest('pass_date')
    # student_data=Student.objects.all()
    # print(student_data.exists())
    # student_data=Student.objects.create(name='kisan',roll=42,city='paris',marks=90,pass_date='2024-08-7')
    student_data,created=Student.objects.get_or_create(name='kisan',roll=42,city='paris',marks=90,pass_date='2024-08-7')
    print(created)

    print("student data:",student_data)
    return render(request,'school/home.html',{'student':student_data})