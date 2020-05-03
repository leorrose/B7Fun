# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=attribute-defined-outside-init

from django.contrib import admin
from .models import community_centers, dog_gardens, elderly_social_club,\
    playgrounds, sport_facilities, urban_nature


@admin.register(community_centers)
class CommunityCentersAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("name", "address", "neighborhood", "lat", "lon")
    search_fields = ['address', 'name']

@admin.register(dog_gardens)
class DogGardensAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("name", "SHAPE_Area", "SHAPE_Length", "lat", "lon")
    search_fields = ['name']

@admin.register(elderly_social_club)
class ElderlySocialClubAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('name', 'address', 'Type', 'lat', 'lon')
    search_fields = ['address', 'name']


@admin.register(playgrounds)
class PlayGroundsAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("name", "lat", "lon")
    search_fields = ['name']

@admin.register(sport_facilities)
class SportFacilitiesAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("name", "address", "neighborhood", "lat", "lon")
    search_fields = ['address', 'name']

@admin.register(urban_nature)
class UrbanNatureAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("MainFeature", "lat", "lon")
    search_fields = ['MainFeature']
