from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class Myview(View):
    name='vk'
    def get(self,request):
        return HttpResponse('<h1>This is class based view</h1>')
    
class MyViewChild(Myview):
    def get(self,reques):
        return HttpResponse(self.name)