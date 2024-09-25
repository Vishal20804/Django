from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name='school/home.html'
    

class HomeTemplateView1(TemplateView):
    template_name='school/home.html'


    def get_context_data(self, **kwargs):
        # context=super().get_context_data(**kwargs)
        # context['name']='Vishal sharma'
        # context['roll']=123
        context={'name':'vishal sharma','roll':123}

        return context
    