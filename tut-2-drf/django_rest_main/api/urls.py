from django.urls import path,include
from . import views

# to work woth viewsets
from rest_framework.routers import DefaultRouter 
from .views import EmployeeViewSet


router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee') #


urlpatterns = [
    # function based view
    path('student/', views.api_students, name='students'),  # this is the URL pattern that will be matched when the user visits the URL /students/
    path('student/create/', views.create_student, name='create student'),
    # path('update/<int:pk>/', views.update_student, name='update student'),
    # path('delete/<int:pk>/', views.delete_student, name='delete student'),
    path('student/fetch/<int:pk>/', views.fetch_student, name='get students with id'),  # this is the URL pattern that will be matched when the user visits the URL /students/
    # path('', views.students ),  # this is the URL pattern that will be matched when the user visits the URL /students/

    # path('employee/', views.Employees.as_view(), name='employees get / create'),  # this is the URL pattern that will be matched when the user visits the URL /students/
    # path('employee/<int:pk>/', views.EmployeeDetail.as_view(), name='employee detail fetch / update / delete'),  # this is the URL pattern that will be matched when the user visits the URL /students/

    path('', include(router.urls)),  # this is the URL pattern that will be matched when the user visits the URL /employees/

    path('blogs/', views.BlogsView.as_view(), name='blogs'),  # this is the URL pattern that will be matched when the user visits the URL /students/
    path('comments/', views.CommentsView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog detail'),  # this is the URL pattern that will be matched when the user visits the URL /students/
   path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment detail'),  # this is the URL pattern that will be matched when the user visits the URL /students/
]   