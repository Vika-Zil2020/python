from django.shortcuts import render
from django.http import HttpResponse
from .models import BookStore

def find_book(request):
	obj_1= BookStore.objects.filter(book_name='book')
	return HttpResponse(obj_1.order_by('publishing_date'))







 


# Create your views here.


