from django.test import TestCase
from feed.models import community_centers, dog_gardens, elderly_social_club, playgrounds, sport_facilities, urban_nature


class community_centersTest(TestCase):
    def setUpTestData(self):
        self.obj = community_centers.objects.create(Name='Name test',
                            Address='Address test',
                            neighborhood='neighborhood test',
                            lat='lat test',
                            lon='lon test',
                            id=0)

    def test_Name(self):
        self.assertEqual(self.obj.Name, 'Name test')

    def test_Address(self):
        self.assertEquals(self.obj.Address, 'Address test')

    def test_neighborhood(self):
        self.assertEquals(self.obj.neighborhood, 'neighborhood test')

    def test_lat(self):
        self.assertEquals(self.obj.lat, 'lat test')

    def test_lon(self):
        self.assertEquals(self.obj.lon, 'lon test')

    def test_id(self):
        self.assertEquals(self.obj.id, 0)

    def test_Name_max_length(self):
        self.assertEqual(self.obj._meta.get_field('Name').max_length, 255)

    def test_Address_max_length(self):
        self.assertEquals(self.obj._meta.get_field('Address').max_length, 255)

    def test_neighborhood_max_length(self):
        self.assertEquals(self.obj._meta.get_field('neighborhood').max_length, 255)

    def test_lat_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        self.assertEquals(self.obj.__str__(), 'Name test')

class dog_gardensTest(TestCase):
    def setUpTestData(self):
        self.obj = dog_gardens.objects.create(Name='Name test',
                            SHAPE_Length='SHAPE_Length test',
                            SHAPE_Area='SHAPE_Area test',
                            lat='lat test',
                            lon='lon test',
                            id=0)


    def test_Name(self):
        self.assertEqual(self.obj.Name, 'Name test')

    def test_SHAPE_Length(self):
        self.assertEquals(self.obj.SHAPE_Length, 'SHAPE_Length test')

    def test_SHAPE_Area(self):
        self.assertEquals(self.obj.SHAPE_Area, 'SHAPE_Area test')

    def test_lat(self):
        self.assertEquals(self.obj.lat, 'lat test')

    def test_lon(self):
        self.assertEquals(self.obj.lon, 'lon test')

    def test_id(self):
        self.assertEquals(self.obj.id, 0)

    def test_Name_max_length(self):
        self.assertEqual(self.obj._meta.get_field('Name').max_length, 255)

    def test_SHAPE_Length_max_length(self):
        self.assertEquals(self.obj._meta.get_field('SHAPE_Length').max_length, 255)

    def test_SHAPE_Area_max_length(self):
        self.assertEquals(self.obj._meta.get_field('SHAPE_Area').max_length, 255)

    def test_lat_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        self.assertEquals(self.obj.__str__(), 'Name test')

class elderly_social_clubTest(TestCase):
    def setUpTestData(self):
        self.obj = elderly_social_club.objects.create(Name='Name test',
                            Address='Address test',
                            Type='Type test',
                            lat='lat test',
                            lon='lon test',
                            id=0)


    def test_Name(self):
        self.assertEqual(self.obj.Name, 'Name test')

    def test_Address(self):
        self.assertEquals(self.obj.Address, 'Address test')

    def test_Type(self):
        self.assertEquals(self.obj.Type, 'Type test')

    def test_lat(self):
        self.assertEquals(self.obj.lat, 'lat test')

    def test_lon(self):
        self.assertEquals(self.obj.lon, 'lon test')

    def test_id(self):
        self.assertEquals(self.obj.id, 0)

    def test_Name_max_length(self):
        self.assertEqual(self.obj._meta.get_field('Name').max_length, 255)

    def test_Type_max_length(self):
        self.assertEquals(self.obj._meta.get_field('Type').max_length, 255)

    def test_lat_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        self.assertEquals(self.obj.__str__(), 'Name test')

