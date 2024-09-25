from django.shortcuts import render
from datetime import datetime
# Create your views here.
def learn_django(request):
  #  return render(request,'course/course1.html',{'nm':"Django"})
   return render(request,'course/course1.html',{'nm':"Django",'st':5})