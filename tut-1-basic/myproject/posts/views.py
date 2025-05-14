from django.shortcuts import render

from .models import Posts


# Create your views here.
def post_list(request):
    posts_list = Posts.objects.all()  # this will get all the posts from the database
    # this will render the template posts/posts_list.html and pass the posts to the template,
    # {'posts': posts_list} the template(posts_list.html) will have access to a variable named posts, which is a list-like object (a QuerySet) containing all post objects.
    return render(request, 'posts/posts_list.html', {'posts': posts_list})  