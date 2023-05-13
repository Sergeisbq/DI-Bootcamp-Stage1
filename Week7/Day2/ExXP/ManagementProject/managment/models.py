from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):

   name = models.CharField(max_length=50, blank=True)
   description = models.TextField(max_length=100, blank=True)

   def __str__(self):
       return f"{self.name}"
   

class Employee(models.Model):
   
   name = models.CharField(max_length=50, blank=True)
   email = models.EmailField(blank=True, null=True)
   phone_number = models.CharField(max_length=50, blank=True)
   department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
   project = models.ManyToManyField('Project')
   administrator = models.BooleanField()
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_connect')

   def __str__(self):
       return f"{self.name} {self.department}"
   

class Task(models.Model):

   name = models.CharField(max_length=50, blank=True)
   description = models.TextField(max_length=100, blank=True)
   due_date = models.DateField(blank=True)
   completed = models.BooleanField()
   project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)

   def __str__(self):
       return f"{self.name} {self.due_date}"
   

class Project(models.Model):

   name = models.CharField(max_length=50, blank=True)
   description = models.TextField(max_length=100, blank=True)
   start_date = models.DateField(blank=True)
   end_date = models.DateField(blank=True)
   
   def __str__(self):
       return f"{self.name}, {self.start_date}, {self.end_date}"
   

   

