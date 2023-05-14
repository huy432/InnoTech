from django.shortcuts import render
from django.http import HttpRequest
from .models import Film, Chapter
# Create your views here.
def movieshomepage(request:HttpRequest):
    return render(request, 'pages/moviesbase.html')

def video(request:HttpRequest,fid,chap):
    film = Film.objects.get(filmid = fid)
    context = {
        'film':film.title
    }
    return render(request, 'pages/video.html', context=context)