
'''
object Introspection means object kebareme research karana or
janakari lena(object researching)
'''

class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"this employee is {self.fname} and {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please using the setter"
        return  f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self,string):
        print("setting now....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("Skill","F")
print(skillf.email)
print(type(skillf))
print(type("this is a strings"))
print(id("this is a strings"))
print(id("this that"))

print(dir("this is a strings"))
print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))
