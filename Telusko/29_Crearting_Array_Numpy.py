
from numpy import  *

arr = array([1,2,3,4,5.0],int)

print(arr.dtype)
print(arr)

# linspace()
arr = linspace(0,15,16)
print(arr)

#arange()
arr = arange(1,15,2)
print(arr)

# longspace()
arr = logspace(1,40,5)
print("%.2f" %arr[4])

# zero()
arr = zeros([5])
print(arr)

# ones()
arr = ones([5])
print(arr)