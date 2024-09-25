from django.shortcuts import render
from .forms import StudentRegistration


# Create your views here.

def showformdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():  # Validate the form
            print(fm.cleaned_data)  # Now you can access cleaned_data
            name=(fm.cleaned_data['name'])
            email=(fm.cleaned_data['email'])
            mobile=(fm.cleaned_data['mobile'])
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
        print('Get request')

    return render(request,'enroll/userregistration.html',{'form':fm})