from django.http import JsonResponse
# from django.shortcuts import render
from students.models import Student

# Create your views here.


# def api_students(request): #function based view
    # Logic to retrieve student data from the database
    # students_data = [
    #     {"name": "John Doe", "age": 20, "grade": "A"},
    #     {"name": "Jane Smith", "age": 22, "grade": "B"},
    #     {"name": "Sam Brown", "age": 19, "grade": "D"},
    # ]
    # # In a real application, you would typically retrieve this data from a database
    # return JsonResponse(students_data, safe=False)
    ########################################################
    # students_data = Student.objects.all()
    # # Convert the queryset to a list of dictionaries   /// not ideal..use serializer 
    # students_data = [
    #     {
    #         "name": student.name,
    #         "age": student.age,
    #         "grade": student.grade,
    #     }
    #     for student in students_data
    # ]
    # # Return the student data as a JSON response
    # return JsonResponse(students_data, safe=False)
########################################################
    # Not recoomened to use this method

    # students_data = Student.objects.all() # all() method returns a queryset of all Student objects in the database
    # students_list = list(students_data.values()) # serializing is taking value from queryset and converting it to a list of dictionaries
    # # Return the student data as a JSON response
    # return JsonResponse(students_list, safe=False)

########################################################
    # use serializer
    # from .serializers import StudentSerializer
    # serializer are used to convert complex data types, such as querysets and model instances,
    #  into native Python datatypes that can then be easily rendered into JSON, XML or
    #  other content types.
    # they also do validation and deserialization
    # different types of serializers
    # 1. ModelSerializer
    # 2. Serializer
    # 3. HyperlinkedModelSerializer
    # 4. ListSerializer
    # if you know how django models works, then you can understand how to use ModelSerializer

from students.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])  # this decorator is used to specify the allowed HTTP methods for the view
def api_students(request):  # function based view
    # if request.method == 'GET':
    students_data = Student.objects.all()
    serializer = StudentSerializer(students_data, many=True) #many=True means that we are serializing a queryset (multiple objects)
    return Response(serializer.data, status=status.HTTP_200_OK) # 200 means OK

@api_view(['post'])
def create_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #save the data to the database
            # serializer.save() is used to save the validated data to the database
            # serializer.save() will create a new Student object in the database
            # and populate it with the data from the serializer
            # serializer.save() will also return the created object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
@api_view(['GET', 'PUT', 'DELETE']) # ,  #this decorator is used to specify the allowed HTTP methods for the vie
def fetch_student(request, pk):
    try:
        student = Student.objects.get(pk=pk) # get the student object with the given primary key
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

