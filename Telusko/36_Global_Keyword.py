
a = 10  # global
print(id(a))

def something():
    a =15   #local
    x = globals()['a']
    print(id(x))
    print("in fun",a)

    globals()['a'] = 5

something()
print("outside",a)