# setting up the env
uv venv

# Activate env
Activate with: source .venv/bin/activate
# installing Django
sujeetkumar@Sujeets-Laptop django_tut % uv pip install django
# creating project in Django
(django_tut) sujeetkumar@Sujeets-Laptop django_tut % django-admin startproject myproject 

# starting the Django server
(django_tut) sujeetkumar@Sujeets-Laptop django_tut % cd myproject 
(django_tut) sujeetkumar@Sujeets-Laptop myproject % python3 manage.py runserver 8000

