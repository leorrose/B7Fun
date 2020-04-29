# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name


from django.db import models


class community_centers(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=255, verbose_name="Address")
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")
    name = models.CharField(max_length=255, verbose_name="name")
    neighborhood = models.CharField(
        max_length=255, verbose_name="neighborhood")

    class Meta:
        db_table = 'community_centers'
        verbose_name_plural = 'community centers'

    def __str__(self):
        return self.name


class dog_gardens(models.Model):
    id = models.IntegerField(primary_key=True)
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")
    name = models.CharField(max_length=255, verbose_name="name")
    SHAPE_Area = models.CharField(max_length=255, verbose_name="SHAPE_Area")
    SHAPE_Length = models.CharField(
        max_length=255, verbose_name="SHAPE_Length")

    class Meta:
        db_table = 'dog_gardens'
        verbose_name_plural = 'dog gardens'

    def __str__(self):
        return self.name


class elderly_social_club(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=255, verbose_name="Address")
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")
    name = models.CharField(max_length=255, verbose_name="name")
    Type = models.CharField(max_length=255, verbose_name="type")

    class Meta:
        db_table = 'elderly_social_club'
        verbose_name_plural = 'elderly social clubs'

    def __str__(self):
        return self.name


class playgrounds(models.Model):
    id = models.IntegerField(primary_key=True)
    carrousel = models.IntegerField(verbose_name="carrousel")
    combined1 = models.IntegerField(verbose_name="combined1")
    combined2 = models.IntegerField(verbose_name="combined2")
    combined3 = models.IntegerField(verbose_name="combined3")
    omega = models.IntegerField(verbose_name="omega")
    roserose = models.IntegerField(verbose_name="roserose")
    slid = models.IntegerField(verbose_name="slid")
    SpecialCom = models.IntegerField(verbose_name="SpecialCom")
    spring = models.IntegerField(verbose_name="spring")
    Swing = models.IntegerField(verbose_name="Swing")
    other = models.CharField(max_length=255, verbose_name="other")
    shadowing = models.CharField(max_length=255, verbose_name="shadowing")
    surface = models.CharField(max_length=255, verbose_name="surface")
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")
    name = models.CharField(max_length=255, verbose_name="name")

    class Meta:
        db_table = 'play_grounds'
        verbose_name_plural = 'play grounds'

    def __str__(self):
        return self.name


class sport_facilities(models.Model):
    id = models.IntegerField(primary_key=True)
    Type = models.CharField(max_length=255, verbose_name="shadowing")
    name = models.CharField(max_length=255, verbose_name="name")
    address = models.CharField(max_length=255, verbose_name="address")
    neighborhood = models.CharField(
        max_length=255, verbose_name="neighborhood")
    Operator = models.CharField(max_length=255, verbose_name="Operator")
    Seats = models.IntegerField(verbose_name="Seats")
    Activity = models.CharField(max_length=255, verbose_name="Activity")
    fencing = models.CharField(max_length=255, verbose_name="fencing")
    lighting = models.CharField(max_length=255, verbose_name="lighting")
    handicapped = models.CharField(max_length=255, verbose_name="handicapped")
    condition = models.CharField(max_length=255, verbose_name="condition")
    Owner = models.CharField(max_length=255, verbose_name="Owner")
    ForSchool = models.CharField(max_length=255, verbose_name="ForSchool")
    association = models.CharField(max_length=255, verbose_name="association")
    SportType = models.CharField(max_length=255, verbose_name="SportType")
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")

    class Meta:
        db_table = 'sport_facilities'
        verbose_name_plural = 'sport facilities'

    def __str__(self):
        return self.name


class urban_nature(models.Model):
    id = models.IntegerField(primary_key=True)
    MainFeature = models.CharField(max_length=255, verbose_name="MainFeature")
    lat = models.CharField(max_length=255, verbose_name="lat")
    lon = models.CharField(max_length=255, verbose_name="lon")

    class Meta:
        db_table = 'urban_nature'
        verbose_name_plural = 'urban nature'

    def __str__(self):
        return self.MainFeature
