from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='Sonam'
    return render(request,'student/setsession.html')

def getsession(request):
    # nm=request.session['name']
    nm=request.session.get('name',default='guest')
    request.session.set_expiry(0)
    # keys=request.session.keys()
    # items=request.session.items()
    return render(request,'student/getsession.html',{'nm':nm})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'student/delsession.html')