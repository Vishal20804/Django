from django.shortcuts import render
from .models import Student
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django import forms
# Create your views here.

class StudentCreateView(CreateView):
    model=Student
    fields=['name','email','password']
    success_url='/thanks/'
#to apply css in the form
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget =forms.TextInput(attrs={'class':'myclass'})
        form.fields['email'].widget =forms.TextInput(attrs={'class':'myemail'})
        form.fields['password'].widget =forms.PasswordInput(attrs={'class':'mypass'})
        return form

class ThanksTemplateView(TemplateView):
    template_name='school/thanks.html'