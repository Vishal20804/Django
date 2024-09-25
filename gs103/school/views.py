from django.shortcuts import redirect,render
from .models import ExamCentre,Student

def home(request):
    e=ExamCentre.objects.get(id=3)
    s=Student.objects.get(id=3)
    print(e)
    print()
    print(s)

    return render(request,'school/home.htm',{'e':e,'s':s})