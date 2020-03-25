from django.db import models

class Album(models.Model):
	singer_name = models.CharField(max_length = 30)
	album_name = models.CharField(max_length = 20)
	release_year = models.DateTimeField('date release')

class Songs(models.Model):
	album =models.ForeignKey(Album,on_delete = models.CASCADE)
	song_name =models.CharField(max_length = 10)
	star = models.IntegerField(default=0)




# Create your models here.
