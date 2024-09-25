from django.urls import path
from . import views
urlpatterns=[
        path('dj/',views.fee_django),
    path('py/',views.fee_python)
]