#Non-premitive data types in python
# 1.List:
# A list is a collection of multiple items stored in a single variable.
#Lists are ordered.
#Lists are mutable (changeable).
#Lists allow duplicate values.
#Lists can store different data types.
#Lists are created using square brackets []
#Example:
fruits = ["Apple", "Mango", "Banana"]

print(fruits)

#Example:
list= [10, 20, 30, 40,20, 20, 50]
list.append(50)
list.extend([50, 60, 70])
list.insert(1, 60)
list.insert(60, 6)
#list.remove(20)
list.pop()
list.pop()
print(list)

# 2.Tuple:
# A tuple is a collection of elements used to store multiple values in a single variable.
# Tuple is ordered.
# Tuple is immutable (cannot be changed after creation).
# Tuple allows duplicate values.
# Tuple can store different data types.
# Tuples are created using round brackets ().
#Example:
my_tuple = (10, 20, 30, 40)

print(my_tuple)
print(type(my_tuple))

# 3.Dictionary:
#A dictionary is a collection of data that stores information in key-value pairs.
# Dictionary is ordered.
# Dictionary is mutable (changeable).
# Keys must be unique.
# Values can be duplicated.
# Keys and values can have different data types.
# Dictionary is created using curly brackets {}.
#Example:
student = {
    "name": "Sonali",
    "age": 22,
    "course": "MCA"
}

print(student)
print(type(student))

#Example:
dict={"name":"Ashis","age":22}
print(dict.get("name"))
print(dict.keys())
print(dict.values())
dict.update({"name":"ashis","age":23})
dict.clear()
a=dict.copy()
print(a)

# 4.Set:
#A set is a collection of unique elements in Python.
# Set is mutable (changeable).
# Set does not allow duplicate values.
# Set is unordered (no fixed position or indexing).
# Set can store different data types.
# Set is created using curly brackets {}.
#Example:
my_set = {10, 20, 30, 40}

print(my_set)
print(type(my_set))

#Example:
set_A={1,2,3,4}
set_B={4,5,6,7}
set_A.add(5)
set_A.update([9,6])
#set_A.remove(10)
set_A.discard(10)
u_set=set_A.union(set_B)
u_set=set_A.intersection(set_B)
u_set=set_A.difference(set_B)
u_set=set_A.difference(set_B)
print(u_set)

