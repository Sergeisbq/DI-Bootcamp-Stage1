from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from datetime import datetime 
# from polls.models import Post

# Create your models here.

class UserProfile(AbstractBaseUser):

    email = models.EmailField(verbose_name="email address", max_length=255, unique=True, default='')
    date_of_birth = models.DateField(default=datetime.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.URLField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"]
    # favorite_authors = models.ManyToManyField(UserProfile)

    def __str__(self):
        return f"{self.user.username}"
    

# User -> create_user_profile -> UserProfile(User) -> 