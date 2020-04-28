# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PostFeed


@login_required(login_url='/')
def admin_posts(request):
    posts = PostFeed.objects.all().order_by('date')
    return render(request, 'postsFeed/admin_posts.html', {'posts': posts})
