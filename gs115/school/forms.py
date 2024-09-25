from django import forms

class ContarctForm(forms.Form):
    name=forms.CharField(max_length=100)
