

'''
Iterable -> __iter__() or __getitem__()
Iterator  -> __next__()                             #generator
Iteration ->

generator : on the fly value generated
'''

def gen(n):
    for i in range(n):
        yield i


g =  gen(3)
print(g)            # <generator object gen at 0x000002A54E7F27B0>
print(g.__next__())     #0
# print(g.__next__())
# print(g.__next__())

# for x in g:
#     print(x.__next__()) # error : generator one time iterate

# iterable
h = "harry"
# h = 1234456     # int object is not iterable

# using for loop
# for c in h:
#     print(c)

print(h[0])         # h
print(iter(h))      #<str_iterator object at 0x000002A54CB7A940>
ier = iter(h)
print(ier.__next__())   #h
print(ier.__next__())   #a


# Quiz

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