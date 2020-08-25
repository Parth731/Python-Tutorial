
grocery = ["Harpic","vim bar","deodrant", "bhindi", "Lollypop",56]

print(grocery)      #list
print(grocery[5])   #56
# print(grocery[6])

number = [2,7,9,11,3]
print(number)       #[2,7,9,11,3]
print(number[2])    #9
# print(number.sort())    #none

#sort number
number.sort()
print(number)          #[2, 3, 7, 9, 11]

#reverse number
# number.reverse()
# print(number)

#sciling
print(number[0:5])      #[2, 3, 7, 9, 11]
print(number[:5])       #[2, 3, 7, 9, 11]
print(number[:])        #[2, 3, 7, 9, 11]
print(number[1:])       #[3, 7, 9, 11]
print(number[1:4])      #[3, 7, 9]

#extened slice
print(number[::3])      #[2, 9]
print(number[::-3])     #reverse number then count[11, 3]
print(number[1:5:2])    #[3, 9]
print(len(number))      #5
print(max(number))      #11
print(min(number))      #2

number = [2,7,9,11,3]

number.append(7)
print(number)   #[2, 7, 9, 11, 3, 7]

number.insert(2,55)
print(number)   #[2, 7, 55, 9, 11, 3, 7]


number.remove(9)
print(number)   #[2, 7, 55, 11, 3, 7]

number.pop()
print(number)   #[2, 7, 55, 11, 3]


print(number[1])
number[1] = 60
print(number)

#mutable - can change
#immutable - can not change
#list is mutable
#tuple is immutables

tp = (1,2,3,4,5)
print(tp)
# tp[1] = 90
print(tp)   #tuple is immutable (1,2,3,4,5)

tp = (1,)
print(tp)   #(1)

#swaping two number
a = 1
b = 3
a,b = b,a
print(a,b)
















