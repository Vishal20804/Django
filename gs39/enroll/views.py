from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect



def showformdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():  # Validate the form
            print(fm.cleaned_data['name'])  # Now you can access cleaned_data
            print(fm.cleaned_data['a']) 
    else:
        fm=StudentRegistration()
        print('Get request')

    return render(request,'enroll/userregistration.html',{'form':fm})