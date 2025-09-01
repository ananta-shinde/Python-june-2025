from Student import Student
from Teacher import Teacher
class Department:

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__students = []
        self.__teachers = []

    def getId(self):
        return self.__id

    def setId(self, value):
        self.__id = value

    def getName(self):
        return self.__name

    def setName(self, value):
        self.__name = value

    def getStudentList(self):
        return self.__students

    def getStudentById(self,id):
        for student in self.__students:
            if(student.getId() == id):
                return student
        return None

    def setStudent(self,student):
        self.__students.append(student)

    def addStudent(self):
        s = Student()
        s.setId(int(input("enter student id :")))
        s.setName(input("enter student name"))
        s.setEmail(input("enter student email :"))
        s.setPassword(input("enter student password :"))
        self.__students.append(s)

    def getTeacherList(self):
        return self.__teachers

    def getTeacherById(self, id):
        for teacher in self.__teachers:
            if (teacher.getId() == id):
                return teacher
        return None

    def setTeacher(self, teacher):
        self.__teachers.append(teacher)

    def addTeacher(self):
        t = Teacher()
        t.setId(int(input("enter teacher id :")))
        t.setName(input("enter teacher name"))
        t.setEmail(input("enter teacher email :"))
        t.setPassword(input("enter teacher password :"))
        self.__teachers.append(t)