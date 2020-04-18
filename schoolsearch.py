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