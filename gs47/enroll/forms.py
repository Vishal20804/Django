from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    name=forms.CharField(error_messages={'required':'enter your name'})
    email=forms.EmailField(error_messages={'required':'enter your name'})
    password=forms.CharField(widget=forms.PasswordInput)
    



    
    
