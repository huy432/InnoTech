from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def movieshomepage(request:HttpRequest):
    return render(request, 'pages/moviesbase.html')

def video(request:HttpRequest):
    return render(request, 'pages/video.html')