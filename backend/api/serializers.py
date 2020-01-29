from rest_framework import serializers
from .models import Culinary, StatesAndCities

class CulinarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Culinary
        fields = ('name', 'dishes')

class StatesAndCitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatesAndCities
        fields = ('initials', 'state', 'cities')