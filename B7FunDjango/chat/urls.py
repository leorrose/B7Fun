# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.urls import path
from . import views


app_name = 'chat'


urlpatterns = [
    path('chat_rooms/<str:room_type>/<int:room_id>/', views.chat_room, name='chat_room'),
]
