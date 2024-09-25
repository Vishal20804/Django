from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect

# Create your views here.
def thankyou(request):
    return render(request,'enroll/success.html')

def showformdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():  # Validate the form
            print(fm.cleaned_data)  # Now you can access cleaned_data
            name=(fm.cleaned_data['name'])
            email=(fm.cleaned_data['email'])
            mobile=(fm.cleaned_data['mobile'])

            fm={'name':name,
                'email':email,
                'mobile':mobile}
            return HttpResponseRedirect('/enroll/success/')
            #return render(request,'enroll/success.html',{'name':name})
    else:
        fm=StudentRegistration()
        print('Get request')

    return render(request,'enroll/userregistration.html',{'form':fm})