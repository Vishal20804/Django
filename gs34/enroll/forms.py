from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField(label='Your Name',label_suffix='',initial='vishal' ,disabled=True,help_text='help text')
    # email=forms.EmailField()
    # mobile=forms.IntegerField()
    # key=forms.CharField(widget=forms.HiddenInput())
    
