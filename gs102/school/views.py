from django.shortcuts import render
from .models import Student,Teacher,Contractor

# Create your views here.

def home(request):
    stu_data=Student.objects.all()
    teach_data=Teacher.objects.all()
    cont_data=Contractor.objects.all()

    return render(request,'school/home.htm',{'stu':stu_data,'tea':teach_data,'con':cont_data})