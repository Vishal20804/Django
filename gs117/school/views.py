from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

class GeekyShowsRedirectView(RedirectView):
    url='https://geekyshows.com'