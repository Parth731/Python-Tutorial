
 #
'''
== -> value equality -> two objects have the same value
    is -> referance equality -> two referance refer  to the same object
'''

a = [7,4,5]
b = a
print(b==a)
print(b is a)
b[0] = 0
print("a => ",a)
print("b => ",b)
c = a[:]    # reference equality
print(c)
print(c==a)
print(c==b)
print(c is a)
print(c is b)

#a ki  34 value aor b ki 34 value  same  hai  but  a and b ka object same nai hai
# a and b (a==b => true) value same hogi to true hoga but a and b(a is b => false) object same hoga to true  hoga
# javascript me "==" and "===" ka different same python me "==" and "is" ka different hai
a = [6,4,"34"]
b = [6,4,"34"]
print(a is b)   # false
print(a == b)