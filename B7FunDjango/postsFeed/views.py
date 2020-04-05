from django.shortcuts import render
from .models import PostFeed

# Create your views here.
def posts(request):
    posts = PostFeed.objects.all().order_by('date')
    return render(request, 'postsFeed/posts.html', {'posts': posts})