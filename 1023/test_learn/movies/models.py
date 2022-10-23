from django.db import models

# Create your models here.
class Actor(models.Model):

    name = models.CharField(max_length=100)

class Movie(models.Model):

    actor_id = models.ManyToManyField("Actor", verbose_name=("movie_id"))
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()

class Review(models.Model):

    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
