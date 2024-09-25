from django.shortcuts import render
from .models import Student

from django.views.generic.detail import DetailView


class StudentDetailView(DetailView):
    model =Student  # here context object name will be student(all char in small letter)
    template_name='school/student.html'  #here student.html template must be exist
    context_object_name='stu'  #now context obj name will not student it change in stu

