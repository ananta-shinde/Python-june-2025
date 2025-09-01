
class Teacher:

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__email = None
        self.__password = None


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


    def getId(self):
        return self.__id


    def setId(self, value):
        self.__id = value