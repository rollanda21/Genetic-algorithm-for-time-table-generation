from django.db import models

# Create your models here.


class Instructor(models.Model):

    STATUS = (
			('Disponible', 'Disponible'),
			('Indisponible', 'Indisponible'),
		)
    
    name = models.CharField(max_length=200, null=True, verbose_name='Nom')
    email = models.CharField(max_length=200, null=True, verbose_name='Adresse email')
    phone = models.CharField(max_length=200, null=True, verbose_name='Téléphone')
    grade = models.CharField(max_length=200, null=True, blank=True, verbose_name='Grade')
    status =  models.CharField(max_length=200, null=True, verbose_name='Statut', choices=STATUS, default='Disponible')

    def __str__(self):
        return self.name

    class Meta:
       ordering = ('name',)



#Ajouter ici un manytomanyfield relié à enseignant
class Course(models.Model):

    SEMESTER = (
			('Semestre 1', 'Semestre 1'),
			('Semestre 2', 'Semestre 2'),
		)


    code = models.CharField(max_length=200, null=True, verbose_name='Code EC')
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Intitulé')
    number_CM = models.FloatField(null=True, verbose_name='Nombre heures CM')
    number_TD = models.FloatField(null=True, verbose_name='Nombre heures TD')
    number_TP = models.FloatField(null=True, verbose_name='Nombre heures TP')
    coef = models.FloatField(null=True, blank=True, verbose_name='Nombre crédits')
    semester = models.CharField(max_length=200, null=True, verbose_name='Semestre', choices=SEMESTER, default='Semestre 1')
    instructors = models.ManyToManyField(Instructor, verbose_name='Enseignants')

    def __str__(self):
        return self.code

    class Meta:
       ordering = ('code',)


class MeetingTime(models.Model):

    TIME = (
			('7h-9h', '7h-9h'),            
            ('9h-11h', '9h-11h'),            
            ('11h-13h', '11h-13h'),           
            ('13h-15h', '13h-15h'),           
            ('15h-17h', '15h-17h'),            
            ('17h-19h', '17h-19h'),            
            ('19h-21h', '19h-21h'),          
            
		)


    DAY = (
			('Lundi', 'Lundi'),
			('Mardi', 'Mardi'),
            ('Mercredi', 'Mercredi'),
            ('Jeudi', 'Jeudi'),
            ('Vendredi', 'Vendredi'),
            ('Samedi', 'Samedi'),
            ('Dimanche', 'Dimanche'),
		)

    STATUS = (
			('Libre', 'Libre'),
			('Occupé', 'Occupé'),
		)



    day = models.CharField(max_length=200, verbose_name='Jour', null=True, choices=DAY)
    time = models.CharField(max_length=200, verbose_name='Plage horaire', null=True, choices=TIME)
    status =  models.CharField(max_length=200, null=True, verbose_name='Etat', choices=STATUS, default='Libre')

    def __str__(self):
        return f'{self.day} {self.time}'

    class Meta:
       ordering = ('day',)


class Room(models.Model):
    STATUS = (
			('Libre', 'Libre'),
			('Occupé', 'Occupé'),
		)
    
    name = models.CharField(max_length=200, null=True, verbose_name='Salle' )
    capacity = models.FloatField(null=True, verbose_name='Capacité')
    meeting_time = models.ManyToManyField(MeetingTime, verbose_name='Plages horaires')
    status =  models.CharField(max_length=200, null=True, verbose_name='Etat', choices=STATUS, default='Libre')
    

    def __str__(self):
        return self.name

    class Meta:
       ordering = ('name',)



class Faculty(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='Nom du département')

    def __str__(self):
        return self.name

    class Meta:
       ordering = ('name',)

class Department(models.Model): # cette classe représente en realite les classes comme MA3
    LEVEL = (
			('Niveau 1', 'Niveau 1'),
			('Niveau 2', 'Niveau 2'),
            ('Niveau 3', 'Niveau 3'),
            ('Niveau 4', 'Niveau 4'),
            ('Niveau 5', 'Niveau 5'),

		)



    name = models.CharField(max_length=200, null=True, verbose_name='Nom de la classe')
    faculty = models.ForeignKey(Faculty, on_delete = models.SET_NULL, null=True, verbose_name='Departement')
    courses =  models.ManyToManyField(Course, verbose_name='Cours')
    size = models.FloatField(null=True, verbose_name='Effectif')
    level    = models.CharField(max_length=200, null=True, choices=LEVEL, default='Niveau 1', verbose_name='Niveau')

    def __str__(self):
        return self.name

    class Meta:
       ordering = ('name',)




