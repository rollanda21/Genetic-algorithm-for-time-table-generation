from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
from .decorators import unauthenticated_user, allowed_users, admins_only

from .models import *
from ressources import views
from ressources.models import *
import random as rnd
import prettytable as prettytable
from .forms import *
from .filters import SeanceFilter


POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1
timeTable = None
header = None




# Create your views here.
#Choisir une entete
def choose_header(request, pk):
    
    #Les variables locales et globales
    global header  #Objet entête
    global data
    header = get_object_or_404(Header, id=pk)
    levels = []           #Les niveaux
    depts = []              #Les classes
    courses = []            #Les cours
    groups = []   #Les classes et les groupes
    all_courses = []
    
    #Dictionnaire qui associe à chaque niveau la liste des classes
    depts_per_level = {}
    sorted_groups = []
        
        
    #chargement de la variable data

    semester = header.semester      #Le semestre pour determiner quels cours choisir
    activity = header.activity      #Activité pour determiner quel groupes pour les classes
    all_levels = header.levels.all()   #Les niveaux pour filtrer préalablement les classes concernées
    
    #Lister les niveaux
    for level in all_levels:
        levels.append(level.level)
    

    print('************les niveaux choisis*************************')
    print(levels)
    print('************** Activité *******************')
    print(activity)
    print('**************** semestre *********************')
    print(semester)

    
    
    #Choix de toutes les classes en fonction des niveaux
    
    for i in range(0, len(levels)):
        depts += Department.objects.filter(level = levels[i])
        #depts_per_level[levels[i]] = Department.objects.filter(level = levels[i])
        
    
    #print(depts_per_level.values())
        

    #print('************** toutes les classes *****************')
    #print(depts)
    

    for i in range(0, len(depts)):
        all_courses += depts[i].courses.all()

    #print('************** tous les cours des semestres *****************')

    
    

    #Choix des cours
    for i in range(0, len(all_courses)):
        if all_courses[i].semester == semester:
            courses.append(all_courses[i])

    print(courses)
    data.set_courses(courses)

    
    
    #Filtrer les groupes en fonction de l'activité
    for i in range(0, len(depts)):
        group = depts[i].group_set.all()
        

        if group.count() > 0:

            for j in range(0, len(group)):
                if group[j].activity == activity:
                    groups.append(group[j])
                    
            
            del depts[i]
    
    print('***********************groupes triés avec succès***********************************')
    print(depts)
    print(groups)
    

    data.set_depts(depts)    

    return render(request, 'saisie/configure.html')


#Chargement des données
class Data:

    def __init__(self):
        
        self._depts = [] #Department.objects.all()
        self._rooms = Room.objects.all()
        self._meetingTimes = MeetingTime.objects.all()
        self._instructors = Instructor.objects.all()
        self._courses =  [] #Course.objects.all()        

    #Les getters

    def get_rooms(self): return self._rooms
    def get_instructors(self): return self._instructors
    def get_courses(self): return self._courses
    def get_depts(self): return self._depts
    def get_meetingTimes(self): return self._meetingTimes
    def get_numberOfClasses(self): return self._numberOfClasses

    #Les setters
    def set_rooms(self, rooms): self._rooms = rooms
    def set_instructors(self, instructors): self._instructors = instructors
    def set_courses(self, courses): self._courses = courses
    def set_depts(self, depts): self._depts = depts


