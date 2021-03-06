from cmds import *

def parse_input(user_input):
   user_input = user_input.split()

   if len(user_input) > 1:
       t = user_input[1][0]
       if (t == '-'):
           print('')
           return

       t = user_input[1]
       if (t == '0' or t == '1' or t == '2' or t == '3' or t == '5' or t == '6'
            or t == '7' or t == '8' or t == '9'):
            y = int(t)
            if (user_input[0][0] != 'B' or user_input[0] != 'Bus' or
                    user_input[0] == 'G' or user_input[0] == 'Grade'):
                if (y < 1 or y == 5 or y == 0 or y > 6):
                    print("")
                    return


   # Check for S[tudent] search
   if(user_input[0] == "S" or user_input[0] == "Student"):
      if(len(user_input) == 2):
         studentLastname(user_input[1])
      if(len(user_input) == 3 and (user_input[2] == "B" or user_input[2] == "Bus")):
         lastNameBus(user_input[1])
      if(len(user_input) > 3):
         print("INPUT ERROR")

   # Check for T[eacher] search
   elif(user_input[0] == "T" or user_input[0] == "Teacher"):
      if(len(user_input) == 2):
         teacher(user_input[1])
      if(len(user_input) > 2):
         print("INPUT ERROR")

   # Check for B[us] search
   elif(user_input[0] == "B" or user_input[0] == "Bus"):
      if(len(user_input) == 2 and user_input[1].isdigit()):
         busRoute(int(user_input[1]))
      if(len(user_input) > 2):
         print("INPUT ERROR")

   # Check for G[rade] search
   elif(user_input[0] == "G" or user_input[0] == "Grade"):
      if(len(user_input) == 2):
          studentsInGrade(int(user_input[1]))
      if(len(user_input) == 3):
         if(user_input[2] == "L" or user_input[2] == "Low"):
            lowestGPA(int(user_input[1]))
         if(user_input[2] == "H" or user_input[2] == "High"):
            highestGPA(int(user_input[1]))
      if(len(user_input) > 3):
         print("INPUT ERROR")

   # Check for A[verage] search
   elif(user_input[0] == "A" or user_input[0] == "Average"):
      if(len(user_input) == 2 and user_input[1].isdigit()):
          usr_in = user_input[1]
          usr_in = int(usr_in.strip())
          average(usr_in)
      else:
         print("INPUT ERROR")

   # Check for I[nfo] search
   elif(user_input[0] == "I" or user_input[0] == "Info"):
      if(len(user_input) == 1):
         gradeRange()
      else:
         print("INPUT ERROR")

   # Check for C[lassroom]
   elif(user_input[0] == "C" or user_input[0] == "Classroom"):
      # if(len(user_input) == 2):
      #     studentsInGrade(int(user_input[1]))
      if(len(user_input) == 3):
         if(user_input[2] == "S" or user_input[2] == "Students"):
            classRoomStudents(int(user_input[1]))
         if(user_input[2] == "T" or user_input[2] == "Teachers"):
            classRoomTeachers(int(user_input[1]))
      else:
         print("INPUT ERROR")

   # Check for Te[aching] grade
   elif(user_input[0] == "Te" or user_input[0] == "Teaching"):
      if(len(user_input) == 2):
          teacherByGrade(int(user_input[1]))
      else:
         print("INPUT ERROR")

   # Check for R[eport] enrollment
   elif(user_input[0] == "R" or user_input[0] == "Report"):
      if(len(user_input) == 1):
         enrollment()
      else:
         print("INPUT ERROR")

    # Check for An[alytics]
   elif(user_input[0] == "An" or user_input[0] == "Analytics"):
          if(len(user_input) == 1):
             print("======== Analytics ========")
             print("Bus GPA average:")
             print(" ")
             busGpaAverage()
             print(" ")
             print(" ")
             print("Grade GPA average:")
             print(" ")
             gradeGpaAverage()
             print(" ")
             print(" ")
             print("Teacher GPA average:")
             print(" ")
             teacherGpaAverage()
             print(" ")
             print(" ")
          else:
             print("INPUT ERROR")

   elif(user_input[0] == "Q" or user_input[0] == "Quit"):
       return True
   else:
       print("INPUT ERROR")



def run_test_suite():
   f = open("tests.txt", "r")
   line = f.readline()
   quit = False

   # Check for data files
   #try:
   #   student_file = open("students.txt", "r")
   #except IOError:
   #   print("No 'students.txt' file found.")

   try:
      list_file = open("list.txt", "r")
   except IOError:
      print("No 'list.txt' file found.")

   try:
      teachers_file = open("teachers.txt", "r")
   except IOError:
      print("No 'teachers.txt' file found.")

   while(line):
      if(line[0] != "/" and line.strip()):
         quit = parse_input(line.strip())
         if(quit):
            print("Quitting.... (but not really)")
            quit = False
      line = f.readline()


def schoolSearch():
   quit = False

   print("Run Test Suite? [Y/N] (Case sensitive)")
   if(input() == "Y"):
      run_test_suite()
      return

   # Run prompt till quit is entered
   while(quit != True):
      # Prompt user
      print("")
      print("")
      print("S[tudent]:   <lastname> [B[us]]")
      print("T[eacher]:   <lastname>")
      print("B[us]:   <number>")
      print("G[rade]:   <number> [H[igh]|L[ow]]")
      print("A[verage]:   <number>")
      print("I[nfo]")
      print("C[lassroom]: <number> [S[tudents]]|[T[eachers]")
      print("Te[aching] grade: <number>")
      print("R[eport] enrollment")
      print("An[alytics]")
      print("Q[uit]")
      print("")
      user_input = input()
      quit = parse_input(user_input)

schoolSearch()
