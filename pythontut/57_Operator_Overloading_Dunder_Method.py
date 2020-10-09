'''
Dunder Method : __ se start ho ne wali or __ se end ho ne wali method ko
dunder method kehate hai

search: Mapping Operators to Functions

link : https://docs.python.org/3/library/operator.html

str is used object define
'''
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

    # Dunder method
    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        # return self.printdetails()
        return f"Employee ('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return self.printdetails()



emp1 = Employee("harry", 340, "Programmer")
emp2 = Employee("Rohan", 80, "cleaner")

# print(emp1 + emp2)
# print(emp1 / emp2)
print(emp1)
print(str(emp1))
print(emp1)
print(repr(emp1))

# when commented __str__ dunder method
print(str(emp1))

'''
output:

Employee ('harry', 340, 'Programmer')
Employee ('harry', 340, 'Programmer')
Employee ('harry', 340, 'Programmer')
Employee ('harry', 340, 'Programmer')
Employee ('harry', 340, 'Programmer')
'''

# when not commented __str__ dunder method
print(str(emp1))

'''
output:

The Name is harry. Salary is 340 and role is Programmer 
The Name is harry. Salary is 340 and role is Programmer 
Employee ('harry', 340, 'Programmer')
The Name is harry. Salary is 340 and role is Programmer 
The Name is harry. Salary is 340 and role is Programmer 
'''

