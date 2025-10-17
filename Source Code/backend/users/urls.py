from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('organizer/', views.organizers, name="organizer.home"),
    path('club_manager/', views.club_managers, name="club_manager.home"),
    path('judge/', views.judges, name="judge.home")
]