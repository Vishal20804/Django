from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
from .models import User


def showformdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():  # Validate the form
            print(fm.cleaned_data['name'])  # Now you can access cleaned_data
            nm=fm.cleaned_data['name']
            print(fm.cleaned_data['email']) 
            em=fm.cleaned_data['email']
            print(fm.cleaned_data['password'])
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            #for delete
            #reg=User(id=1)
            #reg.delete()
    else:
        fm=StudentRegistration()
        print('Get request')

    return render(request,'enroll/userregistration.html',{'form':fm})