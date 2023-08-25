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
   print(request)
   email = request.POST['email']
   print(email)
   password = request.POST['password']
   return null



def store(request): 
   print(request)
   return render(request, 'main.html')




