from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    # stu_data=Student.objects.all()
    #after changing model manger
    stu_data=Student.stu.all()
    return render(request,'school/home.html',{'s':stu_data})
