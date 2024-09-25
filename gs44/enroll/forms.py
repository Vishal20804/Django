from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(widget=forms.PasswordInput,label="password(again)")

    def clean(self):
        clean_data=super().clean()
        valpwd=self.cleaned_data['password']
        valrpwd=self.cleaned_data['repassword']

        if valpwd !=valrpwd:
            raise forms.ValidationError("password should be matched")
        



    
    
