from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
from saisie.decorators import unauthenticated_user, allowed_users, admins_only

from .models import *
from saisie.models import *
from .forms import *

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins', 'chef_service','vice-doyen'])
def index(request):  

    context = {}
    return render(request, 'ressources/index.html', context)

#deconnexion
def logoutUser(request):
    logout(request)

    return redirect('/')






#Liste des edt à valider
def timetables_to_approve(request):
	to_approve = TimeTable.objects.filter(status = 'soumis')
	context = {'to_approve': to_approve}

	return render(request, 'ressources/for_approvement.html', context)

#Valider un emploi du temps
def approve_timetable(request, pk):
	timetable = TimeTable.objects.get(id = pk)
	timetable.status = 'signe'
	timetable.save()
	return redirect('/ressources/')
	


    
#***********************************CRUD ressources****************************************************


def create_instructor(request):

	form = InstructorForm()

	if request.method == 'POST':
		#print('printing POST:', request.POST)

		form = InstructorForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/ressources/create_instructor/')

	context = {'form': form}

	return render(request, 'ressources/instructor_form.html', context)


def update_instructor(request, pk):
	instructor = Instructor.objects.get(id = pk)
	form = InstructorForm(instance = instructor)
	if request.method == 'POST':	

		form = InstructorForm(request.POST, instance = instructor)

		if form.is_valid():
			form.save()
			return redirect('/ressources/instructors/')


	context = {'form': form}
	return render(request, 'ressources/instructor_form.html', context)


def delete_instructor(request, pk):
	instructor = Instructor.objects.get(id = pk)

	if request.method == 'POST':	

		instructor.delete()
		return redirect('/ressources/instructors/')


	context = {'instructor': instructor}
	return render(request, 'ressources/delete_instructor.html', context)



def create_course(request):

	form = CourseForm()

	if request.method == 'POST':
		#print('printing POST:', request.POST)

		form = CourseForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/ressources/create_course/')

	context = {'form': form}

	return render(request, 'ressources/course_form.html', context)


def update_course(request, pk):
	course = Course.objects.get(id = pk)
	form = CourseForm(instance = course)
	if request.method == 'POST':	

		form = CourseForm(request.POST, instance = course)

		if form.is_valid():
			form.save()
			return redirect('/ressources/courses/')


	context = {'form': form}
	return render(request, 'ressources/course_form.html', context)

def delete_course(request, pk):
	course = Course.objects.get(id = pk)

	if request.method == 'POST':	

		course.delete()
		return redirect('/ressources/courses/')



	context = {'course': course}
	return render(request, 'ressources/delete_course.html', context)


def create_meetingTime(request):

	form = MeetingTimeForm()

	if request.method == 'POST':
		#print('printing POST:', request.POST)

		form = MeetingTimeForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/ressources/create_meetingTime/')

	context = {'form': form}

	return render(request, 'ressources/meetingTime_form.html', context)


def update_meetingTime(request, pk):
	meetingTime = MeetingTime.objects.get(id = pk)
	form = MeetingTimeForm(instance = meetingTime)
	if request.method == 'POST':	

		form = MeetingTimeForm(request.POST, instance = meetingTime)

		if form.is_valid():
			form.save()
			return redirect('/ressources/meetingTimes/')


	context = {'form': form}
	return render(request, 'ressources/meetingTime_form.html', context)

def delete_meetingTime(request, pk):
	meetingTime = MeetingTime.objects.get(id = pk)

	if request.method == 'POST':	

		meetingTime.delete()
		return redirect('/ressources/meetingTimes/')



	context = {'meetingTime': meetingTime}
	return render(request, 'ressources/delete_meetingTime.html', context)


def create_room(request):

	form = RoomForm()

	if request.method == 'POST':
		#print('printing POST:', request.POST)

		form = RoomForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/ressources/')

	context = {'form': form}

	return render(request, 'ressources/room_form.html', context)


def update_room(request, pk):
	room = Room.objects.get(id = pk)
	form = RoomForm(instance = room)
	if request.method == 'POST':	

		form = RoomForm(request.POST, instance = room)

		if form.is_valid():
			form.save()
			return redirect('/ressources/')


	context = {'form': form}
	return render(request, 'ressources/room_form.html', context)

def delete_room(request, pk):
	room = Room.objects.get(id = pk)

	if request.method == 'POST':	

		room.delete()
		return redirect('/ressources/rooms/')



	context = {'room': room}
	return render(request, 'ressources/delete_room.html', context)


def create_department(request):

	form = DepartmentForm()

	if request.method == 'POST':
		#print('printing POST:', request.POST)

		form = DepartmentForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/ressources/students/')

	context = {'form': form}

	return render(request, 'ressources/department_form.html', context)


def update_department(request, pk):
	department = Department.objects.get(id = pk)
	form = DepartmentForm(instance = department)
	if request.method == 'POST':	

		form = DepartmentForm(request.POST, instance = department)

		if form.is_valid():
			form.save()
			return redirect('/ressources/')


	context = {'form': form}
	return render(request, 'ressources/department_form.html', context)

def delete_department(request, pk):
	department = Department.objects.get(id = pk)

	if request.method == 'POST':	

		department.delete()
		return redirect('/ressources/students/')



	context = {'department': department}
	return render(request, 'ressources/delete_department.html', context)


def instructors(request):
	instructors = Instructor.objects.all()
	total_instructors = instructors.count()

	context = {'instructors': instructors, 'total_instructors': total_instructors}

	return render(request, 'ressources/instructors.html', context)

def courses(request):

	courses = Course.objects.all()
	total_courses = courses.count()

	context = {'courses': courses, 'total_courses': total_courses}

	return render(request, 'ressources/courses.html', context)


def rooms(request):

	rooms = Room.objects.all()
	total_rooms = rooms.count()

	context = {'rooms': rooms, 'total_rooms': total_rooms}

	return render(request, 'ressources/rooms.html', context)


def departments(request):

	departments = Department.objects.all()
	total_departments = departments.count()

	context = {'departments': departments, 'total_departments': total_departments}

	return render(request, 'ressources/departments.html', context)

def meetingTimes(request):

	meetingTimes = MeetingTime.objects.all()

	context = {'meetingTimes': meetingTimes}

	return render(request, 'ressources/meetingTimes.html', context)





#************************************Statistiques****************************************************
def charts(request):
	context = {}
	return render(request, 'ressources/charts.html', context)

#************************************ Fin Statistiques****************************************************
    
    