
x = [10,20,30,40,50]
b = bytes(x)
print(type(b))
print(b[0])
# b[0] = 100  #error : byte object does not support item assignment
print(b[-1])
for x in b: print(x)

