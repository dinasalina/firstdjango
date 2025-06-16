from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    post_list = Post.objects.all()

    context = {
        'post_list': post_list,
    }

    return render(request, "home.html", context)
    
    