from django.urls import path
from . import views

urlpatterns = [
    path('', views.competition_list, name='competition_list'),
    path('new/', views.competition_create, name='competition_create'),
    path('<int:id>/', views.competition_detail, name='competition_detail'),
    path('<int:id>/edit/', views.competition_edit, name='competition_edit'),
    path('<int:id>/publish/', views.competition_publish, name='competition_publish'),
]