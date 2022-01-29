from django.shortcuts import render, redirect, redirect,get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from saisie.decorators import unauthenticated_user, allowed_users, admins_only
from saisie import views as saisie_views

from saisie.models import *
from ressources import views
from ressources.models import *
import random as rnd
import prettytable as prettytable

from saisie.filters import SeanceFilter


#from .models import *
#from .forms import *

# Create your views here.

@login_required(login_url='login')
@admins_only
def index(request):
    timetables = TimeTable.objects.all()

    
    active_timetables = timetables.filter(status = 'actif')
    
    context = {'active_timetables': active_timetables}
    return render(request, 'requetes/index_requetes.html', context)




def consulter_edt(request, pk):
    timetable = get_object_or_404(TimeTable, id=pk)
    
    depts = Department.objects.all()
    classes =  timetable.classes.all()
    days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    
    return render(request, 'requetes/consulter_edt.html', {'timetable':timetable, 'days': days, 'classes': classes, 'depts': depts})


def logoutUser(request):
    logout(request)

    return redirect('/')



@login_required(login_url='login')
def consulter_edt(request):
    context = {}
    return render(request, 'requetes/consulter_edt.html', context)

@login_required(login_url='login')
def edt_instructor(request):
    context = {}
    return render(request, 'requetes/edt_instructor.html', context)


@login_required(login_url='login')
def request(request):  

    context = {}
    return render(request, 'requetes/request.html', context)

@login_required(login_url='login')
def edt_vice_doyen(request):
    context = {}
    return render(request, 'requetes/edt_vice_doyen.html', context)
    