#Creation des seances
class Schedule:
    def __init__(self):
        #global data
        self._data = data            #les données d'entré de l'algo
        self._classes = []               #Les seances
        self._numbOfConflicts = 0         #Le compteur de conflits
        self._fitness = -1              #la performance du modèle
        self._classNumb = 0             #Le nombre de seances de chaque classe
        self._isFitnessChanged = True    #evolution de la performance

    def get_classes(self):              #obtenir les seances
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self): return self._numbOfConflicts

    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness
    
    
    #******************** Initialisation des seances ************************************
    def initialize(self):
        depts = self._data.get_depts()
        courses = self._data.get_courses()
        
        for i in range(0, len(depts)):
            
            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])
                self._classNumb += 1
                newClass.set_room(data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])                
                #newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, len(data.get_meetingTimes()))])                
                newClass.set_instructor(courses[j].instructors.all()[rnd.randrange(0,len(courses[j].instructors.all()))])
                self._classes.append(newClass)

        #Une fois toutes les séances créées on affecte à chacune une plage horaire choisie parmi celles de sa salle 
        #On déclare ensuite les plage horaire assignées comme occupées
        seances = self._classes
        
        for i in range(0,len(seances)):
            room = seances[i].get_room()
            meeting_times = room.meeting_time.all()

            free_meeting_times = []
            for j in range(0, len(meeting_times)):
                mt = meeting_times[j]
                if mt.status == 'Libre':
                    free_meeting_times.append(mt)

            selected_mt = free_meeting_times[rnd.randrange(0,len(free_meeting_times))]
            seances[i].set_meetingTime(selected_mt)
            selected_mt.status = 'Occupé'            
                                  
        return self


#************ Revoir le calcul de performance et modifier le comportement à chaque confilt ********************
    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if (classes[i].get_room().capacity < classes[i].get_dept().size):
                self._numbOfConflicts += 1

            for j in range(0, len(classes)):
                if (j >= i):
                    if (classes[i].get_meetingTime().day == classes[j].get_meetingTime().time):                        
                        if (classes[i].get_room().name == classes[j].get_room().name):
                            self._numbOfConflicts += 1

                        if (classes[i].get_instructor().name == classes[j].get_instructor().name):
                            self._numbOfConflicts += 1

                        if (classes[i].get_dept().name == classes[j].get_dept().name):
                            self._numbOfConflicts += 1

        return 1 / ((1.0*self._numbOfConflicts + 1))


    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes)-1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes)-1])
        return returnValue

class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size): self._schedules.append(Schedule().initialize())

    def get_schedules(self): return self._schedules


class GeneticAlgorithm:
    def evolve(self, population): return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if (rnd.random() > 0.5): crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else: crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if(MUTATION_RATE > rnd.random()): mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop

class Class:
    def __init__(self, id, dept, course):
        self.id = id
        self.dept = dept
        self.course = course
        self.instructor = None
        self.meetingTime = None
        self.room = None

       
    def get_id(self): return self.id
    def get_dept(self): return self.dept
    def get_course(self): return self.course
    def get_instructor(self): return self.instructor
    def get_meetingTime(self): return self.meetingTime
    def get_room(self): return self.room
    def set_instructor(self, instructor): self.instructor = instructor
    def set_meetingTime(self, meetingTime): self.meetingTime = meetingTime
    def set_room(self, room):
        self.room = room
        

    def __str__(self):
        return str(self.dept.__str__()) + "," + str(self.course.__str__()) + "," + \
               str(self.room.__str__()) + "," + str(self.instructor.__str__()) + "," + str(self.meetingTime.__str__())

