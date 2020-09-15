

def greet():
    print("Hello")
    print("Good Morning")


greet()

# add two number
def add(a,b):
    x = a +b
    return x

greet()
res = add(10,12)
print(res)


# mltivalue return
def add_sub(a,b):
    x = a +b
    y = a - b
    return x,y

greet()
res1,res2 = add_sub(10,12)
print(res1,res2)