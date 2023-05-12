from django.urls import path
from . import views
urlpatterns = [
    path('', views.movieshomepage),
    path('video/', views.video)
]
