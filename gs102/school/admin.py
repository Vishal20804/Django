from django.contrib import admin
from .models import Student,Contractor,Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age','fee']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','age','salary','date']


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display=['id','name','age','payment','date']