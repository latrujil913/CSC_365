# -*- coding: utf-8 -*-
# CSC 365 Sec01
# Von Dollen
# Lab 1 - Part 1 (Spring 18)
# Team : Geraldo Macias, Luis Trujillo, Joshua Rivas

import pandas as pd


# Create a dataframe by reading from a csv file
# Explicitly write all column names
columns = ['lastName', 'firstName', 'grade', 'classroom', 'bus', 'gpa',
            'tLastName', 'tFirstName']
df = pd.read_csv('students.txt', names=columns)

# ******************************************************************************
#                       lastNameBus
# Returns the information of the student depending on the student last name
# For each entry found, print the last name, first name and
# the bus route the student takes.
# ******************************************************************************
def lastNameBus(last):
    bus = df.loc[df['lastName'] == last]
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
    bus = df.loc[df['lastName'] == last]
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
    tlast = df.loc[df['tLastName'] == tlast]
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
    bus = df.loc[df['bus'] == busNum].head()
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
    grade = df.loc[df['grade'] == grade]
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
    grade = df.loc[df['grade'] == grade]
    grade = grade.sort_values(by=['gpa']).head(1)
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
    grade = df.loc[df['grade'] == grade]
    grade = grade.sort_values(by=['gpa'], ascending=False).head(1)
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
    avg = df.loc[df['grade'] == gradeLevel]
    # Print variable value as well
    print("Grade:%d\t\tAverage GPA:%0.2f" %(gradeLevel, avg['gpa'].mean()))

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
        info = df.loc[df['grade'] == i]
        print("Grade:%d\t\tNumber of Students:%d" %(i,info.shape[0]))

# ******************************************************************************
#                       testing block
# ******************************************************************************
grade = 2
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
