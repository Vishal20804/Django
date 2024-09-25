from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1'}))
    # email=forms.EmailField()
    # mobile=forms.IntegerField()
    # key=forms.CharField(widget=forms.HiddenInput())
    
