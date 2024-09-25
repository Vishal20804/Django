from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView


# Create your views here.
class StudentListView(ListView):
    model=Student

    # template_name_suffix='_get'# it will find student_get.html   _post   _anyname
    ordering=['name']

    template_name='school/student.html'  #fully customizable it will not throw error weather write student.html or student_list.html
    context_object_name='student_list'  #the context object will change we can set any context object name (it is use in for loop iterable)


    def get_queryset(self):
        return Student.objects.filter(course='python')
