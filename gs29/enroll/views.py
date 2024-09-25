from django.shortcuts import render
from .forms import StudentRegistration


# Create your views here.

def showformdata(request):
    fm=StudentRegistration(auto_id=True, label_suffix='',initial={'name':'vishal'})
    fm.order_fields(field_order=['email','name'])
    return render(request,'enroll/userregistration.html',{'form':fm})