# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from django.urls import reverse
from accounts.models import User
from feed.models import community_centers, dog_gardens, elderly_social_club, playgrounds, sport_facilities, urban_nature


class ChatRoomTest(TestCase):
    def setUp(self):
        #Arrange
        self.user = User.objects.create(email='testPostsFeedTest@text.com',
                                        user_name='PostsFeedTest user name',
                                        first_name='first name',
                                        last_name='last name',
                                        about='This is test',
                                        profile_image=None,
                                        password='user password')

    @tag('unit-test')
    def test_view_url(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('chat:chat_room', kwargs={'room_type':'test', 'room_id':4}))

        #Assert
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_view_uses_correct_template(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('chat:chat_room', kwargs={'room_type':'test', 'room_id':4}))

        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/chat_room.html')

    @tag('unit-test')
    def test_view_has_room_type(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('chat:chat_room', kwargs={'room_type':'test', 'room_id':4}))

        #Assert
        self.assertEqual(response.context["room_type"], 'test')

    @tag('unit-test')
    def test_view_has_room_id(self):
        #Arrange
        self.client.force_login(self.user)

        #Act
        response = self.client.get(reverse('chat:chat_room', kwargs={'room_type':'test', 'room_id':4}))

        #Assert
        self.assertEqual(response.context["room_id"], 4)

    @tag('unit-test')
    def test_view_has_room_description_community_centers(self):
        #Arrange
        self.client.force_login(self.user)
        obj = community_centers.objects.create(name='name test', address='address test', neighborhood='neighborhood test', lat='lat test',
                                               lon='lon test', id=0)

        #Act
        response = self.client.get(reverse('chat:chat_room', kwargs={'room_type':'community_centers', 'room_id':0}))

        #Assert
        self.assertEqual(response.context["room_description"], "מרכז קהילתי: " + obj.name)

    @tag('unit-test')
    def test_view_has_room_description_dog_gardens(self):
        #Arrange
        self.client.force_login(self.user)
        obj = dog_gardens.objects.create(name='name test', SHAPE_Length='SHAPE_Length test', SHAPE_Area='SHAPE_Area test', lat='lat test',
                                         lon='lon test', id=0)

        #Act
        response = self.client.get(reverse('chat:chat_room', kwargs={'room_type':'dog_gardens', 'room_id':0}))

        #Assert
        self.assertEqual(response.context["room_description"], "גינת כלבים: " + obj.name)

    @tag('unit-test')
    def test_view_has_room_description_elderly_social_club(self):
        #Arrange
        self.client.force_login(self.user)
        obj = elderly_social_club.objects.create(name='name test', address='address test', Type='Type test', lat='lat test',
                                                 lon='lon test', id=0)

        #Act
        response = self.client.get(reverse('chat:chat_room', kwargs={'room_type':'elderly_social_club', 'room_id':0}))

        #Assert
        self.assertEqual(response.context["room_description"], "מועדון חברתי לקשיש: " + obj.name)

    @tag('unit-test')
    def test_view_has_room_description_elderly_playgrounds(self):
        #Arrange
        self.client.force_login(self.user)
        obj = playgrounds.objects.create(name='name test', carrousel=10, combined1=10, combined2=10, combined3=10, omega=10, roserose=10,
                                         slid=10, SpecialCom=10, spring=10, Swing=10, other='other test', shadowing='shadowing test',
                                         surface='surface test', lat='lat test', lon='lon test', id=0)

        #Act
        response = self.client.get(reverse('chat:chat_room', kwargs={'room_type':'playgrounds', 'room_id':0}))

        #Assert
        self.assertEqual(response.context["room_description"], "גן משחקים: " + obj.name)

    @tag('unit-test')
    def test_view_has_room_description_elderly_sport_facilities(self):
        #Arrange
        self.client.force_login(self.user)
        obj = sport_facilities.objects.create(name='name test', Type='Type test', address='address test', neighborhood='neighborhood test',
                                              Operator='Operator test', Seats=10, Activity='Activity test', fencing='fencing test',
                                              lighting='lighting test', handicapped='handicapped test', condition='condition test',
                                              Owner='Owner test', ForSchool='ForSchool test', association='association test',
                                              SportType='SportType test', lat='lat test', lon='lon test', id=0)

        #Act
        response = self.client.get(reverse('chat:chat_room', kwargs={'room_type':'sport_facilities', 'room_id':0}))

        #Assert
        self.assertEqual(response.context["room_description"], "מתקן ספורט: " + obj.name)

    @tag('unit-test')
    def test_view_has_room_description_elderly_urban_nature(self):
        #Arrange
        self.client.force_login(self.user)
        obj = urban_nature.objects.create(MainFeature='MainFeature test', lat='lat test', lon='lon test', id=0)

        #Act
        response = self.client.get(reverse('chat:chat_room', kwargs={'room_type':'urban_nature', 'room_id':0}))

        #Assert
        self.assertEqual(response.context["room_description"], "אתר טבע עירוני: " + obj.MainFeature)
