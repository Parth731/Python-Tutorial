
# generator will give to iterator
# this is not normal function it is generator
def topten1():
    yield 1
    yield 2
    yield 3
    yield 4


values = topten1()
print(values.__next__())
print(values.__next__())

for x in values:
    print(x)


####################
def topten():
    n=1
    while n<=10:
        sequre = n * n
        yield sequre
        n = n +1



val = topten()

for x in val:
    print(x)

'''
thing about you are fetching thousand record from database may be all or 
may be process something fetch thousand all record in lowered memory
one value at time thousand record at time using the generator fetch the list 
one by one value fetch
'''
