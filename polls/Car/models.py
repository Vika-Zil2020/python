from django.db import models
class Car(models.Model):
	production_year = models.IntegerField()
	price = models.IntegerField()
	mark = models.CharField(max_length = 10)
	owner_name = models.CharField(max_length = 15)
	number_of_doors = models.IntegerField()

# Create your models here.
