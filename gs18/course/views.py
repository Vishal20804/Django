from django.shortcuts import render

# Create your views here.

def learn_django(request):
    details={'name':'django framework',
             'time':'3 month'}
    return render(request,'course/course.html',details)