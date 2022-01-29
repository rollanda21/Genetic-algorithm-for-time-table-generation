from django.forms import ModelForm
from .models import *

class InstructorForm(ModelForm):   #Formulaire des enseignants
	class Meta:
		model = Instructor
		fields = ['name', 'email','phone']


class CourseForm(ModelForm):  #Formulaire des cours
	class Meta:
		model = Course
		fields = '__all__'
		#fields = ['code', 'description', 'number_CM', 'number_TD', 'number_TP', 'instructors']

class MeetingTimeForm(ModelForm):   #Formulaire des plages horaires
	class Meta:
		model = MeetingTime
		fields = '__all__'

class RoomForm(ModelForm):  #Formulaire des salles
	class Meta:
		model = Room
		fields = ['name', 'capacity', 'meeting_time']

class DepartmentForm(ModelForm): #Formulaire des classes
	class Meta:
		model = Department
		fields = '__all__'

