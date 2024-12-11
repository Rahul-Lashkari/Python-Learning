# Set Methods in Python
# This Python file provides examples and explanations for common set methods.

# Creating example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# add() - Adds an element to the set
set1.add(6)
print("After add(6):", set1)

# remove() - Removes a specific element from the set (throws an error if the element is not present)
set1.remove(6)
print("After remove(6):", set1)

# discard() - Removes a specific element from the set (does not throw an error if the element is not present)
set1.discard(6)  # Element 6 is already removed
print("After discard(6):", set1)

# pop() - Removes and returns an arbitrary element from the set
popped_element = set1.pop()
print("Popped element:", popped_element)
print("After pop():", set1)

# clear() - Removes all elements from the set
set1.clear()
print("After clear():", set1)

# union() - Returns a new set with elements from both sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# intersection() - Returns a new set with elements common to both sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# difference() - Returns a new set with elements in the first set but not in the second
difference_set = set2.difference(set1)
print("Difference of set2 and set1:", difference_set)

# symmetric_difference() - Returns a new set with elements in either set but not both
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)

# issubset() - Checks if a set is a subset of another set
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?:", is_subset)

# issuperset() - Checks if a set is a superset of another set
is_superset = set2.issuperset(set1)
print("Is set2 a superset of set1?:", is_superset)

# isdisjoint() - Checks if two sets have no elements in common
is_disjoint = set1.isdisjoint(set2)
print("Are set1 and set2 disjoint?:", is_disjoint)

# copy() - Returns a shallow copy of the set
set_copy = set2.copy()
print("Copy of set2:", set_copy)

# update() - Updates a set with the union of itself and others
set2.update({9, 10})
print("After update({9, 10}):", set2)

# intersection_update() - Updates a set with the intersection of itself and another
set2.intersection_update({5, 6, 7, 10})
print("After intersection_update({5, 6, 7, 10}):", set2)

# difference_update() - Updates a set by removing elements found in another
set2.difference_update({5, 10})
print("After difference_update({5, 10}):", set2)

# symmetric_difference_update() - Updates a set with the symmetric difference of itself and another
set2.symmetric_difference_update({7, 8, 11})
print("After symmetric_difference_update({7, 8, 11}):", set2)
