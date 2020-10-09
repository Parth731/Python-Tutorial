
class Employee:
    var = 8
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
class player:
    var = 9
    no_of_game = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The Name is {self.name}. game is {self.game}"


class coolProgrammer(player, Employee):
    # var = 10
    language = "c++"

    def printLanguage(self):
        print(self.language)





harry = Employee("harry", 255,  "instructor")
rohan = Employee("Rohan", 2554, "student")

shubham = player("shubham", ["Cricket", ])
# karan = coolProgrammer("karan",8999, "CoolProgrammer")
karan = coolProgrammer("karan",["cricket"])
print(karan.printdetails())
karan.printLanguage()
print(karan.var)
