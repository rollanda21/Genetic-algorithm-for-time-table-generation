from django.db import models
from django.utils import timezone

# Create your models here.
from ressources.models import *


TAILLE_POPULATION = 9
NOMBRE_EDT_ELUS = 1
TAILLE_SELECTION_TOURNOI = 3
TAUX_MUTATION = 0.05




class Group(models.Model):

    ACTIVITIES = (
			('Cours Magistral', 'Cours Magistral'),
			('Travaux Dirigés', 'Travaux Dirigés'),
            ('Travaux Pratiques', 'Travaux Pratiques'),
            ('Contrôle Continu', 'Contrôle Continu'),
            ('Examens', 'Examens'),
            ('Soutenances', 'Soutenances'),
            ('Autre', 'Autre')

		)


    activity = models.CharField(max_length=200, blank=True, null=True, choices=ACTIVITIES, default='Cours Magistral', verbose_name='Activité')
    department = models.ForeignKey(Department, on_delete = models.SET_NULL, blank=True, null=True, verbose_name='Classe')
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nom du groupe')    
    size = models.FloatField(null=True, blank=True, verbose_name='Effectif') #effectif

    def __str__(self):
        return self.name




class Level(models.Model):

    LEVEL = (
			('Niveau 1', 'Niveau 1'),
			('Niveau 2', 'Niveau 2'),
            ('Niveau 3', 'Niveau 3'),
            ('Niveau 4', 'Niveau 4'),
            ('Niveau 5', 'Niveau 5'),

		)


    level = models.CharField(max_length=200, null=True, choices=LEVEL, default='Niveau 1')

    def __str__(self):
        return self.level


class Header(models.Model):
    
    ACTIVITIES = (
			('Cours Magistral', 'Cours Magistral'),
			('Travaux Dirigés', 'Travaux Dirigés'),
            ('Travaux Pratiques', 'Travaux Pratiques'),
            ('Contrôle Continu', 'Contrôle Continu'),
            ('Examens', 'Examens'),
            ('Soutenances', 'Soutenances'),
            ('Autre', 'Autre')

		)

    SEMESTERS = (
			('Semestre 1', 'Semestre 1'),
			('Semestre 2', 'Semestre 2'),

		)
    
    semester = models.CharField(max_length=200, blank=True, null=True, choices=SEMESTERS, default='Semestre 1', verbose_name='Semestre')
    activity = models.CharField(max_length=200, blank=True, null=True, choices=ACTIVITIES, default='Cours Magistral', verbose_name='Activité')
    academic_year = models.CharField(max_length=200, blank=True, null=True, verbose_name='Année académique')
    levels = models.ManyToManyField(Level, verbose_name='Niveaux')

    def __str__(self):
        return f'{self.semester} {self.activity} {self.academic_year}'


















class Seance(models.Model):


    ACTIVITIES = (
			('Cours Magistral', 'Cours Magistral'),
			('Travaux Dirigés', 'Travaux Dirigés'),
            ('Travaux Pratiques', 'Travaux Pratiques'),
            ('Contrôle Continu', 'Contrôle Continu'),
            ('Examens', 'Examens'),
            ('Soutenances', 'Soutenances'),
            ('Autre', 'Autre')

		)

    activity = models.CharField(max_length=200, blank=True, null=True, choices=ACTIVITIES, default='Cours Magistral', verbose_name='Activité')
    dept = models.ForeignKey(Department, on_delete = models.SET_NULL, null=True, verbose_name='Classe')
    course = models.ForeignKey(Course, on_delete = models.SET_NULL, null=True, verbose_name='Course')
    instructor = models.ForeignKey(Instructor, on_delete = models.SET_NULL, null=True, verbose_name='Enseignant')
    meetingTime = models.ForeignKey(MeetingTime, on_delete = models.SET_NULL, null=True,verbose_name='Plage horaire')
    room = models.ForeignKey(Room, on_delete = models.SET_NULL, null=True, verbose_name='Salle')

    def __str__(self):
        return f'{self.course} {self.room} {self.instructor} {self.dept} {self.meetingTime}'

    


class TimeTable(models.Model):
    STATUS = (
			('actif', 'actif'),
			('Desactive', 'desactive'),
            ('soumis', 'soumis'),
            ('signe', 'signe'),
            ('en_attente', 'en_attente'),


		)

    semester = models.CharField(max_length=200, blank=True, null=True)
    classes = models.ManyToManyField(Seance)
    date_created = models.DateTimeField(default= timezone.now, null=True)
    status =  models.CharField(max_length=200, null=True, choices=STATUS, default='en_attente')
    #header = models.ForeignKey(Header, on_delete = models.SET_NULL, null=True)

    class Meta:
       ordering = ('date_created',)


