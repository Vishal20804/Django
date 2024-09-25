from django.shortcuts import render
from .models import Student


# Create your views here.

def studentinfo(request):
    stu = Student.objects.all()
    #for getting one data we can used 
    #stu=Student.objects.get(pk=1)
    return render(request,'enroll/studetails.html',{'stu':stu})