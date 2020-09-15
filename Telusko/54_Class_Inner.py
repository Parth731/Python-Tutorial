

# inner class
'''

note: you can create object of inner class inside the outer class

    or

note : you can create object of inner class outside the outer class
provided you use outer class name to call it
'''
class student:          # outer class
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:   # inner class

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = student('navin',2)
s2 = student('jenny',3)

s1.show()
s2.show()

lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))

lap1 = student.laptop()
lap1.show()


