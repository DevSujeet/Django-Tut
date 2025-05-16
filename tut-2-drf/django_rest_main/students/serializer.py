from rest_framework import serializers
from .models import Student
from rest_framework.serializers import ModelSerializer

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # This will include all fields from the Student model
        # fields = ['name', 'age']  # You can specify specific fields if needed