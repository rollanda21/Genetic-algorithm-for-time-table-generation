import random as rnd 
from prettytable import PrettyTable

POPULATION_SIZE = 9
NUMBER_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1

class Data:
    '''data initialization '''
    ROOMS = [["R1", 25], ["R2", 45], ["R3", 35]]

    MEETINGTIMES = [["MT1", "MMF 09:00 - 10:00"],
                    ["MT2", "MMF 10:00 - 11:00"],
                    ["MT3", "TTM 09:00 - 10:30"],
                    ["MT4", "MMF 10:30 - 12:00"]]

    INSTRUCTORS = [["I1", "Dr James Web"],
                   ["I2", "Mr Mike Brown"],
                   ["I3", "Dr Steve Day"],
                   ["I1", "Mrs Jane Doe"]]

    def __init__(self):
        self._rooms = []; self._meetingTimes = []; self._instructors = []

        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))

        for i in range(0, len(self.MEETINGTIMES)):
            self._meetingTimes.append(MeetingTime(self.MEETINGTIMES[i][0], self.MEETINGTIMES[i][1]))

        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]))


        course1 = Course("C1", "325K", [self._instructors[0], self._instructors[1]], 25)
        course2 = Course("C2", "319K", [self._instructors[0], self._instructors[1], self._instructors[2]], 35,)
        course3 = Course("C3", "462K", [self._instructors[0], self._instructors[1]], 25)
        course4 = Course("C4", "464K", [self._instructors[2], self._instructors[3]], 30)
        course5 = Course("C5", "360C", [self._instructors[3]], 35)
        course6 = Course("C6", "303K", [self._instructors[0], self._instructors[2]], 45)
        course7 = Course("C7", "303L", [self._instructors[1], self._instructors[3]], 45)

        self._courses = [course1, course2, course3, course4, course5, course6, course7]

        dept1 = Departement("MATH", [course1, course3])
        dept2 = Departement("EE", [course2, course4, course5])
        dept3 = Departement("PHY", [course6, course7])

        self._depts = [dept1, dept2, dept3]
        self._numberOfClasses = 0

        for i in range(0, len(self._depts)):
            self._numberOfClasses += len(self._depts[i].getCourses())

    def getRooms(self):return self._rooms
    def getIntructors(self):return self._instructors
    def getCourses(self):return self._courses
    def getDepts(self):return self._depts
    def getMeetingTimes(self):return self._meetingTimes
    def getNumerOfClasses(self):return self._numberOfClasses



class Schedule:
    ''' constructeur'''
    def __init__(self):
        self._data = data
        self._classes = []
        self._numberOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def initialize(self):
        depts = self._data.getDepts()

        for i in range(0, len(depts)):
            courses = depts[i].getCourses()

            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])
                self._classNumb += 1
                newClass.setMeetingTime(data.getMeetingTimes()[rnd.randrange(0, len(data.getMeetingTimes()))])
                newClass.setRoom(data.getRooms()[rnd.randrange(0, len(data.getRooms()))])
                newClass.setInstructor(courses[j].getInstructors()[rnd.randrange(0, len(courses[j].getInstructors()))])
                self._classes.append(newClass)

        return self

    
    def getClasses(self):
        return self._classes

    def getFitness(self):
        return self._fitness

    def calculate_fitness(self):
        self._numberOfConflicts = 0
        classes = self.getClasses()

        for i in range(0, len(classes)):
            if(classes[i].getRoom().getCapacity() < classes[i].getCourse().getMaxNumberOfStudents()):
                self._numberOfConflicts += 1

            for j in range(0, len(classes)):
                if (j >= i):
                    if(classes[i].getMeetingTime() == classes[j].getMeetingTime() and classes[i].getId() != classes[j].getId()):
                        if (classes[i].getRoom() == classes[j].getRoom()):
                            self._numberOfConflicts += 1
                        if(classes[i].getInstructor() == classes[i].getInstructor()):
                            self._numberOfConflicts += 1
        return 1 / ((1.0*self._numberOfConflicts + 1)) 

    def __str__(self):
        returnValue = "" ""
        for i in range(0, len(self._classes)-1):
            returnValue += str(self._classes[i]) + ","

        returnValue += str(self._classes[len(self._classes)-1])
        return returnValue

