from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login, name='login_page'),
    path('register/',views.register, name='register_page'),
    path('profile/',views.profile, name='profile_page'),
    path('logout/',views.logout, name='logout_action'),
]
