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
from. import views
from saisie import views as saisie_views

urlpatterns = [
    path('', views.index, name = 'index_requete'),

   
    path('print_timetable/<str:pk>', saisie_views.print_timetable, name = 'print_timetable'),    
    path('edt_instructor/', views.edt_instructor, name = 'edt_instructor'),
    path('edt_vice_doyen/', views.edt_vice_doyen, name = 'edt_vice_doyen'),
    path('request/', views.request, name = 'request'),
    path('logout', views.logoutUser, name = 'logout'),
    
    ]
    