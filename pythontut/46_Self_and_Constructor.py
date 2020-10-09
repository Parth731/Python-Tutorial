
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


harry = Employee("harry", 455, "instructor")
rohan = Employee("Rohan", 4554, "student")

# harry.name = "harry"
# harry.salary = 455
# harry.role = "instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "student"

print(rohan.printdetails())
print(harry.printdetails())


