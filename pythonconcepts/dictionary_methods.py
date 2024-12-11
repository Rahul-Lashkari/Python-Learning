# Dictionary Methods in Python
# This Python file provides examples and explanations for common dictionary methods.

# Creating an example dictionary
dict1 = {"name": "Alice", "age": 25, "city": "New York"}
print(dict1)

# keys() - Returns a view object of all keys in the dictionary
keys = dict1.keys()
print("Keys:", keys)

# values() - Returns a view object of all values in the dictionary
values = dict1.values()
print("Values:", values)

# items() - Returns a view object of key-value pairs
items = dict1.items()
print("Items:", items)

# get() - Returns the value for a key, or a default value if the key is not present
age = dict1.get("age")
print("Age:", age)
unknown = dict1.get("salary", "Not Available")
print("Salary:", unknown)

# update() - Updates the dictionary with key-value pairs from another dictionary or iterable
dict1.update({"profession": "Engineer", "city": "Boston"})
print("After update:", dict1)

# pop() - Removes a key-value pair and returns the value
removed_value = dict1.pop("age")
print("Removed age:", removed_value)
print("After pop:", dict1)

# popitem() - Removes and returns the last inserted key-value pair
last_item = dict1.popitem()
print("Popped item:", last_item)
print("After popitem:", dict1)

# clear() - Removes all elements from the dictionary
dict1.clear()
print("After clear:", dict1)

# copy() - Returns a shallow copy of the dictionary
dict_copy = {"a": 1, "b": 2}.copy()
print("Copy of dictionary:", dict_copy)
