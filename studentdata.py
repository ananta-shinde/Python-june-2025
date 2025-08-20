studentList = [{'name': 'Ananta', 'rollNo': 12, 'marks': 60.0}, {'name': 'Rahul', 'rollNo': 45, 'marks': 12.0}]

def addNewStudent():
    student = {}
    student["name"] = input("enter student name")
    student["rollNo"] = int(input("enter roll no"))
    student["marks"] = float(input("enter marks in percentage"))
    studentList.append(student)

def printAllStudent():
    for x in studentList:
        print(x)

def searchStudentByRollNo(rollNo):
    for x in studentList:
        if(x["rollNo"] == rollNo):
            print(x)


def deleteStudentByRollno(rollno):
    for x in studentList:
        if(x["rollNo"] == rollno):
            studentList.remove(x)

deleteStudentByRollno(12)

print(studentList)




