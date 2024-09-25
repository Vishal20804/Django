from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    stu_data1=Student.objects.all()  #default
    #after changing model manger
    stu_data2=Student.stu.all()#custom
    return render(request,'school/home.html',{'s':stu_data1,'e':stu_data2})
