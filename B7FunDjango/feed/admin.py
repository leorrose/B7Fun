# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from django.contrib import admin
from .models import community_centers, dog_gardens, elderly_social_club,\
    playgrounds, sport_facilities, urban_nature


class CommunityCentersAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'neighborhood', 'lat', 'lon']

    def get_queryset(self, request):
        qs = super(CommunityCentersAdmin, self).get_queryset(request)
        self.request = request
        return qs


admin.site.register(community_centers, CommunityCentersAdmin)
admin.site.register(dog_gardens)
admin.site.register(elderly_social_club)
admin.site.register(playgrounds)
admin.site.register(sport_facilities)
admin.site.register(urban_nature)
