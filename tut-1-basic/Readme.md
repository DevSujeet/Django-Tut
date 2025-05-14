# reference
    https://www.youtube.com/watch?v=Rp5vd34d-z4&t=1275s
# extenstions used
    vscode-icons
    Django (Baptiste )
# vscode setting
    - cmd + , (to open settings)
    - search emmet
    - include language
    - add item
    - django-html:html
usage fr html page. type "!" and press tab to get a basic html page.
To get emoji you can use this command:- ctrl + cmd + spacebar

# setting up the env
uv venv

# Activate env
Activate with: source .venv/bin/activate

# installing Django
uv pip install django

# creating project in Django
django-admin startproject myproject 

# starting the Django server
cd myproject 
python3 manage.py runserver 8000 # note 8000 is also the default folder

Note: db.sqlite3 is created on running the server for the first time.

# stopping the server
ctrl + c

# return http response / returning some text
- create/Update the myproject/views.py
    - Add function view to render html pages or Httpresponse(containing html)
    - eg:-  from django.http import HttpResponse
            from django.shortcuts import render

            def homepage(request):
                return HttpResponse("Hello, world. ")

- Update the myproject/urls.py
    add these to - urlpatterns array.
        path('', views.homepage),
        path('about/',views.about)

# creating template html for myproject
- create templates folder (add home.html and about.html)
- Go to myproject/setting.py
- edit TEMPLATES -> DIRS to DIRS:['templates']
- This will tell django to look for html pages in this folder

- To return html templates update the views.py
            def homepage(request):
                return render(request, 'home.html')

- Update the myproject/urls.py
    add these to - urlpatterns array.
        path('', views.homepage),
        path('about/',views.about)


## to apply css and js in the html templates
- go to the setting.py
- import os # at the top
- add this below STATIC_URL.
-
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'), # Add this line to include the static directory Where the static files are located
    ]
- we can add style sheet using "django templating engine"
- add this just below doctype
    {% load static %} #this load the static assets in the template
- to link the stylesheet
    <link rel="stylesheet" href="{% static 'css/style.css' %}">

## link js - similar to applying css
{% load static %} #under doctype
<script src="{% static 'js/main.js' %}" defer></script> #inside head tag # defer means that load script when the page has loaded.

# creating apps and template
    - difference-between-app-and-project-in-django ?
    A project is typically the top-level directory that contains all the files and directories needed for a Django application to run.

    It’s where you define the database settings, URL routing, and other global configurations for the applications that it contains.

    App: a Django application is a self-contained module that can be plugged into any Django project.

    An application is typically designed to serve a specific purpose or feature within a project, and can include models, views, templates, and static files.

    # steps to create App
    - python3 manage.py startapp [name of the app eg:post]
        - This will create and posts folder structure.
    
    Goto the settings.py in the myproject folder and add to INSTALLED_APPS:
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'posts' # we have told Django that we have a new app called posts
        ]

    - note views.py is already prsent in the posts folder
        add this:
        # Create your views here.
        def post_list(request):
            return render(request, 'posts/posts_list.html', {}) # this is the view function that will be called when the user visits the URL /posts/

    - create a templates folder in the posts folder # remember we had told django to look for templates
        folderd dir.this applicable to both app and project
    - again create a "post" dir inthe template dir
        - this create a namespace
        - Add html file as required

    - To make route available for the apps
        - create urls.py in the posts app, similar to the urls.py in the project folder.

        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.post_list, name='post_list'),  # this is the URL pattern that will be matched when the user visits the URL /posts/
]
    - To integrate the app route to the main project.
    update the "urls.py" to include the app routes.
        add this to urlpatters = []
            path('posts/', include('posts.urls')),  # this is the URL pattern that will be matched when the user visits the URL /posts/

# Creating skeleton Template that can be used in various pages
    You can create a skelton HTML and add place holers using blocks
    <title>
        {% block title %}
            Django App
        {% endblock  %}
    </title>

    we have created a layout.html for skeleton, which would be used by home and about page

    We do this extention like this:

    {% extends "layout.html" %} # to extend the layout.html

    {% block title %} # the block values can be
    Home
    {% endblock title %}

    {%block content %}
        <h1>Home Page</h1>
        <p>Welcome to the Home page of this Django project.</p>
        <p>checkout my <a href="/about">About</a> page.</p>
    {% endblock content %}

# model and migration
    There are models.py file in the app's folder (Posts in this case).
    We can define data model here. these models would correspond to a table in the data base.
    The table create happens when we migrate the migration. Before doing the migration we
    have to create the migration file which describe the creation and changes to a given model and
    thus these changes are migrated seemlessly.
    STEPS:
    1. Create/Define data model
        - Create model Posts
    2. create migration / this creates migration file to keep track of changes to the model
        - $ python3 manage.py makemigrations
        Migrations for 'posts':
        posts/migrations/0001_initial.py # migrtion file is created

    3. apply migrations
        $ python3 manage.py migrate

        This will apply migration that was created by the user as well as the migration that 
        were built-in by the system.

# Django ORM
    ORM test in interactive shell
    $ python3 manage.py shell

    # Interactive shell session sample
    Python 3.13.2 (main, Feb  5 2025, 18:58:04) [Clang 19.1.6 ] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from posts.models import Posts
    >>> p = Posts()
    >>> p.title = "My first post"
    >>> p.save()
    >>> Posts.obects.all()
    Traceback (most recent call last):
    File "<console>", line 1, in <module>
    AttributeError: type object 'Posts' has no attribute 'obects'. Did you mean: 'objects'?
    >>> Posts.objects.all()
    <QuerySet [<Posts: My first post>]>
    >>> exit() # to leave the shell

# Django Admin
    $ python3 manage.py createsuperuser
        Username (leave blank to use 'sujeetkumar'): sunny
        Email address: 
        Password: 
        Password (again):      #sunny@987
        The password is too similar to the username.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.

    # start the server and open /admin -> lgin with above cred

    # the Admin page can also be used as content management system.
    But we dont see the posts that we had created.
    To do this we need to registed this model with the admin
    - Go to the posts/admin.py
        from posts.models import Posts

        # Register your models here.
        admin.site.register(Posts)
    - Now you can see posts on the admin panel and add new post to the db from here.

# access model data into html
    - Update hte views.py in posts
    def post_list(request):
        posts_list = Posts.objects.all()  # this will get all the posts from the database
        return render(request, 'posts/posts_list.html', {'posts': posts_list}) # Template will have access to the "posts" as array of queryset.

    # in the Post_list,html do this:
        <section>
        <h2>Posts</h2>
        {% for post in posts %}  # we passed this posts data as dict
            <article>
                <h3>{{ post.title }}</h3>
                <p>{{ post.content }}</p>
                <p>Published on: {{ post.created_at }}</p>
            </article>
        {% empty %}
            <p>No posts available.</p>
        {% endfor %}

# what we have done so far is creating web application endpoints and not the API endpoints
    - A web endpoint is where a html pages are rendered and can be accessed via browser
    - API endpoint are generally used by other application/ api client like postman.