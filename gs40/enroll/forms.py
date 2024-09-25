from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField(strip= True,min_length=3,max_length=130)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)

    # validating
    def clean_name(self):
        valname=self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError('enter at least 4 char')
        return valname



    
    
