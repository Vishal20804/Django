from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course_django(request):
    return render(request,'course/course1.html')
    
    return HttpResponse("<h1>django </h1>")
def course_python(request):
    return render(request,'course/course2.html')
    return HttpResponse("<h1>Python </h1>")