from django.shortcuts import render
from datetime import datetime
# Create your views here.
def learn_django(request):
    
    cname="Django"
    duration="4 Months"
    text="This is the paragraph for django, Django is used to develope web dev."
    d=datetime.now()
    detail={'name':cname,'du':duration,'text':text,'dt':d}
    
    return render(request,'course/course1.html',context=detail)