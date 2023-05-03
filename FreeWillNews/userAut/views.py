from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    context =  {}
    try:
        return render(request, "./authentication/login.html", context)
    except:
        print("the template does not exist")