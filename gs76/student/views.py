from django.shortcuts import render,HttpResponse

# Create your views here.
def settestcookie(request):
    request.session['name']='sonam'

    request.session.set_test_cookie()
    return render(request,'student/setcookie.html')


def checktestcookie(request):
    name =request.session['name']

    return render(request,'student/testcookie.html',{'name':name})


def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request,'student/delcookie.html')



