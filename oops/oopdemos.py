from builtins import input

studentlist = []

def acceptStudentData():
    student = {}
    rollNo = int(input("enter rollno :"))
    name = input("enter name : ")
    marks = float(input("enter marks in percentage :"))
    student["rollNo"] = rollNo
    student["name"] = name
    student["marks"] = marks
    student["subjects"] = []
    for x in range(3):
        subjectDetails = {}
        subjectDetails["name"] = input("enter name of subject")
        subjectDetails["code"] = input("enter subject code")
        subjectDetails["maxMarks"] = float(input("enter max marks of subject"))
        subjectDetails["obtainedMarks"] = float(input("enter obtained marks"))
        student["subjects"].append(subjectDetails)
    return student

def addNewStudent(student):
    studentlist.append(student)


# s1 = {"rollno":200,"name": "Ananta","marks":75}
for x in range(3):
    s1 = acceptStudentData()
    addNewStudent(s1)

print(studentlist[0])





