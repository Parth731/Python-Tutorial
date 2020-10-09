
# f-strings

# error
# me = "harry"
# my = "parth"
# a = "this is %s"%me

#error
# me = "harry"
# a1 = 3
# my = "parth"
# a = "this is %s %d %s nwdkjwkdkkwkdbkbkdbsbbdsb" %(me,a1,my)
# print(a)


# me = "harry"
# a1 = 3
# my = "parth"
# a = "This is {1} and {0}"
# b = a.format(me,my)
# print(b)

# fstring
import math
me = "harry"
a1 = 3
my = "parth"
# a= f"this is {a1}, {me} and {my} "
a= f"this is {a1}, {me} and {math.cos(65)}"
print(a)

i = "I"
l = "Love"
y = "You"
b = "Bro"
a = f"{i} {l} {y} {b}, thanks for this tutorial"
print(a)