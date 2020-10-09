
# 
# ls = []
# 
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)

# list Comprehensions
ls = [i for i in range(100) if i%3==0 ]
print(ls)

# dictionary Comprehensions
dict2 = { i : f"item{i}" for i in range(1001) if i%100==0}
dict1 = { i : f"item{i}" for i in range(5)}

# dictionary reverse
dict1 = {value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)

# set Comprehensions
dresses = {dress for dress in ["dress1", "dress1", "dress1",
                               "dress2","dress2","dress2"]}
print(dresses)
print(type(dresses))


# generator Comprehensions
# () -> this is perenthisis
even = (i for i in range(100) if i%2==0)
print(even.__next__())
print(even.__next__())
print(even.__next__())
print(even.__next__())




