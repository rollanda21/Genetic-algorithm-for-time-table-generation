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
from ressources import views as ressources_views

#Name space


urlpatterns = [
    path('', views.index, name = 'index_saisie'),
    path('logout', views.logoutUser, name = 'logout'),
    path('pending/', views.pending, name = 'pending'),
    path('posted/', views.posted, name = 'posted'),
    path('approved/', views.approved, name = 'approved'),


    path('post_timetable/<str:pk>', views.post_timetable, name = 'post_timetable'),
    path('desactivate_timetable/<str:pk>', views.desactivate_timetable, name = 'desactivate_timetable'),
    path('send_mail/', views.send_mail, name = 'send_mail'),

    path('create_timetable/', views.generer_edt, name = 'create_timetable'),
    path('configure/', views.configure, name = 'configure'),

    #Entêtes
    path('headers/', views.headers, name = 'headers'),                                          
    path('create_header/', views.create_header, name = 'create_header'),
    path('available_ressources/', views.available_ressources, name = 'available_ressources'),                       #Creer un nouvel entete
    path('choose_header/<str:pk>', views.choose_header, name = 'choose_header'),


    path('view_timetable/<str:pk>', views.print_timetable, name = 'print_timetable'),           #afficher l'edt
    path('submit_timetable/<str:pk>', views.submit_timetable, name = 'submit_timetable'),       #Soumettre l'edt
    path('update_timetable/<str:pk>', views.update_timetable, name = 'update_timetable'),       #Modifier l'edt
    path('delete_timetable/<str:pk>', views.delete_timetable, name = 'delete_timetable'),       #Supprimer l'edt


    #Gestion des groupes d'étudiants
    path('create_group/', views.create_group, name = 'create_group'),
    path('update_group/<str:pk>', views.update_group, name = 'update_group'),
    path('delete_group/<str:pk>', views.delete_group, name = 'delete_group'),
    path('groups/', views.groups, name = 'groups'),


    #CRUD pour les ressources
    #path('create_instructor/', views.create_instructor, name = 'create_instructor'),
    path('update_instructor/<str:pk>', ressources_views.update_instructor, name = 'update_instructor'),
    #path('delete_instructor/<str:pk>', views.delete_instructor, name = 'delete_instructor'),

    #path('create_course/', views.create_course, name = 'create_course'),
    path('update_course/<str:pk>', ressources_views.update_course, name = 'update_course'),
    #path('delete_course/<str:pk>', views.delete_course, name = 'delete_course'),

   #path('create_meetingTime/', views.create_meetingTime, name = 'create_meetingTime'),
    path('update_meetingTime/<str:pk>', ressources_views.update_meetingTime, name = 'update_meetingTime'),
    #path('delete_meetingTime/<str:pk>', views.delete_meetingTime, name = 'delete_meetingTime'),

    #path('create_room/', views.create_room, name = 'create_room'),
    path('update_room/<str:pk>', ressources_views.update_room, name = 'update_room'),
    #path('delete_room/<str:pk>', views.delete_room, name = 'delete_room'),

    #path('create_department/', views.create_department, name = 'create_department'),
    path('update_department/<str:pk>', ressources_views.update_department, name = 'update_department'),
    #path('delete_department/<str:pk>', views.delete_department, name = 'delete_department'),

    #path('create_meetingTime/', views.create_meetingTime, name = 'create_meetingTime'),
    path('update_meetingTime/<str:pk>', ressources_views.update_meetingTime, name = 'update_meetingTime'),
    #path('delete_meetingTime/<str:pk>', views.delete_meetingTime, name = 'delete_meetingTime'),

    ]
    