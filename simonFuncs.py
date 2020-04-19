def main():
    print("Hello world")







#R7 function takes in a number as input, and prints the student(s) first and last name with matching GPAs

def searchGrade(number):
    for student in students:
        if student.grade == number:
            print("First Name: " + student.firstName)
            printf("Last Name: " + student.lastName)

#R9 function takes in a number and high/low. Returns student in same grade with lowest or highest GPA
def searchGrade(number, flag):
    studentsInSameGrade = []
    high = 0
    low = 0

    if flag == "L" or flag == "Low":
        # 'Low' was passed in, return lowest GPA student
        low = 1

    elif flag == "H" or flag == "High":
        # 'High' was passed in, return highest GPA student
        high = 1

    #Populate students with same grade
    for student in students:
        if student.grade == number:
            studentsInSameGrade.append(student)
    
    #Filter for either lowest or highest GPA
    for s in studentsInSameGrade:
        curr = studentsInSameGrade[0]
        if low == 1:
            if s.GPA < curr.GPA:
                curr = s
        elif high == 1:
            if s.GPA > curr.GPA:
                curr = s
    print("Name: " + curr.firstName + " " + curr.lastName)
    print("GPA: " + curr.GPA)
    print("Teacher: " + curr.teacherFirstName + " " + curr.teacherLastName)
    print("Bus: " + curr.bus)

if __name__ == "__main__":
    main()
