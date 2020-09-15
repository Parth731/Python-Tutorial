
#
def add(a,b):   #formal argument
    c = a+b
    print(c)

add(5,6)    # actual argument

'''
Actual argument 4 type
- position
- keyword
- default
- variable length

'''


def person(name,age=18):   #formal argument
    print(name)
    print(age)

# person("navin",28)    # actual argument
person(28,"Navin")  # position
# person(age=28,name="Navin") #keyword
# person("Navin",28) #default

# variable length
def add1(*b):
    # print(a)
    print(b)
    c = 0

    for x in b:
        c = c + x
    print(c)



add1(5,6,34,48) #variable length
