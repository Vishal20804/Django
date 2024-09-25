from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response= render(request,'student/setcookie.html')
    response.set_cookie('name','sonali',max_age=120)
    return response

def getcookie(request):
    # name=request.COOKIES['name']
    #the below syntax is also  used but it will also take default value as optional value
    name=request.COOKIES.get('name','guest') 
    return render(request,'student/getcookie.html',{'nm':name})

def delcookie(request):
    response= render(request,'student/delcookie.html')
    response.delete_cookie('name')
    return response