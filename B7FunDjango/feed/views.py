# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import community_centers, dog_gardens, elderly_social_club, playgrounds,\
    sport_facilities, urban_nature


@login_required(login_url='/')
def feed(request):
    return render(request, 'feed/feed.html',
                  {"community_centers_json": json.dumps(list(community_centers.objects.values())),
                   "dog_gardens_json": json.dumps(list(dog_gardens.objects.values())),
                   "elderly_social_club_json":
                   json.dumps(list(elderly_social_club.objects.values())),
                   "playgrounds_json": json.dumps(list(playgrounds.objects.values())),
                   "sport_facilities_json": json.dumps(list(sport_facilities.objects.values())),
                   "urban_nature_json": json.dumps(list(urban_nature.objects.values()))})
