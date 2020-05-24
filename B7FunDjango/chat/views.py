# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from feed.models import community_centers, dog_gardens, elderly_social_club, playgrounds, sport_facilities, urban_nature

@login_required(login_url='/')
def chat_room(request, room_type, room_id):
    room_description = ''
    if room_type == "community_centers":
        room_description += "מרכז קהילתי: " + community_centers.objects.filter(id=room_id)[0].name
    elif room_type == "dog_gardens":
        room_description += "גינת כלבים: " + dog_gardens.objects.filter(id=room_id)[0].name
    elif room_type == "elderly_social_club":
        room_description += "מועדון חברתי לקשיש: " + elderly_social_club.objects.filter(id=room_id)[0].name
    elif room_type == "playgrounds":
        room_description += "גן משחקים: " + playgrounds.objects.filter(id=room_id)[0].name
    elif room_type == "sport_facilities":
        room_description += "מתקן ספורט: " + sport_facilities.objects.filter(id=room_id)[0].name
    elif room_type == "urban_nature":
        room_description += "אתר טבע עירוני: " + urban_nature.objects.filter(id=room_id)[0].MainFeature

    return render(request, 'chat/chat_room.html', {'room_type': room_type, 'room_id' : room_id, 'room_description': room_description})
    