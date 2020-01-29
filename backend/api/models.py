from django.db import models
from django.contrib.postgres.fields import ArrayField

class Culinary(models.Model):
    name = models.CharField(max_length=30)
    dishes = ArrayField(models.CharField(max_length=60, blank=True), default=list)

    def __str__(self):
        return self.name

class StatesAndCities(models.Model):
    initials = models.CharField(max_length=2)
    state = models.CharField(max_length=25)
    cities = ArrayField(models.CharField(max_length=60, blank=True), default=list)
