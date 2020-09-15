

def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print("x => ",x)

a = 10
print(id(a))
update(10)
print("a => " ,a)


# mutable
def update_lst(x):
    print(id(x))
    print(x)
    x[1] = 25
    print(id(x))
    print("x => ",x)

lst = [10,20,30]
print(id(lst))
update_lst(lst)
print("lst => " ,lst)
