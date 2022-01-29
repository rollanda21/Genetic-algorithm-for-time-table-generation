from django.http import HttpResponse
from django.shortcuts import redirect


#*************** Pour forcer l'authentification de l'utilisateur **********************************************
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

  
#***************** Restriction des droits d'accès en fonction des utilisateurs *************************************************  
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)

            else:
                return HttpResponse('Accès refusé')

        return wrapper_func
    return decorator

#************************* Choix de la redirection pendant l'authentification
def admins_only(view_func):   
    def wrapper_func(request, *args, **kwargs):

        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'admins':
            return redirect('/')
            

        if group == 'agent_saisie':
            return redirect('/saisie/')

        if (group == 'chef_service'):
            return redirect('/ressources/')
        

        if group == 'vice-doyen':
            return redirect('/ressources/')

        if group == 'enseignants':
            return view_func(request, *args, **kwargs)

        if group == 'etudiants':
            return view_func(request, *args, **kwargs)

        

    return wrapper_func
    
            
            
