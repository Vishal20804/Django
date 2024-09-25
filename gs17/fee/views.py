from django.shortcuts import render

# Create your views here.

def fee_django(request):
    return render (request,'fee/info.html')