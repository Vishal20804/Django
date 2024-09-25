from django.shortcuts import render
from .models import Student

from django.views.generic.detail import DetailView


class StudentDetailView(DetailView):
    model =Student  # here context object name will be student(all char in small letter)

