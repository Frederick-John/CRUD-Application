from django.db import models
#from datetime import dateline

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField()

    def _str_(self):
        return self.first_name

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete = models.PROTECT)
    title = models.CharField(max_length = 40)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.IntegerField()

    def _str_(self):
        return self.title

class Lyric(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete = models.PROTECT)
    Song = models.ForeignKey(Song, on_delete = models.PROTECT)
    content = models.CharField(max_length = 1000)
    song_id = models.IntegerField()

    def _str_(self):
        return self.song_id