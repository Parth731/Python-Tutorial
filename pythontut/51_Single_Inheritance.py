
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
        return cls(*string.split('-'))

    @staticmethod
    def printgood(string):
        print("This is a good " + string)
        # return "Thenga"

# code reusebility
class programmer(Employee):
    no_of_holiday = 56
    def __init__(self,name,salary,role,language):
        self.name = name
        self.salary = salary
        self.role = role
        # super(programmer, self).__init__(name,salary,role)
        self.language = language

    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is " \
               f"{self.role} The language are {self.language}"


harry = Employee("harry", 255,  "instructor")
rohan = Employee("Rohan", 2554, "student")

subham = programmer("shubham", 555, "Programmer",["python"])
ketan = programmer("ketan", 755, "Programmer",["python","cpp"])

# print(ketan.printdetails())
print(ketan.printprog())
print(ketan.no_of_holiday)

