from django.db import models
from django.contrib.postgres.fields import ArrayField


class Customer(models.Model):

    first_name = models.CharField(max_length=50, blank=False, db_index=True)
    last_name = models.CharField(max_length=50, blank=False, db_index=True)
    email = models.EmailField()
    # allergens = ArrayField(models.CharField(max_length=250, null=True))
    allergens = models.ManyToManyField('Allergens')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

   
class Dishes(models.Model):
    
    name = models.CharField(max_length=50, blank=False, db_index=True)
    dish = ArrayField(models.CharField(max_length=250))

    def __str__(self):
        return f"{self.name} {self.dish}"
    def list_ing(self):
        return ", ".join(self.dish)
    


class Restaurant(models.Model):

    name = models.CharField(max_length=50, blank=False, db_index=True, unique=True)
    address = models.CharField(max_length=100, blank=False, db_index=True)

    def __str__(self):
        return f"{self.name} {self.address}"
    


class Menu(models.Model):

    restaurant_id = models.ManyToManyField('Restaurant', blank=True, db_index=True, related_name='menus')
    dish_id = models.ManyToManyField('Dishes', blank=True, db_index=True, related_name='menus')
    # dish_id = models.ForeignKey('Dishes', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.restaurant_id} {self.dish_id}"



class Allergens(models.Model):

    name = models.CharField(max_length=50, blank=False, db_index=True, unique=True)

    def __str__(self):
        return f"{self.name}"


