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

# stopping the server
ctrl + c

# steps to create App
    - python3 manage.py startapp [name of the app eg:post]
    - Goto the settings.py in the myproject folder and add to INSTALLED_APPS:

# model and migration
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