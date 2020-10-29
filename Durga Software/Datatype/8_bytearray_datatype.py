x = [10,20,30,40,50]
b = bytearray(x)
for x in b : print(x)
b[0] = 100      # no error
for x in b : print(x)


# x = [10,256,30]     #error : byte must be range(0,256)
# b = bytearray(x)
# for x in b: print(x)