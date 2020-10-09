

def function1():
    print("Subscribe now")

func2 = function1
del function1
func2()


# we can return function inside function
# def functionret(num):
#     if num == 0:
#         return print
#     else:
#         return sum

# a = functionret(1)
# print(a)

# we can pass function as argument
# def executor(func):
#     func("this")
#
# executor(print)


# decorators
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec
print("dec1 function")

@dec1
def who_is_harry():
    print("Harry is a good boy")

# who_is_harry = dec1(who_is_harry)
who_is_harry()


# smart division
def div(a,b):
    return a/b

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart_div(div)
print(div1(2,4))
