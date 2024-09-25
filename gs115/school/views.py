from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContarctForm
# Create your views here.

class Myview(View):
    name='vk'
    def get(self,request):
        return render(request,'school/home.html')

class ContractClassView(View):
    def get(self,request):
        form=ContarctForm()
        return render(request,'school/contact.html',{'form':form})
    
    def post(self,request):
        form=ContarctForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("thank you!!!")