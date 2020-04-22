from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import community_centers, dog_gardens, elderly_social_club, playgrounds, sport_facilities, urban_nature
import json

@login_required(login_url='/')
def feed(request):
    return render(request,'feed/feed.html', {"community_centers": json.dumps(list(community_centers.objects.values())),
    "dog_gardens": json.dumps(list(dog_gardens.objects.values())),
    "elderly_social_club": json.dumps(list(elderly_social_club.objects.values())),
    "playgrounds": json.dumps(list(playgrounds.objects.values())),
    "sport_facilities": json.dumps(list(sport_facilities.objects.values())),
    "urban_nature": json.dumps(list(urban_nature.objects.values()))})