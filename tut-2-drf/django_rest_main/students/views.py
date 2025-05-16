from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def students(request):
    # Logic to retrieve student data from the database
    students_data = [
        {"name": "John Doe", "age": 20, "grade": "A"},
        {"name": "Jane Smith", "age": 22, "grade": "B"},
        {"name": "Sam Brown", "age": 19, "grade": "C"},
    ]

    # Return the student data as a JSON response
    # In a real application, you would typically retrieve this data from a database
    return JsonResponse(students_data, safe=False)
