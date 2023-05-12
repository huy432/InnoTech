from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request:HttpRequest):
    context = {} 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context['un'] = username

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            context['error'] = 'Username or password is incorrect'
    return render(request=request, template_name='pages/login.html', context=context)

def register(request:HttpRequest):
    error = ""
    context = {} 
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        context['un'] = username
        context['em'] = email

        if User.objects.filter(username=username).count() != 0:
            error = 'Your username has been used'
        elif User.objects.filter(email=email).count() != 0:
            error = 'Your email has been used'
        elif len(password1) < 8:
            error = 'Your password must be 8 or more in length'
        elif any(i in password1 for i in """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""):
            error = 'Your password has special character'
        elif password1 != password2:
            error = 'Two password are not same'
        else:
            try:
                User.objects.create_user(username, email, password1)
                return redirect('/')
            except Exception as e:
                error = e
    context['error'] = '*' + error
    return render(request=request, template_name='pages/register.html', context=context)

@login_required(login_url='/authenticate/login/')
def profile(request):
    return render(request=request, template_name='pages/profile.html')

@login_required(login_url='/authenticate/login/')
def logout(request):
    auth.logout(request)
    return redirect('/')
