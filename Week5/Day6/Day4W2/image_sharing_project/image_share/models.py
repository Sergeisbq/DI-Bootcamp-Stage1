from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):

    file = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=50, blank=False, db_index=True)
    description = models.CharField(max_length=150, blank=False, db_index=True)
    user_upload = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}| {self.description}"



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    number_of_images = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f"{self.user.username}"
    

# User -> create_user_profile -> UserProfile(User) -> 