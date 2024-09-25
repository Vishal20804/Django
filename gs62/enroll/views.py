from django.shortcuts import render
from .forms import Signup

# Create your views here.

def sign_up(request):
    if request.method=="POST":
        fm=Signup(request.POST)
        if fm.is_valid():
            fm.save()
    else:

        fm=Signup()
    return render(request,'enroll/signup.html',{'fm':fm})