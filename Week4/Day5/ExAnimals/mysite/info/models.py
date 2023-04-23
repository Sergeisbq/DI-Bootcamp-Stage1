from django.db import models

# Create your models here.

class Family(models.Model):
    # id is automatically created
    name = models.CharField(max_length = 50) # varchar in sql

# {
#     "id": 1,
#     "name": "Felidae"
# }


class Animal(models.Model):
    # id is automatically created
    name = models.CharField(max_length = 50) # varchar in sql
    legs = models.IntegerField() # int in sql
    weight = models.FloatField() # float in sql
    height = models.FloatField() # float in sql
    speed = models.FloatField() # float in sql
    family = models.ForeignKey(Family, on_delete = models.SET_NULL, null = True)
    image = models.URLField(blank = True, null = True)

# {
#     "id" :1,
#     "name": "Dog",
#     "legs": 4,
#     "weight": 5.67,
#     "height": 4.2,
#     "speed": 34,
#     "family": 2
# }

