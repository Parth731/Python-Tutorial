'''
if have create two method same name and same no of parameter
& argument available in two different class is called method overriding
'''


class A:

    def show(self):
        print("In A Show")

class B(A):

    def show(self):
        print("In B Show")


a1 = B()
a1.show()