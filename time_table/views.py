from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from saisie.decorators import unauthenticated_user, allowed_users, admins_only

 


from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='etudiants')
            user.groups.add(group)

            messages.success(request, username + ' '  +'  crée avec succès'  )
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


#@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/requetes/')

        else:
            messages.info(request, 'Le nom d\'utilisateur ou le mot de passe est incorrect!')            
    context = {}
    return render(request, 'login.html', context)





