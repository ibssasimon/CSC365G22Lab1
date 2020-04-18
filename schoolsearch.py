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
    students = []
    populateData("students.txt")

    # Write the prompts for user input
    #writePrompts()

    # Ask for user input until user quits
    

   


def populateData(fileName):
    #Open the file
    f = open(fileName, "r")
    lines = f.readlines()

    

    for line in lines:
        studentRawData = line.strip()
        studentInfo = studentRawData.split(",")

        firstName = studentInfo[0]
    
        print(studentInfo)


        

    #print(lines)

if __name__ == "__main__":
    main()