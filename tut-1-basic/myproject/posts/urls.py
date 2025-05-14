from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # this is the URL pattern that will be matched when the user visits the URL /posts/
]