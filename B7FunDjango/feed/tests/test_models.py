# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.test import TestCase, tag
from feed.models import community_centers, dog_gardens, elderly_social_club,\
    playgrounds, sport_facilities, urban_nature


@tag('unit-test')
class CommunityCentersTest(TestCase):
    def setUp(self):
        self.obj = community_centers.objects.create(name='name test',
                                                    address='address test',
                                                    neighborhood='neighborhood test',
                                                    lat='lat test',
                                                    lon='lon test',
                                                    id=0)

    def test_name(self):
        #Assert
        self.assertEqual(self.obj.name, 'name test')

    def test_address(self):
        #Assert
        self.assertEqual(self.obj.address, 'address test')

    def test_neighborhood(self):
        #Assert
        self.assertEqual(self.obj.neighborhood, 'neighborhood test')

    def test_lat(self):
        #Assert
        self.assertEqual(self.obj.lat, 'lat test')

    def test_lon(self):
        #Assert
        self.assertEqual(self.obj.lon, 'lon test')

    def test_id(self):
        #Assert
        self.assertEqual(self.obj.id, 0)

    def test_name_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('name').max_length, 255)

    def test_address_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('address').max_length, 255)

    def test_neighborhood_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('neighborhood').max_length, 255)

    def test_lat_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        #Assert
        self.assertEqual(self.obj.__str__(), 'name test')

@tag('unit-test')
class DogGardensTest(TestCase):
    def setUp(self):
        #Arrange
        self.obj = dog_gardens.objects.create(name='name test',
                                              SHAPE_Length='SHAPE_Length test',
                                              SHAPE_Area='SHAPE_Area test',
                                              lat='lat test',
                                              lon='lon test',
                                              id=0)

    def test_name(self):
        #Assert
        self.assertEqual(self.obj.name, 'name test')

    def test_shape_length(self):
        #Assert
        self.assertEqual(self.obj.SHAPE_Length, 'SHAPE_Length test')

    def test_shape_area(self):
        #Assert
        self.assertEqual(self.obj.SHAPE_Area, 'SHAPE_Area test')

    def test_lat(self):
        #Assert
        self.assertEqual(self.obj.lat, 'lat test')

    def test_lon(self):
        #Assert
        self.assertEqual(self.obj.lon, 'lon test')

    def test_id(self):
        #Assert
        self.assertEqual(self.obj.id, 0)

    def test_name_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('name').max_length, 255)

    def test_shape_length_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('SHAPE_Length').max_length, 255)

    def test_shape_area_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('SHAPE_Area').max_length, 255)

    def test_lat_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        #Assert
        self.assertEqual(self.obj.__str__(), 'name test')

@tag('unit-test')
class ElderlySocialClubTest(TestCase):
    def setUp(self):
        #Arrange
        self.obj = elderly_social_club.objects.create(name='name test',
                                                      address='address test',
                                                      Type='Type test',
                                                      lat='lat test',
                                                      lon='lon test',
                                                      id=0)

    def test_name(self):
        #Assert
        self.assertEqual(self.obj.name, 'name test')

    def test_address(self):
        #Assert
        self.assertEqual(self.obj.address, 'address test')

    def test_type(self):
        #Assert
        self.assertEqual(self.obj.Type, 'Type test')

    def test_lat(self):
        #Assert
        self.assertEqual(self.obj.lat, 'lat test')

    def test_lon(self):
        #Assert
        self.assertEqual(self.obj.lon, 'lon test')

    def test_id(self):
        #Assert
        self.assertEqual(self.obj.id, 0)

    def test_name_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('name').max_length, 255)

    def test_type_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('Type').max_length, 255)

    def test_lat_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        #Assert
        self.assertEqual(self.obj.__str__(), 'name test')

@tag('unit-test')
class PlaygroundsTest(TestCase):
    def setUp(self):
        #Arrange
        self.obj = playgrounds.objects.create(name='name test',
                                              carrousel=10,
                                              combined1=10,
                                              combined2=10,
                                              combined3=10,
                                              omega=10,
                                              roserose=10,
                                              slid=10,
                                              SpecialCom=10,
                                              spring=10,
                                              Swing=10,
                                              other='other test',
                                              shadowing='shadowing test',
                                              surface='surface test',
                                              lat='lat test',
                                              lon='lon test',
                                              id=0)

    def test_name(self):
        #Assert
        self.assertEqual(self.obj.name, 'name test')

    def test_carrousel(self):
        #Assert
        self.assertEqual(self.obj.carrousel, 10)

    def test_combined1(self):
        #Assert
        self.assertEqual(self.obj.combined1, 10)

    def test_combined2(self):
        #Assert
        self.assertEqual(self.obj.combined2, 10)

    def test_combined3(self):
        self.assertEqual(self.obj.combined3, 10)

    def test_omega(self):
        #Assert
        self.assertEqual(self.obj.omega, 10)

    def test_roserose(self):
        #Assert
        self.assertEqual(self.obj.roserose, 10)

    def test_spring(self):
        #Assert
        self.assertEqual(self.obj.spring, 10)

    def test_special_com(self):
        #Assert
        self.assertEqual(self.obj.SpecialCom, 10)

    def test_slid(self):
        self.assertEqual(self.obj.slid, 10)

    def test_swing(self):
        #Assert
        self.assertEqual(self.obj.Swing, 10)

    def test_other(self):
        #Assert
        self.assertEqual(self.obj.other, 'other test')

    def test_shadowing(self):
        #Assert
        self.assertEqual(self.obj.shadowing, 'shadowing test')

    def test_surface(self):
        #Assert
        self.assertEqual(self.obj.surface, 'surface test')

    def test_lat(self):
        #Assert
        self.assertEqual(self.obj.lat, 'lat test')

    def test_lon(self):
        #Assert
        self.assertEqual(self.obj.lon, 'lon test')

    def test_id(self):
        #Assert
        self.assertEqual(self.obj.id, 0)

    def test_name_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('name').max_length, 255)

    def test_other_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('other').max_length, 255)

    def test_shadowing_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('shadowing').max_length, 255)

    def test_surface_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('surface').max_length, 255)

    def test_lat_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        #Assert
        self.assertEqual(self.obj.__str__(), 'name test')

