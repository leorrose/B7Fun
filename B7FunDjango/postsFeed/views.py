from django.shortcuts import render
from .models import PostFeed
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def posts(request):
    if request.user.is_authenticated:
        print(True)
    posts = PostFeed.objects.all().order_by('date')
    return render(request, 'postsFeed/posts.html', {'posts': posts})