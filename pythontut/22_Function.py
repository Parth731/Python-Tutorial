
a =9
b = 8
c = sum((a,b))  #built in function
print(c)

def function():
    print("Hello, You are in function")

print(function())

def function1(a,b):
    print("Hello, You are in function", a+b)

function1(10,12)


def function2(a,b):
    average = (a+b)/2
    print(average)
    return average


v = function2(10,12)
print(v)

##################  (doc String)##################

def function2(a,b):
    ''' This is a function which will calculate average of two numbers
        This function does not work for three numbers'''
    average = (a+b)/2
    # print(average)
    return average

print(function2.__doc__)
v = function2(10,12)
print(v)



