from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse
from .models import Competition, Appearance, Grade
from users.decorators import role_required
from django.views.decorators.csrf import csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!


def competition_list(request):
    competitions = Competition.objects.all()
    return HttpResponse(competitions)

@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['ORGANIZER'])
def competition_create(request):
    print(request.POST)
    if request.method == 'POST':
        competition = Competition()
        competition.organizer = request.user
        competition.date = request.POST.get('date')
        competition.location = request.POST.get('location')
        competition.description = request.POST.get('description')  
        competition.status = 'draft'       
        competition.save()
        return redirect('competition_detail', id=competition.id)
    
    return HttpResponse('Stvori natjecanje')


def competition_detail(request, id):
    competition = get_object_or_404(Competition, id=id)
    appearances = Appearance.objects.get(competition=competition)
    return HttpResponse(appearances)


@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['ORGANIZER'])
def competition_edit(request, id):
    competition = get_object_or_404(Competition, id=id)

    if competition.organizer != request.user:
        return HttpResponseForbidden("You cannot edit this competition.")

    if request.method == 'POST':
        for field in Competition._meta.fields:
            attr = field.name  
            if attr in ['id', 'status']:
                continue
            if request.POST.get(attr):
                setattr(competition, attr, request.POST.get(attr))

        competition.status = 'draft'       
        competition.save()
        return redirect('competition_detail', id=competition.id)

    return HttpResponse('edit')


@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['ORGANIZER'])
def competition_publish(request, id):
    competition = get_object_or_404(Competition, id=id)

    if competition.organizer != request.user:
        return HttpResponseForbidden("You cannot publish this competition.")

    if request.method == 'POST':
        competition.status = 'published'
        competition.save()
        return redirect('competition_detail', id=competition.id)

    return HttpResponse(competition)


@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['ORGANIZER'])
def competition_activate(request, id):
    competition = get_object_or_404(Competition, id=id)

    if competition.organizer != request.user:
        return HttpResponseForbidden("You cannot activate this competition.")

    if request.method == 'POST':
        competition.status = 'active'
        competition.save()
        return redirect('competition_detail', id=competition.id)

    return HttpResponse(competition)


@csrf_exempt #FOR POSTMAN !!!!!!!!!!!!!!!!!!
@role_required(['JUDGE'])
def competition_grade(request, competition_id, appearance_id):
    competition = get_object_or_404(Competition, id=competition_id)
    appearance = get_object_or_404(Appearance, id=appearance_id)

    if request.method == 'POST':
        if competition.status != 'active':
            return HttpResponseForbidden("You cannot judge an inactive competition.")
        
        if False:
            return HttpResponseForbidden("You cannot grade this appearance.")
        
        appearance_grade = request.POST.get('grade')
        grade = Grade(
            judge=request.user,
            appearance=appearance,
            grade=appearance_grade
        )
        grade.save()

        return HttpResponse(grade)
    
    return HttpResponse(str(competition) + '\n' + str(appearance))
