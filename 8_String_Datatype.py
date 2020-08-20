

mystr = "Harry is a good boy"

print(mystr)
#index is start 0
print(mystr[4])

# 4 is excluding
print(mystr[0:4])

# length count start from 0
print(len(mystr))

# positive index
# print(mystr[0:19])
# print(mystr[0:5:2])
# print(mystr[0::2])
# print(mystr[:5])
# print(mystr[0:])
# print(mystr[:])
# print(mystr[::])
# print(mystr[0:19:1])

#negative index
# mystr = "Harry is a good boy"
print(mystr[-1:0])
print(mystr[-4:])
print(mystr[-4:-1])
print(mystr[15:18])
print(mystr[::-1]) #reverse string
print(mystr[::-2])


#string function
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.endswith("bboy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"))



