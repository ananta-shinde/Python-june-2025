from abc import abstractmethod


# abstraction is mechanism of hidding implementation details and expose only necessary info

class Person:
    @abstractmethod
    def display(self):
       pass
    @abstractmethod
    def talk(self):
        pass
    @abstractmethod
    def eat(self):
        pass


class Student(Person):

    def display(self):
        print("displaying student")

    def talk(self):
        print("student talk in english")


class Teacher(Person):

    def display(self):
        print("teacher displays")



p1 = Person()
s1 = Student()
p1.display()
s1.display()

t1 = Teacher()
t1.display()



