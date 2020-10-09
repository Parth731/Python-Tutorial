
'''
public -
protected -
private -



'''


class Employee:
    no_of_leaves = 8
    _protec = 9
    __priv = 98

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
        return cls(*string.split('-'))

    @staticmethod
    def printgood(string):
        print("This is a good " + string)
        # return "Thenga  "

emp = Employee("harry",123,"Programmer")
print(emp._protec)
# print(emp.__private)
print(emp._Employee__priv) # it is namemanling conspact is their