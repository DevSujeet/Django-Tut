# DRF tut - https://www.youtube.com/watch?v=8d1HgJTEGe8&t=3456s

# django rest framework
## installation / https://www.django-rest-framework.org/#installation
    uv pip install djangorestframework
## add rest framework to django
    Add 'rest_framework' to your INSTALLED_APPS setting(myproject/setting.py) 

### create a student app
    python3 manage.py startapp students

### integrate the app
    Add 'students' to your INSTALLED_APPS

## add URL /student
    add this to urlpatterns in the projects urls.py

    path('students/', include('students.urls')), #any request that is coming to /students, I want ot forward it to 'students/urls'

### create urls.py in the app(students) as it is not there by default.
    add this
    from django.urls import path,include
    from . import views


    urlpatterns = [
        # function based view
        path('', views.students, name='students'),  # this is the URL pattern that will be matched when the user visits the URL /students/
        # path('', views.students ),  # this is the URL pattern that will be matched when the user visits the URL /students/
    ]


### add a function to views.py in the app so as to return the response.
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

    This return a json response for /student

## creating API endpoints
    there can be seperate approach to this.

1 st approach
1.  add a urlpatterns to the projects urls
    path('api/v1/students/', include('students.api.urls')),  # Uncomment this line to include the students API URLs

    This means that api/v1/students is a url path and it will look for url in this path 'students.api.urls'
    That I means I will have to create a folder api in the students(app) folder and add file urls.py to it and then give urlpatterns which would then point to function views.

2nd approach
    create a 'api' app and it will come with its own view.py and we can create urls.py as required
    - if app is create it need to be added to INSTALLED_APPS in setting.py



## Class Based views
## mixins
## generics
## routers
## viewsets.ViewSet
## viewsets.ModelViewSet

## Nested serializer

# steps to create a new app
    1. python3 manage.py startapp blogs
    2. register in the project settings.py under INSTALLED_APPS = []
    3. to register model update in Admin.py
        admin.site.register(Blog)
    4. After making model

# pagination
    1. global pagination (works for generics/viewsets)
    updatein settings.py
        REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 2,
        }

    2. custom Pagination (mixin/apiview)

# filtering
    django filters
    - indigidual field
    - combine multiple filters
    - apply different look up expressions (like i-contains, i-exact ..lte/gte)
    - custom filter with own logic

    ## installation
        pip install django-filter
    ## register in settings.py
    ## global filter: 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'], in the REST_FRAMEWORK in settings.py
        - filterset_fields = ['designation']  in the views
        - but these are case sensitive/exact match

    ## custom filter


# search filter
    in view
    from rest_framework import searchFilter

    in views class
    filter_backends = [SearchFiltes, Django]
    search_fields = ['blog_title', 'blog_content'] //not complete check vid

# ordering filter   
    ordering_fields = ['id', 'blog_title']