# ******************************************************************************
# CSC 365 Spring 18 Von Dollen
# Geraldo Macias
# Luis Trujillo
# Josh Rivas
# ******************************************************************************
import pandas as pd


columns = ['StLastName', 'StFirstName', 'Grade', 'Classroom', 'Bus', 'Gpa']
students = pd.read_csv('list.txt', names=columns)

columns = ['TLastName', 'TFirstName', 'Classroom',]
teachers = pd.read_csv('teachers.txt', names=columns)

df = students.join(teachers.set_index('Classroom'), on='Classroom')

# ******************************************************************************
#                       lastNameBus
# Returns the information of the student depending on the student last name
# For each entry found, print the last name, first name and
# the bus route the student takes.
# ******************************************************************************
def lastNameBus(last):
    bus = df.loc[df['StLastName'] == last]
    j = bus.shape[0]
    if j == 0:
        print('')
        return
    for i in range(0, j):
        lName = bus.iloc[i][0]
        fName = bus.iloc[i][1]
        bNum = bus.iloc[i][4]
        print("%s,%s,%s" %(lName, fName, bNum))

# ******************************************************************************
#                       studentLastname
# Returns the information of the student depending on the student last name
# For each entry found, print the last name, first name, grade and classroom
# assignment for each student found and the name of their
# teacher (last and first name).
# ******************************************************************************
def studentLastname(last):
    bus = df.loc[df['StLastName'] == last]
    j = bus.shape[0]
    if j == 0:
        print('')
        return
    for i in range(0, j):
        lName = bus.iloc[i][0]
        fName = bus.iloc[i][1]
        gra = bus.iloc[i][2]
        cRoom = bus.iloc[i][3]
        tLast = bus.iloc[i][6]
        tFirst =bus.iloc[i][7]
        print('%s,%s,%s,%s,%s,%s' %(lName, fName, gra, cRoom, tLast, tFirst))

# ******************************************************************************
#                       teacher
# Search for teacher by last name
# For each entry found, print the last and the first name of the student.
# ******************************************************************************
def teacher(tlast):
    tlast = df.loc[df['TLastName'] == tlast]
    j = tlast.shape[0]
    if j == 0:
        print('')
        return
    for i in range(0, j):
        lName = tlast.iloc[i][0]
        fName = tlast.iloc[i][1]
        print('%s,%s' %(lName, fName))

# ******************************************************************************
#                       busRoute
# Returns the student list of a given bus route
# For each such entry, output the first and the last name of the student
# and their grade and classroom.
# ******************************************************************************
def busRoute(busNum):
    bus = df.loc[df['Bus'] == busNum].head()
    j = bus.shape[0]
    if j == 0:
        print('')
        return
    for i in range(0,j):
        fName = bus.iloc[i][1]
        lName = bus.iloc[i][0]
        gra = bus.iloc[i][2]
        cRoom = bus.iloc[i][3]
        print("%s,%s,%s,%s" %(fName, lName, gra, cRoom))

# ******************************************************************************
#                       studentsInGrade
# Returns all students within a certain grade
# For each entry, output the name (last and first) of the student
# ******************************************************************************
def studentsInGrade(grade):
    grade = df.loc[df['Grade'] == grade]
    j = grade.shape[0]
    if j == 0:
        print('')
        return
    for i in range(0,j):
        lName = grade.iloc[i][0]
        fName = grade.iloc[i][1]
        print("%s,%s" %(lName, fName))

# ******************************************************************************
#                       lowestGPA
# Given a specific grade, the student with the lowest gpa is returned
# If the L[ow] keyword is used in the command, find the entry in the
# students.txt file for the given grade with the lowest GPA.
# Report the contents of this entry (name of the student, GPA,
# teacher, bus route).
# ******************************************************************************
def lowestGPA(grade):
    grade = df.loc[df['Grade'] == grade]
    grade = grade.sort_values(by=['Gpa']).head(1)
    lName = grade.iloc[0][0]
    fName = grade.iloc[0][1]
    gp = grade.iloc[0][5]
    tlast = grade.iloc[0][6]
    tfirst = grade.iloc[0][7]
    bRoute = grade.iloc[0][3]
    print('%s,%s,%s,%s,%s,%s' %(lName, fName, gp, tlast, tfirst, bRoute))

# ******************************************************************************
#                       highestGPA
# Given a specific grade, the student with the highest gpa is returned
# If the H[igh] keyword is used in the command, find the entry in the
# students.txt file for the given grade with the highest GPA. Report the
# contents of this entry (name of the student, GPA, teacher, bus route).
# ******************************************************************************
def highestGPA(grade):
    grade = df.loc[df['Grade'] == grade]
    grade = grade.sort_values(by=['Gpa'], ascending=False).head(1)
    lName = grade.iloc[0][0]
    fName = grade.iloc[0][1]
    gp = grade.iloc[0][5]
    tlast = grade.iloc[0][6]
    tfirst = grade.iloc[0][7]
    bRoute = grade.iloc[0][3]
    print('%s,%s,%s,%s,%s,%s' %(lName, fName, gp, tlast, tfirst, bRoute))


# ******************************************************************************
#                       average
# When this instruction is issued your program shall perform the following
# actions:
#  Search the contents of the students.txt file for the entries where the
#   student’s grade matches the number provided in the instruction.
#  Compute the average GPA score for the entries found. Output the grade level
#   (the number provided in command) and the average GPA score computed.
# ******************************************************************************
def average(gradeLevel):
    avg = df.loc[df['Grade'] == gradeLevel]
    # Print variable value as well
    print("Grade:%d\t\tAverage GPA:%0.2f" %(gradeLevel, avg['Gpa'].mean()))

