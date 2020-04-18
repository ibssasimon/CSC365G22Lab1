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

    # Write the prompts for user input
    writePrompts()

    # Ask for user input until user quits
    while(1):
        
        args = input().split()
        userInput = args[0]

        if(userInput == "Q" or userInput == "Quit"):
            break

        elif userInput == "S" or userInput == "Student":
            if(len(args) == 2):
                # 1 additional argument passed in
                searchStudent()
            elif(len(args) == 3):
                # 2 addtional arguments passed in
                # Might have to parse for "B" in bus
                searchStudent()

        
        elif userInput == "T" or userInput == "Teacher":
            searchTeacher()
        
        elif userInput == "G" or userInput == "Grade":
            searchGrade()

        elif userInput == "B" or userInput == "Bus":
            searchBus()

        elif userInput == "A" or userInput == "Average":
            searchAverage()

        elif userInput == "I" or userInput == "Info":
            searchInfo()
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

def searchBus():
    pass
    # If passed in bad parameters, print "Bad parameter", exit function

def searchAverage():
    pass
    # If passed in bad parameters, print "Bad parameter", exit function

def searchInfo():
    pass
    # If passed in bad parameters, print "Bad parameter", exit function



        

def writePrompts():
    print("S[tudent]: <lastname> [B[us]]")
    print("T[eacher]: <lastname>")
    print("B[us]: <number>")
    print("G[rade]: <number> [H[igh]|L[ow]]")
    print("A[verage]: <number>")
    print("I[nfo]")
    print("Q[uit]")


    #print(lines)

if __name__ == "__main__":
    main()