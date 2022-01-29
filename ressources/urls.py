"""time_table URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from saisie import views as saisie_views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('instructors/', views.instructors, name = 'instructors'),
    path('courses/', views.courses, name = 'courses'),
    path('rooms/', views.rooms, name = 'rooms'),
    path('students/', views.departments, name = 'departments'),
    path('meetingTimes/', views.meetingTimes, name = 'meetingTimes'),
    
    #Statistiques
    path('charts/', views.charts, name = 'charts'),

    #Voir les emplois du temps en cours
    path('timetables_to_approve/', views.timetables_to_approve, name = 'timetables_to_approve'),
    #afficher un emploi du temps
    path('print_timetable/<str:pk>', saisie_views.print_timetable, name = 'print_timetable'), 
    #Valider un emploi du temps
    path('approve_timetable/<str:pk>', views.approve_timetable, name = 'approve_timetable'), 

    #CRUD pour les ressources
    path('create_instructor/', views.create_instructor, name = 'create_instructor'),
    path('update_instructor/<str:pk>', views.update_instructor, name = 'update_instructor'),
    path('delete_instructor/<str:pk>', views.delete_instructor, name = 'delete_instructor'),

    path('create_course/', views.create_course, name = 'create_course'),
    path('update_course/<str:pk>', views.update_course, name = 'update_course'),
    path('delete_course/<str:pk>', views.delete_course, name = 'delete_course'),

    path('create_meetingTime/', views.create_meetingTime, name = 'create_meetingTime'),
    path('update_meetingTime/<str:pk>', views.update_meetingTime, name = 'update_meetingTime'),
    path('delete_meetingTime/<str:pk>', views.delete_meetingTime, name = 'delete_meetingTime'),

    path('create_room/', views.create_room, name = 'create_room'),
    path('update_room/<str:pk>', views.update_room, name = 'update_room'),
    path('delete_room/<str:pk>', views.delete_room, name = 'delete_room'),

    path('create_department/', views.create_department, name = 'create_department'),
    path('update_department/<str:pk>', views.update_department, name = 'update_department'),
    path('delete_department/<str:pk>', views.delete_department, name = 'delete_department'),

    path('create_meetingTime/', views.create_meetingTime, name = 'create_meetingTime'),
    path('update_meetingTime/<str:pk>', views.update_meetingTime, name = 'update_meetingTime'),
    path('delete_meetingTime/<str:pk>', views.delete_meetingTime, name = 'delete_meetingTime'),
    
    
    ]
    