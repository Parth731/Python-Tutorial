
s = set()
print(type(s))

# s_from_list = set([1,2,3,4,])
# print(s_from_list)
# print(type(s_from_list))

# set is maintain unique value
s.add(1)
s.add(1)

s1 = s.union({1,2,3,4})
print(s, s1)

s1.remove(4)
print(s1)

s1 = s.intersection({1,2,3})
print(s, s1)

#add()
# The add() method adds an element to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

#clear()
# The clear() method removes all elements in a set.
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

# copy()
# The copy() method copies the set.
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

# difference()
# The difference() method returns a set that contains the difference between two sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

# difference_update()
# The difference_update() method removes the items that exist in both sets.
# The difference_update() method is different from the difference() method, because
# the difference() method returns a new set, without the unwanted items, and
# the difference_update() method removes the unwanted items from the original set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

# discard()
# The discard() method removes the specified item from the set.
# This method is different from the remove() method, because
# the remove() method will raise an error if the specified item does not exist,
# and the discard() method will not.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

# intersection()
# The intersection() method returns a set that contains the similarity between two or more sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)


# intersection_update()
# The intersection_update() method removes the items that is not present in both sets
# (or in all sets if the comparison is done between more than two sets).
# The intersection_update() method is different from the intersection() method,
# because the intersection() method returns a new set, without the unwanted items,
# and the intersection_update() method removes the unwanted items from the original set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# isdisjoint()
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)


# issubset()
# The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# issuperset()
# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)


# pop()
# The pop() method removes a random item from the set.
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)


# remove()
# The remove() method removes the specified element from the set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)


# symmetric_difference()
# The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
# same item ko chodake sabi item return karegi.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# symmetric_difference_update()
# The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# union()
# The union() method returns a set that contains all items from the original set, and all items from the specified sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)


# update()
# The update() method updates the current set, by adding items from another set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

