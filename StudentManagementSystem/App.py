from College import College
from Department import Department

c1 = College()
c1.setId(100)
c1.setName("DIEMS")

d1 = Department()
d1.setId(1001)
d1.setName("CSE")

c1.setDepartment(d1)
c1.__departments

print(c1.getDepartmentslist()[0].getName())
