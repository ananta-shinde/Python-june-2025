import os.path


class Student:

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__email = None
        self.__password = None


    def getId(self):
        return self.__id


    def setId (self, value):
        self.__id = value

    def getName(self):
        return self.__name

    def setName(self, value):
        self.__name = value

    def getEmail(self):
        return self.__email

    def setEmail(self, value):
        self.__email = value

    def getPassword(self):
        return self.__password

    def setPassword(self, value):
        self.__password = value

    def toString(self):
        return str(self.__id)+" "+self.__name+" "+self.__email+" "+self.__password


studentList = []

def loadStduentlist():
    if(os.path.isfile("StudentData.txt")):
        datafile = open("StudentData.txt","r")
        for line in datafile.readlines():
            data = line.split()
            student = Student()
            student.setId(int(data[0]))
            student.setName(data[1])
            student.setEmail(data[2])
            student.setPassword(data[3])
            studentList.append(student)


#add new student
def addNewStudent():
    student = Student()
    student.setId(len(studentList)+1)
    student.setName(input("enter student name:"))
    student.setEmail(input("enter student email:"))
    student.setPassword(input("enter student password :"))
    studentList.append(student)
    saveData()

def saveData():
    datafile = open("StudentData.txt","a")
    for student in studentList:
        datafile.write(student.toString()+"\n")

def displayStudentList():
    for student in studentList:
        print(student.toString())


loadStduentlist()
addNewStudent()
# addNewStudent()

displayStudentList()
# loadStduentlist()