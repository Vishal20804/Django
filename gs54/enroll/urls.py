from django.urls import path,register_converter
from . import views,convertors


register_converter(convertors.FourDigitYearConverter,'YYYY')
urlpatterns=[

    path('<YYYY:year>/',views.show_details,name='detail'),

]