from django.db import models

# Create your models here.

class Gif(models.Model):
    title = models.CharField(max_length = 50)
    url = models.URLField(blank = True, null = True)
    uploader_name = models.CharField(max_length = 50)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.title}"
    

class Category(models.Model):
    name = models.CharField(max_length = 50)
    gifs = models.ManyToManyField('Gif')

    def __str__(self):
        return f"{self.name}"