@tag('unit-test')
class SportFacilitiesTest(TestCase):
    def setUp(self):
        #Arrange
        self.obj = sport_facilities.objects.create(name='name test',
                                                   Type='Type test',
                                                   address='address test',
                                                   neighborhood='neighborhood test',
                                                   Operator='Operator test',
                                                   Seats=10,
                                                   Activity='Activity test',
                                                   fencing='fencing test',
                                                   lighting='lighting test',
                                                   handicapped='handicapped test',
                                                   condition='condition test',
                                                   Owner='Owner test',
                                                   ForSchool='ForSchool test',
                                                   association='association test',
                                                   SportType='SportType test',
                                                   lat='lat test',
                                                   lon='lon test',
                                                   id=0)

    def test_name(self):
        #Assert
        self.assertEqual(self.obj.name, 'name test')

    def test_type(self):
        #Assert
        self.assertEqual(self.obj.Type, 'Type test')

    def test_address(self):
        #Assert
        self.assertEqual(self.obj.address, 'address test')

    def test_neighborhood(self):
        #Assert
        self.assertEqual(self.obj.neighborhood, 'neighborhood test')

    def test_operator(self):
        #Assert
        self.assertEqual(self.obj.Operator, 'Operator test')

    def test_seats(self):
        #Assert
        self.assertEqual(self.obj.Seats, 10)

    def test_activity(self):
        #Assert
        self.assertEqual(self.obj.Activity, 'Activity test')

    def test_fencing(self):
        #Assert
        self.assertEqual(self.obj.fencing, 'fencing test')

    def test_lighting(self):
        self.assertEqual(self.obj.lighting, 'lighting test')

    def test_condition(self):
        #Assert
        self.assertEqual(self.obj.condition, 'condition test')

    def test_owner(self):
        #Assert
        self.assertEqual(self.obj.Owner, 'Owner test')

    def test_for_school(self):
        #Assert
        self.assertEqual(self.obj.ForSchool, 'ForSchool test')

    def test_association(self):
        #Assert
        self.assertEqual(self.obj.association, 'association test')

    def test_sport_type(self):
        #Assert
        self.assertEqual(self.obj.SportType, 'SportType test')

    def test_lat(self):
        #Assert
        self.assertEqual(self.obj.lat, 'lat test')

    def test_lon(self):
        #Assert
        self.assertEqual(self.obj.lon, 'lon test')

    def test_id(self):
        #Assert
        self.assertEqual(self.obj.id, 0)

    def test_name_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('name').max_length, 255)

    def test_type_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('Type').max_length, 255)

    def test_address_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('address').max_length, 255)

    def test_operator_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('Operator').max_length, 255)

    def test_activity_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('Activity').max_length, 255)

    def test_fencing_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('fencing').max_length, 255)

    def test_lighting_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lighting').max_length, 255)

    def test_condition_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('condition').max_length, 255)

    def test_owner_max_length(self):
        self.assertEqual(self.obj._meta.get_field('Owner').max_length, 255)

    def test_for_school_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('ForSchool').max_length, 255)

    def test_association_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('association').max_length, 255)

    def test_sport_type_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('SportType').max_length, 255)

    def test_neighborhood_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('neighborhood').max_length, 255)

    def test_lat_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        #Assert
        self.assertEqual(self.obj.__str__(), 'name test')

@tag('unit-test')
class UrbanNatureTest(TestCase):
    def setUp(self):
        #Arrange
        self.obj = urban_nature.objects.create(MainFeature='MainFeature test',
                                               lat='lat test',
                                               lon='lon test',
                                               id=0)

    def test_main_feature(self):
        #Assert
        self.assertEqual(self.obj.MainFeature, 'MainFeature test')

    def test_lat(self):
        #Assert
        self.assertEqual(self.obj.lat, 'lat test')

    def test_lon(self):
        #Assert
        self.assertEqual(self.obj.lon, 'lon test')

    def test_id(self):
        #Assert
        self.assertEqual(self.obj.id, 0)

    def test_name_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('MainFeature').max_length, 255)

    def test_lat_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        #Assert
        self.assertEqual(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        #Assert
        self.assertEqual(self.obj.__str__(), 'MainFeature test')
