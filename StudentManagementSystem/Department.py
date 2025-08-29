
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
