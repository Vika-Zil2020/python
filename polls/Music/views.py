from django.shortcuts import render
from .models import Album,Songs
from django.http import HttpResponse

def count(request,album_id):
	my_list=[]
	album_con = Album.objects.get(pk = album_id)
	song_con = Songs.objects.filter(album = album_id)
	for song in song_con:
		my_list.append('<br>' + song.song_name + ' ' + str(song.star))
	return HttpResponse(album_con.album_name + ''.join (my_list))





# Create your views here.
