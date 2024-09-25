from django.shortcuts import render
from datetime import datetime
# Create your views here.
def learn_django(request):
  data={
    'stu1':{'name':'vishal','roll':130},
    'stu2':{'name':'Mansi','roll':201},
    'stu3':{'name':'Pratik','roll':95},
    'stu4':{'name':'Manali','roll':907},
    'stu5':{'name':'Pallavi','roll':909},

  }

  return render(request,'course/course1.html',{'data':data})