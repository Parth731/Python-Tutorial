#
# i = 10  # global scope
# def function1(n):
#
#     # i = 5   #local scope
#     # i = i + 45    #error
#
#     global i
#     i = i + 40
#     m = 8
#     print(i, m)
#     print(n,"I have printed")
#
#
# function1("This is me")
# print(i)
x = 89
def Harry():
    x = 20
    # print(x)
    def rohan():
        global x
        x = 88
    print("Before calling rohan()",x)
    rohan()
    print("after calling rohan()",x)

Harry()
print(x)