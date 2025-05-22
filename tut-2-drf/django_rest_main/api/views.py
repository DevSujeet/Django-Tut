from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# from django.shortcuts import render
from students.models import Student
from .paginations import CustomPagination
from employees.filters import EmployeeFilter
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
from django.http import Http404

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


from employees.models import Employee
from employees.serializer import EmployeeSerializer
from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view



# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class EmployeeDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
        

#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
from rest_framework import mixins
from rest_framework import generics

# class Employees(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)
    
# class EmployeeDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk=pk)

#     def put(self, request, pk):
#         return self.update(request, pk=pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk=pk)
###############################################
# Generic views
# class Employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     # ListCreateAPIView is a combination of ListAPIView and CreateAPIView

# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     # RetrieveUpdateDestroyAPIView is a combination of RetrieveAPIView, UpdateAPIView and DestroyAPIView

from rest_framework import viewsets

###############################################
# viewsets
# ViewSets are a way to combine the logic for a set of related views into a single class

'''
class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,  status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):     
        # queryset = Employee.objects.all()
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 '''   
###############################################
# model viewset 
class EmployeeViewSet(viewsets.ModelViewSet):
    # ModelViewSet is a combination of ListCreateAPIView and RetrieveUpdateDestroyAPIView
    # ModelViewSet provides the full set of CRUD operations
    # ModelViewSet automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination # this is used to set the pagination class for the viewset
    # filterset_fields = ['designation'] # this is used to set the filter fields for the viewset
    filterset_class = EmployeeFilter # this is used to set the filter class for the viewset

from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer , BlogWithCommentsSerializer


class BlogsView(generics.ListCreateAPIView): 
    queryset = Blog.objects.all()
    serializer_class = BlogWithCommentsSerializer#BlogSerializer
    # ListCreateAPIView is a combination of ListAPIView and CreateAPIView

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # ListCreateAPIView is a combination of ListAPIView and CreateAPIView

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogWithCommentsSerializer
    lookup_field = 'pk' # this is used to specify the field to be used for lookups
    # RetrieveUpdateDestroyAPIView is a combination of RetrieveAPIView, UpdateAPIView and DestroyAPIView
    # RetrieveUpdateDestroyAPIView provides the full set of CRUD operations

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk' # this is used to specify the field to be used for lookups
    # RetrieveUpdateDestroyAPIView is a combination of RetrieveAPIView, UpdateAPIView and DestroyAPIView
    # RetrieveUpdateDestroyAPIView provides the full set of CRUD operations