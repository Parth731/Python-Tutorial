
class Employee:
    no_of_leave = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "harry"
harry.salary = 455
harry.role = "instructor"
rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "student"

print(harry.salary, rohan.salary) #455 4554
print(harry.no_of_leave)    #8
print(rohan.no_of_leave)   #8
print(Employee.no_of_leave)   #8

Employee.no_of_leave = 9
print(Employee.no_of_leave)    #9
print(rohan.no_of_leave)   #9

# class object can not change value but only Employee class can change
# value (no_of_leave)
# instance se class variable can not be change
print(Employee.no_of_leave)    #9
print(rohan.__dict__)
rohan.no_of_leave = 10
print(rohan.__dict__)
print(Employee.no_of_leave) #9
