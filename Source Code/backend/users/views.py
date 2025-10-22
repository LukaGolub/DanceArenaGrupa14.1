from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import role_required
from .models import Role
from django.views.decorators.csrf import csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!

@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
def login_user(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)

    else:
        return HttpResponse("Login.html")
    
    if user is not None:
        role = user.role
        print(Role.CLUB_MANAGER)
        print(role)
        login(req, user)
        if role.lower() == 'admin':
            return redirect('/admin')
        else:
            return redirect('/users/' + role.lower()) 

@role_required(Role.ORGANIZER)
def organizers(req):
    return HttpResponse('Organizer.html')

@role_required(Role.CLUB_MANAGER)
def club_managers(req):
    return HttpResponse('Club manager.html')

@role_required(Role.JUDGE)
def judges(req):
    return HttpResponse('Judge.html')

