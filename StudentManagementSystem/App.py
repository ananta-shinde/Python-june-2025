from College import College
from Department import Department

c1 = College()
c1.setId(100)
c1.setName("DIEMS")
# add new department
c1.addDepartment()

# add new student
c1.getDepartmentById(100).addStudent()
c1.getDepartmentById(100).addTeacher()


print(c1.getDepartmentById(100).getName())
print("******student list ********")
for student in c1.getDepartmentById(100).getStudentList():
    print(student.getName()," ",student.getEmail())
print("******teacher list ********")
for teacher in c1.getDepartmentById(100).getTeacherList():
    print(teacher.getName()," ",teacher.getEmail())


