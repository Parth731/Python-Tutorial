

# lambda function or anonymous function

# def add(a,b):
#     return a+b

# add = lambda x,y : x+y
#
# print(add(10,20))

########################

# def lst_first(a):
#     return a[0]

# lst_first = lambda a : a[0]

lst = [[1, 14], [5, 6], [3,23]]
# lst.sort(key=lst_first)
# lst.sort(key=lambda x:x[0])
lst.sort(key=lambda x:x[1])
print(lst)