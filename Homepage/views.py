from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import User
from .models import Product

# Create your views here.
def homepage(request):
    return render(request=request, template_name= 'pages/homepage.html')
def details(request:HttpRequest, id):
    item = Product.objects.get(id = id)
    rating_star = []
    rate = item.rating
    for i in range(0, 5):
        if rate >= 1:
            rating_star.append(10)
            rate -= 1
        elif rate > 0:
            rating_star.append(5)
            rate = 0
        else:
            rating_star.append(0)
        
    context = {
        'name': item.name,
        'description':item.description,
        'details':eval(item.details),
        'rating': item.rating,
        'price':item.price,
        'image': f'image/products/{item.thumbnail}/',
        'ratingstar': rating_star
    }
    return render(request=request, template_name= 'pages/details.html', context=context)
def addtocart(request, data:str):
    id = data.split('#')[0]
    d = data.split('#')[1:]
    return details(request=request, id=id)

def userprofile(request:HttpRequest, username):
    user = User.objects.get(username=username)
    context = {
        'username': user.username,
        'own': False
    }
    return render(request, 'pages/profile.html', context=context)

def profile(request:HttpRequest):
    context = {
        'username': request.user.username,
        'own': True,
        'products': [1] * 10
    }
    return render(request, 'pages/profile.html', context=context)
