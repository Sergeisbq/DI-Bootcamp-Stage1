from django.db import models
from django.contrib.postgres.fields import ArrayField


class Customer(models.Model):

    first_name = models.CharField(max_length=50, blank=False, db_index=True)
    last_name = models.CharField(max_length=50, blank=False, db_index=True)
    email = models.EmailField()
    # allergens = ArrayField(models.CharField(max_length=250, null=True))
    allergens = models.ManyToManyField('Allergens')

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.allergens}"
    

   
class Dishes(models.Model):
    
    name = models.CharField(max_length=50, blank=False, db_index=True)
    dish = ArrayField(models.CharField(max_length=250))

    def __str__(self):
        return f"{self.name} {self.dish}"
    


class Restaurant(models.Model):

    name = models.CharField(max_length=50, blank=False, db_index=True, unique=True)
    address = models.CharField(max_length=100, blank=False, db_index=True)

    def __str__(self):
        return f"{self.name}"
    


class Menu(models.Model):

    restaurant_id = models.ManyToManyField('Restaurant', blank=True, db_index=True)
    dish_id = models.ManyToManyField('Dishes', blank=True, db_index=True)
    # dish_id = models.ForeignKey('Dishes', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.restaurant_id} {self.dish_id}"



class Allergens(models.Model):

    name = models.CharField(max_length=50, blank=False, db_index=True, unique=True)

    def __str__(self):
        return f"{self.name}"


