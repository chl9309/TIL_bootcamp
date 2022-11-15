from django.db import models

# Create your models here.

class Movie(models.Model):

    id= models.IntegerField()
    title = models.CharField()
    