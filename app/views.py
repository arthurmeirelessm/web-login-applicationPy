from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Admin
from django.contrib.auth import authenticate, login
# Create your views here



def loginPage(request): 
   print(request)
   return render(request, 'login.html')


def home(request): 
   print(request)
   return render(request, 'home.html')


def create(request): 
   print(request)
   return render(request, 'main.html')


def dologin(request): 
 if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']
    try:
          user = Admin.objects.get(email=email, password=password)
    except Admin.DoesNotExist: 
        user = None

    if user is not None: 
        return redirect('/home/')
    else: 
        return render(request, 'login.html', {'error_message': 'Senha incorreta'})
 else:
    return render(request, 'login.html')



def store(request): 
   print(request)
   return render(request, 'main.html')




