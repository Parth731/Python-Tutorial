

def function_name_print(a, b, c, d,e):
    print(a,b,c,d,e)

# *args
# **kwargs
# *args can be change name
def funargs(normal, *argsname, **dic):
    print(type(argsname))
    print(normal)

    # print(args[0])
    for item in argsname:
        print(item)


    print("\nNow I would like to instroduce some of our heros")
    for key,value in dic.items():
        print(f"{key} is a {value}")

# function_name_print("Harry","Rohan","Skiif","Hammad","shivam")

har = ["Harry","Rohan","Skiif","Hammad","shivam","Parth"]
normal = "This is a normal"
dic = {
    "Rohan" : "Monitor",
    "Harry" : "fitness Instructor",
    "Programmer" : "Coordinator",
    "Parth" : "Cook"
}
# funargs(normal,*dic, **har)
funargs(normal,*har, **dic)


