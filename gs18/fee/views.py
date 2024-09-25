from django.shortcuts import render

# Create your views here.
def fee_django(request):
    details={'fee':'1000 rupee'}
    return render(request,'fee/fee.html',details)