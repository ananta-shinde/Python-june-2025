
from College import College

collegeList = []

def getCollegeById(id):
    for college in collegeList:
        if(college.getId() == id):
            return college
        else:
            return None
def registerCollege():
    college = College()
    college.setId(len(collegeList)+1)
    college.setName(input("enter college name :"))
    college.setEmail(input("enter college email id :"))
    college.setPassword(input("enter college password :"))
    college.setAddress(input("enter address :"))
    collegeList.append(college)

def loginAsCollege():
    email = input("enter college email :")
    paasword = input("enter password :")
    for college in collegeList:
        if(college.getEmail() == email):
            if(college.getPassword() == paasword):
                return college
            else:
                print("invalid creds")
        else:
            print("no user found")

    return None

def loginAsTeacher():
    collegeId = input("enter your college Id :")
    departmentId = input("enter your department id :")
    email = input("enter email :")
    paasword = input("enter password :")
    college = getCollegeById(collegeId)
    if(college != None):
        for teacher in college.getDepartmentById(departmentId).getTeacherList():
            if(teacher.getEmail() == email):
                if(teacher.getPassword() == paasword):
                    return teacher
                else:
                    print("invalid creds")
            else:
                print("no user found")

    else:
        print("invalid details")

    return None

def loginAsStudent():
    collegeId = input("enter your college Id :")
    departmentId = input("enter your department id :")
    email = input("enter email :")
    paasword = input("enter password :")
    college = getCollegeById(collegeId)
    if(college != None):
        for student in college.getDepartmentById(departmentId).getStudentList():
            if(student.getEmail() == email):
                if(student.getPassword() == paasword):
                    return student
                else:
                    print("invalid creds")
            else:
                print("no user found")

    else:
        print("invalid details")

    return None



print("******** welcome to student management system ***********")
print("select from following menu :")
print("1. Register as new college"," 2. login as college ")
print("3. login as Teacher ","4. login as Student ")
choice = int(input("enter your choice :"))
if(choice < 1 and choice > 4):
    print("invalid choice, try again")
else:
    if(choice == 1):
        registerCollege()
    elif(choice == 2):
        loginAsCollege()
    elif(choice == 3 ):
        loginAsTeacher()
    elif (choice == 4):
        loginAsStudent()
