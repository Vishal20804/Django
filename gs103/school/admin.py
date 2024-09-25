from django.contrib import admin
from .models import ExamCentre,Student

@admin.register(ExamCentre)
class AdminExaam(admin.ModelAdmin):
    list_display=['id','cname','city']

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display=['id','cname','city','name','roll']