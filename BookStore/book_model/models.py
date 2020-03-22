from django.db import models

class BookStore(models.Model):
    book_name = models.CharField(max_length=20)
    publishing_date = models.IntegerField()
    author_name = models.CharField(max_length=25)
    book_genre = models.CharField(max_length = 20)



# Create your models here.
