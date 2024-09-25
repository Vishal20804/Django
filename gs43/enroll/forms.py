from django import forms
from django.core import validators

def start_with_r(value):
    if value[0]!='s':
        raise forms.ValidationError('Name should start with s')

class StudentRegistration(forms.Form):
    name=forms.CharField(validators=[start_with_r])
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)




    
    
