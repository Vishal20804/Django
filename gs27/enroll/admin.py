from django.contrib import admin
#1st step
from .models import Student

class StudentModelAdmin(admin.ModelAdmin):
    list_display=('id','stuid','stuname')
admin.site.register(Student,StudentModelAdmin)