# ******************************************************************************
#                       info
# When this instruction is issued your program shall perform the following
# actions:
#  For each grade (from 0 to 6) compute the total number of students in that
#   grade.
#  Report the number of students in each grade in the format
# <Grade>: <Number of Students>
# sorted in ascending order by grade.
# ******************************************************************************
def gradeRange():
    for i in range(0, 7):
        info = df.loc[df['Grade'] == i]
        print("Grade:%d\t\tNumber of Students:%d" %(i,info.shape[0]))

# ******************************************************************************
#                       classRoomStudents
# Given a classroom number, list all students assigned to it.
# ******************************************************************************
def classRoomStudents(room):
    classroom = df.loc[df['Classroom'] == room]
    j = classroom.shape[0]
    if j == 0:
        print('')
    else:
        for i in range(0,j):
            sLast = classroom.iloc[i][0]
            sFirst = classroom.iloc[i][1]
            print("%s,%s" %(sLast,sFirst))

# ******************************************************************************
#                       classRoomTeachers
# Given a classroom number, find the teacher (or teachers) teaching in it.
# Need to functionalize
# ******************************************************************************
def classRoomTeachers(number):
    classroom = df.loc[df['Classroom'] == number]
    classroom = classroom.drop_duplicates('TLastName')
    j = classroom.shape[0]
    if j == 0:
        print('')
    else:
        for i in range(0,j):
            tLast = classroom.iloc[i][6]
            tFirst = classroom.iloc[i][7]
            print('%s,%s' %(tLast, tFirst))

# ******************************************************************************
#                       teacherByGrade
# Given a grade, find all teachers who teach it.
# ******************************************************************************
def teacherByGrade(grade):
    teacher = df.loc[df['Grade'] == grade]
    teacher = teacher.drop_duplicates('TLastName')
    j = teacher.shape[0]
    if j == 0:
        print('')
    else:
        for i in range(0,j):
            tLast = teacher.iloc[i][6]
            tFirst = teacher.iloc[i][7]
            print('%s,%s' %(tLast, tFirst))

# ******************************************************************************
#                       enrollment                         
# Report the enrollments broken down by classroom 
# (i.e., output a list of classrooms ordered by classroom number, 
# with a total number of students in each of the classrooms).
# ******************************************************************************
def enrollment():
    enroll = df.sort_values('Classroom', ascending=True)
    a = enroll['Classroom'].drop_duplicates().values
    for i in range(0, len(a)):
        frame = enroll[enroll['Classroom'] == a[i]]
        rows = len(frame)
        print('Classroom:%d\tNumber of students:%d' %(a[i], rows))

# ******************************************************************************
#                       busGpaAverage                         
# A report of each bus route and the average GPA of its students
# ******************************************************************************
def busGpaAverage():
    bga = df
    bga = bga.set_index('Bus').sort_index()
    bga = bga['Gpa'].mean(level=0)
    bga = bga.reset_index()
    bga = bga.sort_values(by='Gpa', ascending=False)
    for x in range(0, bga.shape[0]):
        b = bga.iloc[x][0]
        g = bga.iloc[x][1]
        print('Gpa_Avg:%0.2f\tBus:%d' %(g, b))
    print('Overall Gpa mean:%0.2f' %bga.Gpa.mean())
    print('Standard deviation:%0.2f' %bga.Gpa.std())

# ******************************************************************************
#                       gradeGpaAverage                         
# A report of each grade and the average GPA of its students
# ******************************************************************************
def gradeGpaAverage():
    gga = df
    gga = gga.set_index('Grade')
    gga = gga.sort_index()
    grades = gga['Gpa'].mean(level=0)
    grades = grades.reset_index()
    for x in range(0,7):
        if x == 0:
            print('Grade:0\tGpa:No students enrolled')
        elif x == 5:
            print('Grade:5\tGpa:No students enrolled')
        else:
            g = float(grades[grades['Grade'] == x].Gpa)
            print('Grade:%d\tGpa:%0.2f' %(x, g))
    print('Overall Gpa mean:%0.2f' %grades.Gpa.mean())
    print('Standard deviation:%0.2f' %grades.Gpa.std())

# ******************************************************************************
#                       teacherGpaAverage                         
# A report of each teacher and the average GPA of their students
# ******************************************************************************
def teacherGpaAverage():
    import matplotlib.pyplot as plt
    teach = df
    teach = teach.set_index('TLastName').sort_index()
    grades = teach['Gpa'].mean(level=0)
    grades = grades.reset_index()
    teach = teach.reset_index()
    teach = teach[['TLastName', 'TFirstName', 'Grade']]
    teach = teach.merge(grades)[['TLastName', 'TFirstName', 'Gpa', 'Grade']].drop_duplicates()
    teach = teach.sort_values(by='Gpa', ascending=False)
    for x in range(0, teach.shape[0]):
        t = teach.iloc[x][0]
        l = teach.iloc[x][1]
        g = teach.iloc[x][2]
        gr = teach.iloc[x][3]
        print('Gpa:%0.2f\tGrade:%d\t\tTeacher:%s,%s' %(g, gr, t, l))
    print('Overall Gpa mean:%0.2f' %teach.Gpa.mean())
    print('Standard Deviation:%0.2f' %teach.Gpa.std())

# ******************************************************************************
#                       testing block
# ******************************************************************************
#grade = 2
#print(df.head(10))
#lastNameBus('WOOLERY')
#studentLastname('WOOLERY')
#teacher('GAMBREL')
#busRoute(52)
#studentsInGrade(grade)
#lowestGPA(grade)
#highestGPA(grade)
#average(grade)
#gradeRange()
#classRoomTeachers(110)
#teacherByGrade(grade)
#enrollment()
#busGpaAverage()
#gradeGpaAverage()
#teacherGpaAverage()
