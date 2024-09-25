from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fees_django(request):
    return render(request,'fees/fees1.html')
    return HttpResponse("<h1>django 101 </h1>")
def fees_python(request):
    return render(request,'fees/fees2.html')
    return HttpResponse("<h1>Python 102 </h1>")