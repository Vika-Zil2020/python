from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Vika')

# Create your views here.
