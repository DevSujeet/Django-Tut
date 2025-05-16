from django.urls import path,include
from . import views


urlpatterns = [
    # function based view
    path('', views.students, name='students'),  # this is the URL pattern that will be matched when the user visits the URL /students/
    # path('', views.students ),  # this is the URL pattern that will be matched when the user visits the URL /students/
]
