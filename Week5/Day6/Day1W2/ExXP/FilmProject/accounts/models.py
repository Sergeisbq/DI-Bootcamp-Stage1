from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(null=True, blank=True)
    last_name = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} {self.user.first_name} {self.user.first_name}"