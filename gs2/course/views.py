from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("THis is home")

def learn_django(request):
    return HttpResponse("hello Django")

def learn_python(request):
    return HttpResponse("hello Python")

def learn_var(request):
    return HttpResponse("hello Var")

def learn_math(request):
    return HttpResponse("hello Math")