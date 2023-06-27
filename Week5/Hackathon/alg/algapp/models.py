from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Customer(models.Model):

    first_name = models.CharField(max_length=50, blank=False, db_index=True)
    last_name = models.CharField(max_length=50, blank=False, db_index=True)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    allergens = models.ManyToManyField('Ingredients')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

   
class Dishes(models.Model):
    
    name = models.CharField(max_length=50, blank=False, db_index=True)
    dish_main_ings = ArrayField(models.CharField(max_length=250))
    dish_var_ings = ArrayField(models.CharField(max_length=250, default=[], null=True))

    def __str__(self):
        return f"{self.name} {self.dish_main_ings}"
    def list_ing(self):
        return ", ".join(self.dish_main_ings, self.dish_var_ings)
    

class DishesIng(models.Model):
    
    name = models.CharField(max_length=50, blank=False, db_index=True)
    dish_main_ingredients = models.ManyToManyField('Ingredients', related_name='main_dishes')
    dish_var_ingredients = models.ManyToManyField('Ingredients', related_name='var_dishes')

    def __str__(self):
        return f"{self.name} {self.dish_main_ingredients}"
    def list_ing(self):
        return ", ".join(self.dish_main_ingredients, self.dish_var_ingredients)


class Restaurant(models.Model):

    name = models.CharField(max_length=50, blank=False, db_index=True, unique=True)
    address = models.CharField(max_length=100, blank=False, db_index=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.address}"
    


class Menu(models.Model):

    restaurant_id = models.ManyToManyField('Restaurant', blank=True, db_index=True, related_name='menus')
    dish_id = models.ManyToManyField('DishesIng', blank=True, db_index=True, related_name='menus')
    # dish_id = models.ForeignKey('Dishes', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.restaurant_id} {self.dish_id}"



class Allergens(models.Model):

    name = models.CharField(max_length=50, blank=False, db_index=True, unique=True)

    def __str__(self):
        return f"{self.name}"
    
class Ingredients(models.Model):

    name = models.CharField(max_length=50, blank=False, db_index=True, unique=True)

    def __str__(self):
        return f"{self.name}"
    

class Statistic(models.Model):

    file = models.JSONField()



