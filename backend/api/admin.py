from django.contrib import admin
from .models import Culinary, StatesAndCities

class CulinaryAdmin(admin.ModelAdmin):
    model = Culinary
    list_display = ('name', 'dishes')
    search_fields = ('name', 'dishes')

class StatesAndCitiesAdmin(admin.ModelAdmin):
    model = StatesAndCities
    list_display = ('initials', 'state', 'cities')
    search_fields = ('initials', 'state', 'cities')

admin.site.register(Culinary, CulinaryAdmin)
admin.site.register(StatesAndCities, StatesAndCitiesAdmin)