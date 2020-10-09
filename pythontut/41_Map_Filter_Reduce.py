
# ----------------------------- map() ------------------------

numbers = ["3","34","64"]

# for item in range(len(numbers)):
#     numbers[item] = int(numbers[item])

# using map function
numbers = list(map(int,numbers))

numbers[2] = numbers[2] + 1
print(numbers) # [3, 34, 65]
print(numbers[2]) # 65




def seq(a):
    return a*a


num = [2,3,5,6,76,3,3,2,1]
sequre = list(map(seq,num))

sequre1 = list(map(lambda x : x*x,numbers))
print(sequre1)
# [9, 1156, 4225]

sequre2 = list(map(lambda x : x*x,num))
print(sequre2)
# [4, 9, 25, 36, 5776, 9, 9, 4, 1]

# ------------ example 2 -----------------

def seqare(a):
    return a*a

def cube(a):
    return a*a*a

func = [seqare,cube]
num = [2,3,5,6,76,3,3,2,1]

for i in num:
    val = list(map(lambda x : x(i),func))
    print(val)

# --------------------------------- filter() -----------------------


lst1 = [1,2,3,4,5,6,7,8,9]

def is_sequre_5(num):
    return num>5

# qt_than_5 = list(filter(is_sequre_5,lst1))
qt_than_5 = list(filter(lambda x : x > 5,lst1))

print(qt_than_5)

# --------------------------------- reduce() -----------------------

from functools import reduce

lst1 = [1,2,3,4,5]
# num = 0
# for x in  lst1:
#     num = num + x
# print(num)

num = reduce(lambda x,y: x+y,lst1)
print(num)


