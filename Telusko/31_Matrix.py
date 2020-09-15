
from numpy import *

arr1 = array([
                    [1,2,3,6,2,9],
                     [4,5,6,7,5,3]
                ])

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

# converting 2-D array to 1-D Array
arr2 = arr1.flatten()
print(arr2)
print()

# converting 1-D to  3-D Array
arr3 = arr2.reshape(3,4)
print(arr3)
print()

arr3 = arr2.reshape(2,2,3)
print(arr3)
print()

# matrix
# arr1 = array([
#             [1,2,3,6],
#             [4,5,6,7]
#         ])
# print(arr1)

m = matrix('1,2 ; 3,6 ; 4,5 ;6,7') # 4 row and 2 column
print(m)
print()
m = matrix('1,2 3; 6,4,5 ; 1,6,7') # 3 row and 3 column
print(m)
print()
print(diagonal(m))
print()
print(m.max())
print(m.min())


# matrix multiplication
m1 = matrix('1,2 3; 6,4,5 ; 1,6,7') # 3 row and 3 column
m2 = matrix('1,2 3; 6,4,5 ; 2,6,7') # 3 row and 3 column

m3 = m1 + m2
print()
print(m3)

m3 = m1 * m2
print()
print(m3)