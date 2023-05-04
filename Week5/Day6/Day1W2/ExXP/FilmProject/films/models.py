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
    created_in_country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='films_created')
    available_in_countries = models.ManyToManyField('Country', related_name='films_available')
    category = models.ManyToManyField('Category')
    director = models.ManyToManyField('Director',  related_name='films')

    def __str__(self) -> str:
        return f"{self.title} {self.release_date} {self.created_in_country} {self.director}"
    

class Director(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"