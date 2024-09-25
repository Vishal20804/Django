from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course_django(request):
    coursename={'cname':'Data structure is imp subject in CSE'}
    return render(request,'course/course1.html' ,context=coursename)
    
    return HttpResponse("<h1>django </h1>")
def course_python(request):
    cname ="C Programming language"
    duration ="6 month training"
    seats = 100
    details={'nm':cname,'du':duration,'st':seats} 
    return render(request,'course/course2.html', context=details)
    return HttpResponse("<h1>Python </h1>")