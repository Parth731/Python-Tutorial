
# clear()
# The clear() method removes all the elements from a dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

# copy()
# The copy() method returns a copy of the specified dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)

# fromkeys()
# The fromkeys() method returns a dictionary with the specified keys and the specified value.The fromkeys() method returns a dictionary with the specified keys and the specified value.
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

# get()
# The get() method returns the value of the item with the specified key.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)

# items()
#  The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)

# keys()
# The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)

# pop()
# The pop() method removes the specified item from the dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

# popitem()
# The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)

# setdefault()
# The setdefault() method returns the value of the item with the specified key.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)

# update()
# The update() method inserts the specified items to the dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)

# values()
# The values() method returns a view object. The view object contains the values of the dictionary, as a list.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)
