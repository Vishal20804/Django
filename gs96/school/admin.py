from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentdminRegister(admin.ModelAdmin):
    list_display=['id','name','roll','city','marks','pass_date']
