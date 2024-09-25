from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.

class ContactFormView(FormView):
    template_name='school/contact.html'
    form_class=ContactForm
    success_url='/thankyou/'
    def form_valid(self,form):
        print(form)
        print(form.cleaned_data['name'])
        return super().form_valid(form)
class ThanksTemplateView(TemplateView):
    template_name='school/thankyou.html'