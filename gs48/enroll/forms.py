from django import forms
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        # labels={'name':'enter name'}
        #similor for validators here label will write labels everything with s suffix
    