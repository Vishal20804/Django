from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print("i am view")
    return HttpResponse("<h1>This is view</h1>")
