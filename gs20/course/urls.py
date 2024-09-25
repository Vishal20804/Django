from django.urls import path

from . import views

urlpatterns=[
    path('learndj',views.django_course,name='course1')
]