from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'posts/posts_list.html', {}) # this is the view function that will be called when the user visits the URL /posts/