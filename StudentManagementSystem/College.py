
class College:

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__address = None
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