
# Array has all value same type

# one way
# import array as arr
# arr.array()

from array import *

vals = array('i',[5,9,8,4,2])
print(vals.buffer_info())
print(vals.typecode)
# vals.reverse()
# print(vals)

# for x in range(len(vals)):
#     print(vals[x])

for x in vals:
    print(x)

# vals = array('u',['a','e','i'])
#
# for x in vals:
#     print(x)

newarray = array(vals.typecode,(a * a for a in vals))

for e in newarray:
    print(e,end=" ")
print()

i = 0
while i<len(newarray):
    print(newarray[i], end=" ")
    i += 1
