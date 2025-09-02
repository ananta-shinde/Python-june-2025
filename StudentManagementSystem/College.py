from Department import Department
class College:

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__address = None
        self.__email = None
        self.__password = None
        self.__website = None
        self.__departments = []

    def getId(self):
        return self.__id

    def setId(self,value):
        self.__id = value

    def getName(self):
        return self.__name

    def setName(self, value):
        self.__name = value

    def getAddress(self):
        return self.__address

    def setAddress(self, value):
        self.__address = value

    def getWebsite(self):
        return self.__website

    def setAddress(self, value):
        self.__website = value

    def getDepartmentslist(self):
        return self.__departments

    def setDepartment(self,dept):
        self.__departments.append(dept)

    def addDepartment(self):
        d = Department()
        d.setId(int(input("enter department id :")))
        d.setName(input("enter department name :"))
        self.__departments.append(d)

    def getDepartmentById(self,id):
        for d in self.__departments:
            if (d.getId() == id):
                return d
        return None

    def getEmail(self):
        return self.__email

    def setEmail(self, value):
        self.__email = value

    def getPassword(self):
        return self.__password

    def setPassword(self, value):
        self.__password = value