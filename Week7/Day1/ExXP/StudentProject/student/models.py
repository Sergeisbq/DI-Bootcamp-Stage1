from django.db import models

# Create your models here.

class Student(models.Model):

   first_name = models.CharField(max_length=50, blank=True)
   last_name = models.CharField(max_length=50, blank=True)
   email = models.EmailField(blank=True, null=True)
   date_joined = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f"{self.first_name} {self.last_name}"