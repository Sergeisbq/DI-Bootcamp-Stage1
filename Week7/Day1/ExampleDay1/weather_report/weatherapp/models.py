from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Report(models.Model):

    CHOICES = (
        ('rainy', 'Rainy'),
        ('storm', 'Storm'),
        ('sunny', 'Sunny'),
        ('cloudy', 'Cloudy'),
    )

    location = models.CharField(max_length=50)
    temperature = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(60.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    weather_type = models.CharField(max_length=10, choices=CHOICES, blank=True, null=True)
    forecaster = models.ForeignKey('Forecaster', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.location}, {self.temperature}"
    

class Forecaster(models.Model):
    forecaster_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.forecaster_user}"
        