class playgroundsTest(TestCase):
    def setUpTestData(self):
        self.obj = playgrounds.objects.create(Name='Name test',
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


    def test_Name(self):
        self.assertEqual(self.obj.Name, 'Name test')

    def test_carrousel(self):
        self.assertEquals(self.obj.carrousel, 10)
    
    def test_combined1(self):
        self.assertEquals(self.obj.combined1, 10)
    
    def test_combined2(self):
        self.assertEquals(self.obj.combined2, 10)

    def test_combined3(self):
        self.assertEquals(self.obj.combined3, 10)
    
    def test_omega(self):
        self.assertEquals(self.obj.omega, 10)
    
    def test_roserose(self):
        self.assertEquals(self.obj.roserose, 10)
    
    def test_spring(self):
        self.assertEquals(self.obj.spring,10)
    
    def test_SpecialCom(self):
        self.assertEquals(self.obj.SpecialCom, 10)
    
    def test_slid(self):
        self.assertEquals(self.obj.slid, 10)
    
    def test_Swing(self):
        self.assertEquals(self.obj.Swing,10)
    
    def test_other(self):
        self.assertEquals(self.obj.other, 'other test')
    
    def test_shadowing(self):
        self.assertEquals(self.obj.shadowing, 'shadowing test')
    
    def test_surface(self):
        self.assertEquals(self.obj.surface, 'surface test')

    def test_lat(self):
        self.assertEquals(self.obj.lat, 'lat test')

    def test_lon(self):
        self.assertEquals(self.obj.lon, 'lon test')

    def test_id(self):
        self.assertEquals(self.obj.id, 0)

    def test_Name_max_length(self):
        self.assertEqual(self.obj._meta.get_field('Name').max_length, 255)
    
    def test_other_max_length(self):
        self.assertEquals(self.obj._meta.get_field('other').max_length, 255)
    
    def test_shadowing_max_length(self):
        self.assertEquals(self.obj._meta.get_field('shadowing').max_length, 255)
    
    def test_surface_max_length(self):
        self.assertEquals(self.obj._meta.get_field('surface').max_length, 255)

    def test_lat_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        self.assertEquals(self.obj.__str__(), 'Name test')
 
class sport_facilitiesTest(TestCase):
    def setUpTestData(self):
        self.obj = sport_facilities.objects.create(Name='Name test',
                            Type='Type test',
                            street='street test',
                            HouseNumber='HouseNumber test',
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
    def test_Name(self):
        self.assertEqual(self.obj.Name, 'Name test')

    def test_Type(self):
        self.assertEquals(self.obj.Type, 'Type test')

    def test_street(self):
        self.assertEquals(self.obj.street, 'street test')

    def test_HouseNumber(self):
        self.assertEquals(self.obj.HouseNumber, 'HouseNumber test')
    
    def test_neighborhood(self):
        self.assertEquals(self.obj.neighborhood, 'neighborhood test')
    
    def test_Operator(self):
        self.assertEquals(self.obj.Operator, 'Operator test')
    
    def test_Seats(self):
        self.assertEquals(self.obj.Seats, 10)
    
    def test_Activity(self):
        self.assertEquals(self.obj.Activity, 'Activity test')
    
    def test_fencing(self):
        self.assertEquals(self.obj.fencing, 'fencing test')
    
    def test_lighting(self):
        self.assertEquals(self.obj.lighting, 'lighting test')
    
    def test_condition(self):
        self.assertEquals(self.obj.condition, 'condition test')
    
    def test_Owner(self):
        self.assertEquals(self.obj.Owner, 'Owner test')
    
    def test_ForSchool(self):
        self.assertEquals(self.obj.ForSchool, 'ForSchool test')
    
    def test_association(self):
        self.assertEquals(self.obj.association, 'association test')
    
    def test_SportType(self):
        self.assertEquals(self.obj.SportType, 'SportType test')

    def test_lat(self):
        self.assertEquals(self.obj.lat, 'lat test')

    def test_lon(self):
        self.assertEquals(self.obj.lon, 'lon test')

    def test_id(self):
        self.assertEquals(self.obj.id, 0)

    def test_Name_max_length(self):
        self.assertEqual(self.obj._meta.get_field('Name').max_length, 255)

    def test_Type_max_length(self):
        self.assertEquals(self.obj._meta.get_field('Type').max_length, 255)

    def test_street_max_length(self):
        self.assertEquals(self.obj._meta.get_field('street').max_length, 255)

    def test_HouseNumber_max_length(self):
        self.assertEquals(self.obj._meta.get_field('HouseNumber').max_length, 255)
    
    def test_Operator_max_length(self):
        self.assertEquals(self.obj._meta.get_field('Operator').max_length, 255)
    
    def test_Activity_max_length(self):
        self.assertEquals(self.obj._meta.get_field('Activity').max_length, 255)
    
    def test_fencing_max_length(self):
        self.assertEquals(self.obj._meta.get_field('fencing').max_length, 255)
    
    def test_lighting_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lighting').max_length, 255)
    
    def test_condition_max_length(self):
        self.assertEquals(self.obj._meta.get_field('condition').max_length, 255)
    
    def test_Owner_max_length(self):
        self.assertEquals(self.obj._meta.get_field('Owner').max_length, 255)
    
    def test_ForSchool_max_length(self):
        self.assertEquals(self.obj._meta.get_field('ForSchool').max_length, 255)
    
    def test_association_max_length(self):
        self.assertEquals(self.obj._meta.get_field('association').max_length, 255)
    
    def test_SportType_max_length(self):
        self.assertEquals(self.obj._meta.get_field('SportType').max_length, 255)

    def test_neighborhood_max_length(self):
        self.assertEquals(self.obj._meta.get_field('neighborhood').max_length, 255)

    def test_lat_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        self.assertEquals(self.obj.__str__(), 'Name test')

class urban_natureTest(TestCase):
    def setUpTestData(self):
        self.obj = urban_nature.objects.create(MainFeature='MainFeature test',
                            lat='lat test',
                            lon='lon test',
                            id=0)


    def test_MainFeature(self):
        self.assertEqual(self.obj.MainFeature, 'MainFeature test')

    def test_lat(self):
        self.assertEquals(self.obj.lat, 'lat test')

    def test_lon(self):
        self.assertEquals(self.obj.lon, 'lon test')

    def test_id(self):
        self.assertEquals(self.obj.id, 0)

    def test_Name_max_length(self):
        self.assertEqual(self.obj._meta.get_field('MainFeature').max_length, 255)

    def test_lat_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lat').max_length, 255)

    def test_lon_max_length(self):
        self.assertEquals(self.obj._meta.get_field('lon').max_length, 255)

    def test_str(self):
        self.assertEquals(self.obj.__str__(), 'MainFeature test')      
