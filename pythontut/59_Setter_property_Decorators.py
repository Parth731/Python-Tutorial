

class Employee:
    def __init__(self,fname,lname):                                                         # step2
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):                                                                      # step 4
        return f"this employee is {self.fname} and {self.lname}"

    @property
    def email(self):                                                                            # step 6,9,15
        if self.fname == None or self.lname == None:
            return "Email is not set. Please using the setter"
        return  f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self,string):                                                         # step 11
        print("setting now....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]    # this
        self.lname = names.split(".")[1]    # this

    @email.deleter
    def email(self):                                                                      # step 14
        self.fname = None
        self.lname = None



# note: when Employee constructor call, email is intization after than we can't
# change email so email property will used

hindustani_supporter = Employee("Hindustani","supporter")       # step 1: create object
# nikhil_raj_pandey = Employee("Nikhil", "raj")

print(hindustani_supporter.explain())                                         # step 3

# hindustani_supporter.email is use @property Attribute
print(hindustani_supporter.email)                                              # step 5

hindustani_supporter.fname = "US"                                           # step 7

# hindustani_supporter.email is use @property Attribute
print(hindustani_supporter.email)                                              # step 8


# i want to set email and also set email's attribute
# setting the attribute
hindustani_supporter.email = "this.that@codewithharry.com"      # step 10
print(hindustani_supporter.fname)
print(hindustani_supporter.lname)
print(hindustani_supporter.email)                                               # step 12

# deleting Attribute
del hindustani_supporter.email                                                   # step 13
print(hindustani_supporter.email)                                               # step 14
hindustani_supporter.email = "parth.selena@codewithharry.com"
print(hindustani_supporter.email)
