from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('organizer/', views.organizers),
    path('club_manager/', views.club_managers),
    path('judge/', views.judges)
]