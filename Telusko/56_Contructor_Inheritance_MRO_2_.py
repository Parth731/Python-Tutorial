'''
MRO : Method resolution order
'''

'''

sub class can access all the feature of super class
but
super class can not access any feature of sub class

if you create object of sub class it will first try find init of sub class
if it is not found then it will call init of super class
'''

class A: # perent class

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1-> A working")

    def feature2(self):
        print("Feature 2 working")

class B: # child class

    def __init__(self):
        print("in B init")

    def feature1(self):
        print("Feature 1 -> B  working")

    def feature4(self):
        print("Feature 4 working")

# MRO: Module resolution Operator
class C(A,B):

    def __init__(self):     # using constructor
        super(C, self).__init__()
        print("in C init")

    def feature(self):      # using method
        super(C, self).feature1()


a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature1()
b1.feature4()
c1 = C()
c1.feature()




