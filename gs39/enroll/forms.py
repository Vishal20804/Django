from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField(strip= True,min_length=3,max_length=130)
    agree=forms.BooleanField(label_suffix='',label='I agree')
    a=forms.URLField()

    
