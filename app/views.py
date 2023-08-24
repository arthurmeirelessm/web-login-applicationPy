from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here


def home(request): 
   print(request)
   return render(request, 'home.html')


def create(request): 
   print(request)
   return render(request, 'main.html')

def dologin(request): 
user = authenticate(email=request.POST['email'], password=request.POST['password'])
if user is not None:
    # A backend authenticated the credentials
   login(request, user)
   return redirect('/home/') 
else:
    # No backend authenticated the credentials
    return render(request, 'login.html')



def store(request): 
   print(request)
   return render(request, 'main.html')




