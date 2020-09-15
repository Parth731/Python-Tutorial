
# a = 5
# b = "Hello"
# print(a + b)    # synthetic sugar

# a = 5
# b = 6
# print(a+b)
# print(int.__add__(a,b))


# a = '5'
# b = '6'
# print(a+b)
# print(str.__add__(a,b))

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = student(m1,m2)
        return m3

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        m3 = student(m1, m2)
        return m3

    def __mul__(self, other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        m3 = student(m1, m2)
        return m3

    def __gt__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        if m1 > m2:
            return True
        else:
            return False

    def __str__(self):
        # return self.m1, self.m2
        return "{} {}".format(self.m1,self.m2)



s1 = student(87,68)
s2 = student(60,65)

s3 = s1 + s2
# s3 = s1 - s2
# s3 = s1 * s2

print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

a =9
print(a)
# print(s1)
'''
printing object doesn't matter int or div behind 
the sens calling the method is called str
'''
print(a.__str__())
print(s1.__str__())

