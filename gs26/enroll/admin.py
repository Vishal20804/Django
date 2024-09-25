from django.contrib import admin
#1st step
from .models import Student

# Register your models here.
#2nd step
admin.site.register(Student)