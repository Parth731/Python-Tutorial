
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






harry = Employee("harry", 455, "instructor")
rohan = Employee("Rohadn", 4554, "student")

# Employee.no_of_leaves = 89

harry.change_leave(34)


# print(Employee.no_of_leaves) #34
print(harry.no_of_leaves) #34




