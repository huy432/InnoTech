from django.urls import path
from . import views
urlpatterns = [
    path('', views.movieshomepage),
    path('video/<str:fid>/<str:chap>', views.video)
]
