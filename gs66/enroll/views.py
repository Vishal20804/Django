from django.shortcuts import render,HttpResponseRedirect
from .forms import Signup ,EditUserProfileForm,EditAdminUserProfileForm
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm ,SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def sign_up(request):
    if request.method=="POST":
        fm=Signup(request.POST)
        if fm.is_valid():
            messages.success(request,'created in successfully')
            fm.save()

            
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
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/profile/')


# def userprofile(request):
#     if request.user.is_authenticated:
#         return render(request,'enroll/profile.html' ,{'name':request.user})
#     else:
#         return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# change password with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user ,data=request.POST)
            if fm.is_valid():
                fm.save()
                # if we do not use update_session_auth_hash(request,fm.user)  the session will expire after change password .Now session is maintained or update
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password change successfully')
                return HttpResponseRedirect('/profile')
        else:
            fm=PasswordChangeForm(user=request.user)
            return render(request,'enroll/changepass.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/login/')
    

# change password without old password
def user_change_pass1(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(user=request.user ,data=request.POST)
            if fm.is_valid():
                fm.save()
                # if we do not use update_session_auth_hash(request,fm.user)  the session will expire after change password .Now session is maintained or update
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password change successfully')
                return HttpResponseRedirect('/profile')
        else:
            fm=SetPasswordForm(user=request.user)
            return render(request,'enroll/changepass1.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/login/')
    
# change the form i.e name , email etc
def userprofile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser==True:
                fm=EditAdminUserProfileForm(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserProfileForm(request.POST,instance=request.user)
                users=None
            if fm.is_valid():
                messages.success(request,'Profile updated')
                fm.save()
        else:
            if request.user.is_superuser==True:
                fm=EditAdminUserProfileForm(instance=request.user)
                users=User.objects.all()
            else:
                fm=EditUserProfileForm(instance=request.user)
                users=None
        return render(request,'enroll/profile.html' ,{'name':request.user.username,'fm':fm, 'users':users})
    else:
        return HttpResponseRedirect('/login/')
    

def user_detail(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm= EditAdminUserProfileForm(instance=pi)

        return render(request,'enroll/userdetail.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/login/')