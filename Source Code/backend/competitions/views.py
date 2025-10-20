from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse
from .models import Competition, Appearance, Grade, Competition_Judge
from users.models import User
from users.decorators import role_required
from django.views.decorators.csrf import csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!


def competition_list(request):
    competitions = Competition.objects.all()
    return HttpResponse(competitions)

@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['ORGANIZER'])
def competition_create(request):
    if request.method == 'POST':
        competition = Competition(
            organizer=request.user,
            date=request.POST.get('date'),
            location = request.POST.get('location'),
            description=request.POST.get('description'),
            status='draft' 
        )      
        competition.save()
        return HttpResponse(competition)
    
    return HttpResponse("Stvori natjecanje.html")


def competition_detail(request, id):
    competition = get_object_or_404(Competition, id=id)
    appearances = Appearance.objects.get(competition=competition)
    return HttpResponse(appearances)


@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['ORGANIZER'])
def competition_edit(request, id):
    competition = get_object_or_404(Competition, id=id)

    if competition.organizer != request.user:
        return HttpResponseForbidden("Pristup zabranjen.")

    if request.method == 'POST':
        for field in Competition._meta.fields:
            attr = field.name  
            if attr in ['id', 'status']:
                continue
            if request.POST.get(attr):
                setattr(competition, attr, request.POST.get(attr))

        competition.status = 'draft'       
        competition.save()
        return HttpResponse(competition)

    return HttpResponse("Prepravi.html")


@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['ORGANIZER'])
def competition_publish(request, id):
    competition = get_object_or_404(Competition, id=id)

    if competition.organizer != request.user:
        return HttpResponseForbidden("Pristup zabranjen.")

    if request.method == 'POST':
        competition.status = 'published'
        competition.save()
        return HttpResponse(competition)

    return HttpResponse("Objavi.html")


@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['ORGANIZER'])
def competition_invite_judge(request, id):
    competition = get_object_or_404(Competition, id=id)

    if competition.organizer != request.user:
        return HttpResponseForbidden("Pristup zabranjen.")
    
    if competition.status == 'active':
        return HttpResponseForbidden("Natjecanje je aktivno.")

    if request.method == 'POST':
        email = request.POST.get('email')
        if not User.objects.filter(email=email).exists():
            return HttpResponse("Mail.html")
        user = User.objects.get(email=email)
        if user.role != 'JUDGE':
            return HttpResponseForbidden("Korisnik nije sudac.")
        competition_judge = Competition_Judge(
            competition=competition,
            judge=user
        )
        competition_judge.save()
        return HttpResponse(competition_judge)

    return HttpResponse("Pozovi suca.html")


@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['ORGANIZER'])
def competition_activate(request, id):
    competition = get_object_or_404(Competition, id=id)

    if competition.organizer != request.user:
        return HttpResponseForbidden("Pristup zabranjen.")

    if request.method == 'POST':
        if not Competition_Judge.objects.filter(competition=competition).exists():
            return HttpResponseForbidden("Nema sudaca.")
        if Competition_Judge.objects.filter(competition=competition).count() / 2 == 1:
            return HttpResponseForbidden("Broj sudaca je paran.")
        competition.status = 'active'
        competition.save()
        return HttpResponse(competition)

    return HttpResponse("Aktiviraj.html")


@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['ORGANIZER'])
def competition_deactivate(request, id):
    competition = get_object_or_404(Competition, id=id)

    if competition.organizer != request.user:
        return HttpResponseForbidden("Pristup zabranjen.")

    if request.method == 'POST':
        competition.status = 'published'
        competition.save()
        return HttpResponse(competition)

    return HttpResponse("Ugasi.html")


@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['JUDGE'])
def competition_grade(request, competition_id, appearance_id):
    competition = get_object_or_404(Competition, id=competition_id)
    appearance = get_object_or_404(Appearance, id=appearance_id)

    if request.method == 'POST':
        if competition.status != 'active':
            return HttpResponseForbidden("Natjecanje nije aktivno.")
        
        if not Competition_Judge.objects.filter(competition=competition, judge=request.user).exists():
            return HttpResponseForbidden("Pristup zabranjen.")
        
        appearance_grade = request.POST.get('grade')
        grade = Grade(
            judge=request.user,
            appearance=appearance,
            grade=appearance_grade
        )
        grade.save()

        return HttpResponse(grade)
    
    return HttpResponse("Ocijeni.html")

@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['CLUB_MANAGER'])
def competition_signup(request, id):
    competition = get_object_or_404(Competition, id=id)

    if request.method == 'POST':
        if competition.status != 'published':
            return HttpResponseForbidden("Prijava nije moguća.")
        
        appearance = Appearance()
        for field in Appearance._meta.fields:
            attr = field.name  
            if attr in ['id', 'club_manager', 'competition']:
                continue
            if request.POST.get(attr):
                setattr(appearance, attr, request.POST.get(attr))
            else:
                return HttpResponseForbidden("Nepotpuna prijava.")

        if appearance.age_category not in competition.age_categories\
            or appearance.style_category not in competition.style_categories\
            or appearance.group_size_category not in competition.group_size_categories:
            return HttpResponseForbidden("Nepodrzana kategorija.")
        appearance.club_manager = request.user
        appearance.competition = competition
        appearance.save()

        return HttpResponse(appearance)
    
    return HttpResponse("Prijavi nastup.html")
