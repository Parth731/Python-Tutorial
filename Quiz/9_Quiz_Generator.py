
def fact_fun(num):

    if num == 0 or num == 1:
        return 1

    return num * fact_fun(num-1)

def fact_gen(num):

   x = 0

   while x <=num:
       yield fact_fun(x)
       x = x + 1


# print(fact_fun(5))
n = int(input("Enter the int number for factorial: "))
print(fact_gen(n))
f = fact_gen(n)
print(f.__next__())
print(f.__next__())
print(f.__next__())

print("..................")

def fcibo_func(num):
    if num <= 1:
        return num
    else:
        return (fcibo_func(num - 1) + fcibo_func(num - 2))

def fcibo_gen(num):

    x = 0
    while x<=num:
        yield fcibo_func(x)
        x = x + 1


# fcibo_func(5)
n = int(input("Enter the int number for Fibonacci : "))
# print(fcibo_func(n))
f = fcibo_gen(n)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())