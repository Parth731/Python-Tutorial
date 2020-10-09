
class Employee:
    no_of_leaves = 8

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        # print(self)
        return f"The Name is {self.name}. Salary is {self.salary} and role is " \
               f"{self.role} "


    @classmethod
    def change_leave(cls,newLeave):
        cls.no_of_leaves = newLeave

    @classmethod
    # class method as Alternative constructor
    def from_dash(cls,string):
        # params = string.split('-')
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split('-'))




harry = Employee("harry", 455,  "instructor")
rohan = Employee("Rohan", 4554, "student")

# Alternative constructor
parth = Employee.from_dash("Parth-400-student")

print(parth.salary)

# Employee.no_of_leaves = 89
# harry.change_leave(34)


# print(Employee.no_of_leaves) #34

print(harry.no_of_leaves) #34



