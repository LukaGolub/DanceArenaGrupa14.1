from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import User

def login_user(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)

    else:
        return HttpResponse('Need to login.html')
    
    if user is not None:
        role = user.get_role_display()
        login(req, user)
        if role.lower() == 'admin':
            return redirect('/admin')
        else:
            return redirect('/users/' + role.lower()) 

def organizers(req):
    return HttpResponse('Organizer.html')

def club_managers(req):
    return HttpResponse('Club manager.html')

def judges(req):
    return HttpResponse('Judge.html')

