from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Room)
admin.site.register(MeetingTime)
admin.site.register(Faculty)