from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('details/<str:id>/', views.details),
    path('user/', views.profile),
    path('user/<str:username>/', views.userprofile)
]
