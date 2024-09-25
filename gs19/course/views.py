from django.shortcuts import render

# Create your views here.
def django_course(request):
    return render(request,'course/course.html')
