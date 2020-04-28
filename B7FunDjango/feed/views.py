# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import json
from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import community_centers, dog_gardens, elderly_social_club, playgrounds,\
    sport_facilities, urban_nature


@login_required(login_url='/')
def feed(request):
    weather = get_weather()
    return render(request, 'feed/feed.html',
                  {"community_centers_json": json.dumps(list(community_centers.objects.values())),
                   "dog_gardens_json": json.dumps(list(dog_gardens.objects.values())),
                   "elderly_social_club_json":
                   json.dumps(list(elderly_social_club.objects.values())),
                   "playgrounds_json": json.dumps(list(playgrounds.objects.values())),
                   "sport_facilities_json": json.dumps(list(sport_facilities.objects.values())),
                   "urban_nature_json": json.dumps(list(urban_nature.objects.values())),
                   "community_centers": community_centers.objects.values(),
                   "dog_gardens": dog_gardens.objects.values(),
                   "elderly_social_club": elderly_social_club.objects.values(),
                   "playgrounds": playgrounds.objects.values(),
                   "sport_facilities": sport_facilities.objects.values(),
                   "urban_nature": urban_nature.objects.values(),
                   "temperature": weather['temperature'],
                   "icon": weather['icon']})


@login_required(login_url='/')
def filter_data(request, search_term):
    return render(request, 'feed/feed.html',
                  {"community_centers_json":
                   json.dumps(list(community_centers.objects.filter(
                       Q(name__contains=search_term) | Q(address__contains=search_term)).values())),
                   "dog_gardens_json":
                   json.dumps(list(dog_gardens.objects.filter(
                       name__contains=search_term).values())),
                   "elderly_social_club_json":
                   json.dumps(list(elderly_social_club.objects.filter(
                       Q(name__contains=search_term) | Q(address__contains=search_term)).values())),
                   "playgrounds_json":
                   json.dumps(list(playgrounds.objects.filter(
                       name__contains=search_term).values())),
                   "sport_facilities_json":
                   json.dumps(list(sport_facilities.objects.filter(
                       Q(name__contains=search_term) | Q(address__contains=search_term)).values())),
                   "urban_nature_json":
                   json.dumps(list(urban_nature.objects.filter(
                       Q(MainFeature__contains=search_term)).values())),
                   "community_centers": community_centers.objects.filter(
                       Q(name__contains=search_term) | Q(address__contains=search_term)).values(),
                   "dog_gardens": dog_gardens.objects.filter(
                       name__contains=search_term).values(),
                   "elderly_social_club": elderly_social_club.objects.filter(
                       Q(name__contains=search_term) | Q(address__contains=search_term)).values(),
                   "playgrounds": playgrounds.objects.filter(
                       name__contains=search_term).values(),
                   "sport_facilities": sport_facilities.objects.filter(
                       Q(name__contains=search_term) | Q(address__contains=search_term)).values(),
                   "urban_nature": urban_nature.objects.filter(
                       Q(MainFeature__contains=search_term)).values()})


def get_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a34020b19effe33baf44bd412063bb58'
    city = 'Beer Sheva'
    city_weather = requests.get(url.format(city)).json()
    temperature = round((float(city_weather['main']['temp'])))
    temperature = str(temperature)
    weather = {
        'temperature': temperature,
        'icon': city_weather['weather'][0]['icon']
    }
    return weather