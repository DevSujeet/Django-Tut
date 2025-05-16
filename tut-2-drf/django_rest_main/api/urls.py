from django.urls import path,include
from . import views

urlpatterns = [
    # function based view
    path('', views.api_students, name='students'),  # this is the URL pattern that will be matched when the user visits the URL /students/
    path('create/', views.create_student, name='create student'),
    # path('update/<int:pk>/', views.update_student, name='update student'),
    # path('delete/<int:pk>/', views.delete_student, name='delete student'),
    path('fetch/<int:pk>/', views.fetch_student, name='get students with id'),  # this is the URL pattern that will be matched when the user visits the URL /students/
    # path('', views.students ),  # this is the URL pattern that will be matched when the user visits the URL /students/
]