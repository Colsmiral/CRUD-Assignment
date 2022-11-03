from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

class Song(models.Model):
    Song = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    Artiste_id = models.CharField(max_length=200)
    likes = models.IntegerField()

class Lyrics(models.Model):
    Lyrics = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    content = models.CharField(max_length=1500)
    Song_id = models.CharField(max_length=200)
   