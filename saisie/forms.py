from django.forms import ModelForm
from .models import *
from ressources.forms import *

class GroupForm(ModelForm):
	class Meta:
		model = Group
		fields = '__all__'


class TimeTableForm(ModelForm):
	class Meta:
		model = TimeTable
		fields = '__all__'

class SeanceForm(ModelForm):
	class Meta:
		model = Seance
		fields = '__all__'

class HeaderForm(ModelForm):
	class Meta:
		model = Header
		fields = '__all__'