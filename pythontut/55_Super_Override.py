

class A:
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        # instance variable
        self.classvar1 = "Instance var in class A"
        self.special = "_special"


class B(A):
    classvar1 = "I am a class variable in class B"
    # pass

    def __init__(self):
        # super(B,self).__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super(B,self).__init__()    # here overriding to the class B to class A
        print(super().classvar1)    # I am a class variable in class A

a = A()

b = B()

# print(b.special)    # error without super() function
print(b.special)    # noerror with super() function # _special
print(b.special, b.var1,b.classvar1) # _special I am inside class A's constructor Instance var in class A


'''
output:

I am a class variable in class A
_special
_special I am inside class A's constructor Instance var in class A

'''

'''
b.classvar1 instance variable ko pehale class B me khojega nai milega 
to class A me jayega
'''