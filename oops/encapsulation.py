
 # it is binding of attributes and methods associated with them togather
 # it is binding of attributes and behaviours an Entity or Object togather

 #object has following characteristics
 # 1. identity => name given to an object or reference
 # 2. state => data in an object
 # 3. behaviours => actions or methods , generally used to change state of object

 # define a person enity
class Person:

    # constructor of class
    def __init__(self,name):
        self.__name = name
        self.__email = None
        self.__address = None

    # method of person
    def display(self):
        print("name:",self.__name,", email:",self.__email,", address:",self.__address)

  # updates an address attribute  of person
    def setAddress(self,address):
        self.__address = address

    def getName(self):
        return self.name

    def getAddress(self):
        return self.__address

    def setEamil(self,email):
        self.__email = email

    def getEmail(self):
        return self.__email



# lets create objects/instance of person

# first person object
p1 = Person()
p1.setEamil("ananta@example.com")
p1.setAddress("pune")


# first person object
p2 = Person()
p2.setAddress("mumbai")
p2.setEamil("rahul@example.com")


p1.display()
p2.display()

email=p2.getEmail()
print(email)



