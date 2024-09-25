from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='Sonam'
    return render(request,'student/setsession.html')

def getsession(request):
    # nm=request.session['name']
    nm=request.session.get('name',default='guest')
    return render(request,'student/getsession.html',{'nm':nm})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'student/delsession.html')