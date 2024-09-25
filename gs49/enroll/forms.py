from django import forms
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        labels={'name':'Enter name','email':'Enter Email'}
        widgets={'password':forms.PasswordInput,
                 'name':forms.TextInput}
    