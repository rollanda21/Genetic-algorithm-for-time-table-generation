import django_filters
from .models import Seance

class SeanceFilter(django_filters.FilterSet):
    class Meta:
        model = Seance
        
        fields = ['dept', 'room']

'''
class TimeTableFilter(django_filters.FilterSet):
    class Meta:
        model = TimeTable
        fields = ['classes']

'''