from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect

def login_user(request):
    context =  {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("uploadnew")
            
        else: 
            return HttpResponseRedirect("login_user")
            

    else:
        return render(request, "./authentication/login.html", context)
        print("form doldurmadan yonlendirilcek yer")
