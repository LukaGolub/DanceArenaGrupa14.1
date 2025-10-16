from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import role_required

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

@role_required(['ORGANIZER'])
def organizers(req):
    return HttpResponse('Organizer.html')

@role_required(['CLUB_MANAGER'])
def club_managers(req):
    return HttpResponse('Club manager.html')

@role_required(['JUDGE'])
def judges(req):
    return HttpResponse('Judge.html')

