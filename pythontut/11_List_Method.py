
#append()
#The append() method appends an element to the end of the list.
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#clear()
#The clear() method removes all the elements from a list.
fruits.clear()
print(fruits)

#copy()
#The copy() method returns a copy of the specified list.
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

#count()
#The count() method returns the number of elements with the specified value.
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

#extend()
# The extend() method adds the specified list elements (or any iterable) to the end of the current list.
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

#index()
#The index() method returns the position at the first occurrence of the specified value.
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

#insert()
# The insert() method inserts the specified value at the specified position.
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#pop()
#The pop() method removes the element at the specified position.
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#remove()
#The remove() method removes the first occurrence of the element with the specified value.
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#reverse()
# The reverse() method reverses the sorting order of the elements.
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#sort()
# The sort() method sorts the list ascending by default.
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)