class DisplayMgr:
    def print_available_data(self):
        print("> All Available Data")
        self.print_dept()
        #self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()
    def print_dept(self):
        depts = data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(['dept', 'courses'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).courses.all()
            tempStr = "["
            for j in range(0, len(courses) - 1):
                tempStr += courses[j].__str__() + ", "
            tempStr += courses[len(courses) - 1].__str__() + "]"
            availableDeptsTable.add_row([depts.__getitem__(i).__str__(), tempStr])
        print(availableDeptsTable)
    
    def print_instructor(self):
        availableInstructorsTable = prettytable.PrettyTable([ 'instructor'])
        instructors = data.get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row([instructors[i].__str__()])
        print(availableInstructorsTable)

    

    
    def print_room(self):
        availableRoomsTable = prettytable.PrettyTable(['room #', 'max seating capacity'])
        rooms = data.get_rooms()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].__str__()), str(rooms[i].capacity)])
        print(availableRoomsTable)

    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable([ 'Meeting Time'])
        meetingTimes = data.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row([meetingTimes[i].time])
        print(availableMeetingTimeTable)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(['schedule #', 'fitness', '# of conflicts', 'classes [dept,class,room,instructor,meeting-time]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row([str(i+1), round(schedules[i].get_fitness(),3), schedules[i].get_numbOfConflicts(), schedules[i].__str__()])
        print(table1)
        
    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(['Class #', 'Dept', 'Course', 'Room', 'Instructor',  'Meeting Time'])
        for i in range(0, len(classes)):
            table.add_row([str(i+1), classes[i].get_dept().__str__(), classes[i].get_course().__str__() ,                           
                           classes[i].get_room().__str__() ,
                           classes[i].get_instructor().__str__() ,
                           classes[i].get_meetingTime().__str__() ])
        print(table)




#**********************************************les templates***********************************************
@login_required(login_url='login')
@allowed_users(allowed_roles=['admins', 'agent_saisie','vice-doyen'])
def index(request):

    timetables = TimeTable.objects.all()

    '''
    instructors = Instructor.objects.all()
	
    rooms = Room.objects.all()
    total_rooms = rooms.count()
    total_instructors = instructors.count()
    context = {'instructors': instructors, 'total_instructors': total_instructors, 'rooms': rooms, 'total_rooms': total_rooms}

    '''
    context = {'timetables': timetables}
    return render(request, 'saisie/index_saisie.html', context)


#************************ Configuration des données et de l'entete de l'emploi du temps ********************************

#Toutes les entetes
def headers(request):
    
	headers = Header.objects.all()
	#total_headers = headers.count()

	context = {'headers': headers}

	return render(request, 'saisie/headers.html', context)


#Creer une Entête de l'emloi du temps
def create_header(request):

	form = HeaderForm()

	if request.method == 'POST':

		form = HeaderForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/saisie/headers/')

	context = {'form': form}

	return render(request, 'saisie/header_form.html', context)



data = Data()




#Toutes les données disponibles pour un nouvel emploi du temps
def available_ressources(request):

     #Enseignants disponibles
    available_instructors = Instructor.objects.filter(status = 'Disponible')
    

    #Salles avec plages horaires libres
    rooms = Room.objects.all()
    

    total_rooms = rooms.count()
    total_instructors = available_instructors.count()

    context = {'available_instructors': available_instructors, 'total_rooms': total_rooms, 'rooms': rooms, 'total_instructors': total_instructors}
    
    return render(request, 'saisie/available_ressources.html', context)



#  Liste de toutes les données disponible pour créer un emploi du temps
def configure(request):

    #Enseignants disponibles
    available_instructors = Instructor.objects.filter(status = 'Disponible')
    

    #Salles avec plages horaires libres
    rooms = Room.objects.all()
    

    total_rooms = rooms.count()
    total_instructors = available_instructors.count()

    context = {'available_instructors': available_instructors, 'total_rooms': total_rooms, 'rooms': rooms, 'total_instructors': total_instructors}
    return render(request, 'saisie/configure.html', context)





#************************ Fin Configuration des données et de l'entete de l'emploi du temps *******************



classes = None
seances = []






#************************************* Gestion des emplois du temps *********************************************

def generer_edt(request):    

    #Affichage en ligne de commande
    displayMgr = DisplayMgr()

    displayMgr.print_available_data()
    generationNumber = 0
    print("\n> Generation # "+str(generationNumber))
    population = Population(POPULATION_SIZE)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    displayMgr.print_schedule_as_table(population.get_schedules()[0])
    geneticAlgorithm = GeneticAlgorithm()
    while (population.get_schedules()[0].get_fitness() != 1.0):
        generationNumber += 1
        print("\n> Generation # " + str(generationNumber))
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        displayMgr.print_generation(population)
        displayMgr.print_schedule_as_table(population.get_schedules()[0])
    print("\n\n")  

    
 

    #Affichage dans la page web
    if population.get_schedules()[0].get_fitness() == 1.0:
        
        schedule = population.get_schedules()[0]
        global classes
        classes = schedule.get_classes()

        
        
        global seances
        
        for classe in classes:
            seances.append(Seance.objects.create(activity='Cours Magistral',dept=classe.get_dept(), course=classe.get_course(), instructor=classe.get_instructor(), meetingTime=classe.get_meetingTime(), room=classe.get_room()))


        global timeTable
        timeTable = TimeTable.objects.create(semester='semestre1')

        for i in range(0, len(seances)):
            timeTable.classes.add(seances[i])    
   
    return render(request, 'saisie/index_saisie.html')




#Modifier un emploi du temps
def update_timetable(request, pk):
	timetable = TimeTable.objects.get(id = pk)
	form = TimeTableForm(instance = timetable)
	if request.method == 'POST':	

		form = TimeTableForm(request.POST, instance = timetable)

		if form.is_valid():
			form.save()
			return redirect('/saisie/')


	context = {'form': form}
	return render(request, 'saisie/timetable_form.html', context)



#Supprimer un emploi du temps
def delete_timetable(request,pk):
    timetable = TimeTable.objects.get(id = pk)
    if request.method == 'POST':
        timetable.delete()
        return redirect('/saisie/')

    context = {'timetable': timetable}
    return render(request, 'saisie/delete_timetable.html', context)


#Afficher un seul emploi du temps
def print_timetable(request, pk):
    timetable = get_object_or_404(TimeTable, id=pk)

    rooms = data.get_rooms()
    depts = data.get_depts()
    classes =  timetable.classes.all()
    days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    
    return render(request, 'saisie/afficher_edt.html', {'timetable':timetable, 'days': days, 'classes': classes, 'depts': depts, 'rooms': rooms, 'group':group})


# Liste les emplois du temps en cours
def pending(request):
     
    pending = TimeTable.objects.filter(status = 'en_attente')

    context = {'pending': pending}
    return render(request, 'saisie/pending.html', context)


#Liste des emplois du temps actifs
def posted(request):
    posted = TimeTable.objects.filter(status = 'actif')
    context = {'posted': posted}
    return render(request, 'saisie/posted.html', context)


#Les emplois du temps validés ou griffés
def approved(request):
    approved = TimeTable.objects.filter(status = 'signe')
    context = {'approved': approved}
    return render(request, 'saisie/approved.html', context)
    

#Soumettre un emploi du temps pour signature
def submit_timetable(request, pk):
    timetable = TimeTable.objects.get(id = pk)    
    timetable.status = 'soumis'
    timetable.save()
    return redirect('/saisie/')

    


#Publier un emploi du temps
def post_timetable(request, pk):
    timetable = TimeTable.objects.get(id = pk)    
    timetable.status = 'actif'
    timetable.save()
    return redirect('/saisie/')

    


#Desactiver un emploi du temps ***************************
def desactivate_timetable(request, pk):
    timetable = TimeTable.objects.get(id = pk)    
    timetable.status = 'desactive'
    timetable.save()
    return redirect('/saisie/')


#*******************************Fin gestion des groupes**************************************




#************************** Gestion des groupes *********************************************
def create_group(request):

	form = GroupForm()

	if request.method == 'POST':

		form = GroupForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/saisie/groups/')

	context = {'form': form}

	return render(request, 'saisie/group_form.html', context)


def update_group(request, pk):
	group = Group.objects.get(id = pk)
	form = GroupForm(instance = group)
	if request.method == 'POST':	

		form = GroupForm(request.POST, instance = group)

		if form.is_valid():
			form.save()
			return redirect('/saisie/groups/')


	context = {'form': form}
	return render(request, 'saisie/group_form.html', context)



def delete_group(request, pk):
	group = Group.objects.get(id = pk)


	if request.method == 'POST':	

		group.delete()
		return redirect('/saisie/groups/')



	context = {'group': group}
	return render(request, 'saisie/delete_group.html', context)



def groups(request):
    groups = Group.objects.all()
    departments = Department.objects.all()
    total_groups = groups.count()
    
    context = {'groups': groups, 'total_groups': total_groups, 'departments': departments}
    return render(request, 'saisie/groups.html', context)


#************************** fin Gestion des groupes *********************************************






#*************** Notifier les enseignants par mail*************************************

def send_mail(request):

    context = {}
    return render(request, 'saisie/send_mail.html', context)

def logoutUser(request):
    logout(request)

    return redirect('/')




    