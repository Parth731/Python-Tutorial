
'''
type of method
- instance method
- class method
- static method

type of instance method
- Accessor Method
- mutator method
'''


class student:

    school = "Telusko"  #class variable

    def __init__(self,m1,m2,m3):
        self.m1 = m1            #instance variable
        self.m2 = m2
        self.m3 = m3


    def avg(self):      #instance  method
        return (self.m1 + self.m2 + self.m3)/3


    def get_m1(self):   #accessor method
        return self.m1

    def set_m1(self,value): #mutator method
        self.m1 = value

    #class method

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is a student class....in abc molude")



s1 = student(34,47,32)
s2 = student(89,32,12)

print(s1.avg())
print(s2.avg())

print(s1.getSchool())    #class method
print(student.getSchool())    #class method

s1.info()   #static method
student.info()  #static method
