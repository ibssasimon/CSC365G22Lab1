from arvindFuncs import searchInfo
from arvindFuncs import searchBus

# Class definition for student
class Student:
    def __init__(self, lastName, firstName, grade, classroom, bus, GPA, teacherLastName, teacherFirstName):
        self.lastName = lastName
        self.firstName = firstName
        self.grade = grade
        self.classroom = classroom
        self.bus = bus
        self.GPA = GPA
        self.teacherLastName = teacherLastName
        self.teacherFirstName = teacherFirstName



def main():
    #Populate data from text file
    students = populateData("students.txt")

    # Ask for user input until user quits
    while(1):
        
        # Write the prompts for user input
        writePrompts()

        args = input("Command: ").split()
        userInput = args[0]

        if(userInput == "Q" or userInput == "Quit"):
            break

        elif userInput == "S" or userInput == "Student":
            if(len(args) == 2):
                # 1 additional argument passed in
                searchStudent(args[2])
            elif(len(args) == 4 and (args[3] == "B" or args[3] == "Bus")):
                # 2 addtional arguments passed in
                # Might have to parse for "B" in bus
                # Arg 1 is "S", Arg 2 is <lastname>, Arg 3 is "B"
                searchStudentBus(args[1], args[3])
            else:
                print("Bad command")

        
        elif userInput == "T" or userInput == "Teacher":
            searchTeacher(args[])
        
        elif userInput == "G" or userInput == "Grade":
            searchGrade()

        elif userInput == "B" or userInput == "Bus":
            if len(args) == 2:
                searchBus(students, args[1])
            else:
                print("Incorrect use of command")

        elif userInput == "A" or userInput == "Average":
            searchAverage()

        elif userInput == "I" or userInput == "Info":
            searchInfo(students)
        else:
            print("Bad command")
            continue

        

    


def populateData(fileName):
    #Open the file
    f = open(fileName, "r")
    lines = f.readlines()
    students = []


    for line in lines:
        studentRawData = line.strip()
        studentInfo = studentRawData.split(",")

        lastName = studentInfo[0]
        firstName = studentInfo[1]
        grade = studentInfo[2]
        classroom = studentInfo[3]
        bus = studentInfo[4]
        GPA = studentInfo[5]
        teacherLastName = studentInfo[6]
        teacherFirstName = studentInfo[7]

        myStudent = Student(lastName, firstName, grade, classroom, bus, GPA, teacherLastName, teacherFirstName)
        students.append(myStudent)

    return students



def searchStudent():
    pass
    # If passed in bad parameters, print "Bad parameter", exit function


def searchTeacher():
    pass
    # If passed in bad parameters, print "Bad parameter", exit function

def searchGrade():
    pass
    # If passed in bad parameters, print "Bad parameter", exit function

def searchAverage():
    pass
    # If passed in bad parameters, print "Bad parameter", exit function



        

def writePrompts():
    print("\nS[tudent]: <lastname> [B[us]]")
    print("T[eacher]: <lastname>")
    print("B[us]: <number>")
    print("G[rade]: <number> [H[igh]|L[ow]]")
    print("A[verage]: <number>")
    print("I[nfo]")
    print("Q[uit]\n")


if __name__ == "__main__":
    main()