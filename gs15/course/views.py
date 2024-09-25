from django.shortcuts import render
from datetime import datetime
# Create your views here.
def learn_django(request):
  #  return render(request,'course/course1.html',{'nm':"Django"})
  student={'names':['Rahul','Sonam','Raj','Anu']}
  return render(request,'course/course1.html',student)