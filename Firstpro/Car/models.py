from django.db import models

class Car(models.Model):
	production_year = models.IntegerField()
	price = models.IntegerField()
	mark = models.CharField(max_length = 30)
	owner_name = models.CharField(max_length = 30)
	horse_power = models.IntegerField()
	number_doors = models.IntegerField()


# Create your models here.
