from django.db import models
from datetime import date

# Create your models here.

class Country(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Film(models.Model):

    title = models.CharField(max_length=50)
    release_date = models.DateField(default=date.today())
    created_in_country = models.ForeignKey('Country')