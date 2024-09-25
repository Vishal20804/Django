from django.shortcuts import render,HttpResponseRedirect
from .forms import Signup ,EditUserProfileForm,EditAdminUserProfileForm
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm ,SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash 
from django.contrib import messages
from django.contrib.auth.models import User , Group
# Create your views here.

def sign_up(request):
    if request.method=="POST":
        fm=Signup(request.POST)
        if fm.is_valid():
            messages.success(request,'created in successfully')
            user=fm.save()
            group=Group.objects.get(name='editor')
            user.groups.add(group)

            
    else:

        fm=Signup()


    return render(request,'enroll/signup.html',{'fm':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/dashboard/')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

    
# change the form i.e name , email etc
def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request,'enroll/dashboard.html',{'name':request.user.username})
    else:
        return HttpResponseRedirect('/login/')
    
