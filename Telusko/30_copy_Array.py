from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([6,1,9,3,2])
arr3 = arr1 + arr2 # vectorized operation
print(arr3)

print(sin(arr3))
print(cos(arr3))
print(log(arr3))
print(sqrt(arr3))
print(sum(arr3))
print(max(arr3))
print(concatenate([arr1,arr2]))

# both array is pointing same memory address is called as aliasing
arr1 = array([2,6,8,1,3])
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

# shallow copy
arr1 = array([2,6,8,1,3])
arr2 = arr1.view()
arr1[1] = 7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

# deep copy
arr1 = array([2,6,8,1,3])
arr2 = arr1.copy()
arr1[1] = 7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

