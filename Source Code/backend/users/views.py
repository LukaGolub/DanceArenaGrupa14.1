from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import role_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
    else:
        return HttpResponse("Login.html")
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

def google_login(request):
    user_email = None
    user_name = None
    if request.user.is_authenticated:
        user_email = request.user.email
        user_name = request.user.get_full_name() or request.user.username
    return render(request, 'users/google_login.html', {
        'user_email': user_email,
        'user_name': user_name,
    })

def custom_logout(request):
    logout(request)
    return redirect('/users/google-login/')
