from functools import reduce

nums = [3,2,6,8,4,6,2,9]
print(nums)

# filter
# def is_even(n):
#     return n%2==0

# evens = list(filter(is_even,nums))
evens = list(filter(lambda n: n%2==0,nums))
print(evens)

# map
# def update(n):
#     return n + 2

# double = list(map(update,nums))
double = list(map(lambda n : n+2,nums))
print(double)

# reduce
# def add(a,b):
#     return a+b



# sum = reduce(add,nums)
sum = reduce(lambda a,b : a+b,nums)

print(sum)