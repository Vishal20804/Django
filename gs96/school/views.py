from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    # student_data=Student.objects.all()
    # student_data=Student.objects.filter(marks=90)
    # student_data=Student.objects.exclude(marks=90)
    # student_data=Student.objects.order_by('marks')#for ascending order
    # student_data=Student.objects.order_by('-marks')#for descending order
    # student_data=Student.objects.order_by('id').reverse()
    # student_data=Student.objects.values()
    # student_data=Student.objects.values('name','roll')# it  return in the form dictionary rather than objects
    # student_data=Student.objects.values_list(named=True)#it return in the form of tuple
    # student_data=Student.objects.dates('pass_date','month')
    student_data=Student.objects.dates('pass_date','year')   

    print("sql query:",student_data.query)
    print("student data:",student_data)
    return render(request,'school/home.html',{'students':student_data})