class Population:
    '''  population from one generation to the next using crossover mutation '''
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        
        for i in range(0, size):
            self._schedules.append(Schedule().initialize()) 
            
    def getSchedules(self):
        return self._schedules


class GeneticAlgorithm:
    '''Algorithme génétique '''
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, population):
        crossover_population = Population(0)
        for i in range(NUMBER_OF_ELITE_SCHEDULES):
            crossover_population.getSchedules().append(population.getSchedules()[i])
        i = NUMBER_OF_ELITE_SCHEDULES

        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(population).getSchedules()[0]
            schedule2 = self._select_tournament_population(population).getSchedules()[0]
            crossover_population.getSchedules().append(self._crossover_schedule(schedule1, schedule2))

            i += 1

        return crossover_population

    def _mutate_population(self, population):
        for i in range(NUMBER_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.getSchedules()[i])
        return population
        

    def _crossover_schedule(self, schedule1, schedule2):
        crossover_schedule = Schedule().initialize()
        for i in range(0,len(crossover_schedule.getClasses())):
            if (rnd.random() > 0.5):
                crossover_schedule.getClasses()[i] = schedule1.getClasses()[i]
            else:
                crossover_schedule.getClasses()[i] = schedule2.getClasses()[i]

        return crossover_schedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()

        for i in range(0, len(mutateSchedule.getClasses())):
            if(MUTATION_RATE > rnd.random()):
                mutateSchedule.getClasses()[i] = schedule.getClasses()[i]

        return mutateSchedule

    def _select_tournament_population(self, population):
        tournament_population = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_population.getSchedules().append(population.getSchedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_population.getSchedules().sort(key = lambda x: x.getFitness(), reverse = True)
        return tournament_population        



class Course:
    
    ''' constructor '''
    def __init__(self, number, name, instructors, maxNumberOfStudents):
        self._number = number
        self._name = name
        self._maxNumberOfStudents = maxNumberOfStudents
        self._instructors = instructors

    ''' getters'''
    def getNumber(self):
        return self._number

    def getName(self):
        return self._name

    def getInstructors(self):
        return self._instructors
    
    def getMaxNumberOfStudents(self):
        return self._maxNumberOfStudents   

    ''' the string method'''
    def __str__(self): return self._name


class Instructor:
    '''  enseignant  '''
    def __init__(self, id, name):
        self._id = id
        self._name = name

    ''' getters '''
    def getId(self):
        return self._id
    
    def getName(self): 
        return self._name

    ''' the string method'''
    def __str__(self): return self._name


class Room:
    ''' salle '''
    def __init__(self, number, capacity):
        self._number = number
        self._capacity = capacity

    ''' getters '''
    def getNumber(self):
        return self._number

    def getCapacity(self):
        return self._capacity


class MeetingTime:
    '''  plage horaire'''

    def __init__(self, id, time):
        self._id = id
        self._time = time

    ''' getters '''
    def getId(self):
        return self._id
    
    def getTime(self): 
        return self._time
        

class Departement:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses

    ''' getters '''
    def getName(self): 
        return self._name

    def getCourses(self):
        return self._courses

    ''' the string method'''
    def __str__(self): return self._name


class Class:
    ''' cette classe représente une séance comportant une activité, une salle, un enseignant, une plage horiaire '''
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None

    ''' getters '''

    def getId(self):
        return self._id

    def getDept(self):
        return self._dept

    def getCourse(self):
        return self._course

    def getInstructor(self):
        return self._instructor

    def getMeetingTime(self):
        return self._meetingTime

    def getRoom(self):
        return self._room

    ''' setters '''

    def setInstructor(self, instructor):
        self._instructor = instructor

    def setMeetingTime(self, meetingTime):
        self._meetingTime = meetingTime

    def setRoom(self, room):
        self._room = room

    def __str__(self):
        return str(self._dept.getName()) + "," + str(self._course.getNumber()) + "," + \
            str(self._room.getNumber()) + "," + str(self._instructor.getId()) + "," + str(self._meetingTime.getId())  


    
data = Data()

        
