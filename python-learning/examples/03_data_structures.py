"""
TOPIC 3: Data Structures - Lists, Tuples, Sets and Dictionaries
=================================================================
Run this file with:  python 03_data_structures.py

Quick decision guide:
  - Need an ordered, changeable collection, duplicates OK?      -> list
  - Need an ordered collection that should NEVER change?        -> tuple
  - Need to store unique items and don't care about order?      -> set
  - Need to look things up by a name/key instead of position?   -> dict
"""

# -----------------------------------------------------------------------
# 1. LISTS - ordered, mutable (changeable), allow duplicates
# -----------------------------------------------------------------------
print("--- Lists ---")
fruits = ["apple", "banana", "cherry"]
print("fruits:", fruits)

# Indexing (starts at 0) and negative indexing (-1 = last item)
print("first fruit:", fruits[0])
print("last fruit:", fruits[-1])

# Slicing: list[start:stop] (stop is excluded)
print("first two:", fruits[0:2])

# Modifying a list
fruits.append("date")          # add to the end
fruits.insert(1, "apricot")    # insert at a specific index
fruits.remove("banana")        # remove by value
popped = fruits.pop()          # removes & returns the last item
print("after edits:", fruits, "| popped:", popped)

fruits.sort()                  # sort alphabetically, in place
print("sorted:", fruits)

# Looping and length
print("number of fruits:", len(fruits))
for fruit in fruits:
    print(" -", fruit)

# List comprehension: a compact way to build a new list from a loop
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
print("squares:", squares)
print("evens:", evens)


# -----------------------------------------------------------------------
# 2. TUPLES - ordered, IMMUTABLE (cannot change after creation)
# -----------------------------------------------------------------------
print("\n--- Tuples ---")
point = (3, 4)
print("point:", point, "x =", point[0], "y =", point[1])

# Tuples are great for fixed groups of values, e.g. coordinates, RGB colors
color = (255, 0, 0)

# Attempting color[0] = 100 would raise: TypeError: 'tuple' object does not
# support item assignment. Use a list instead if you need to change values.

# "Unpacking" - assigning each tuple element to its own variable
x, y = point
print("unpacked x, y:", x, y)

# A function can return multiple values as a tuple
def min_max(values):
    return min(values), max(values)

lowest, highest = min_max([4, 1, 9, 2])
print("lowest:", lowest, "highest:", highest)


# -----------------------------------------------------------------------
# 3. SETS - unordered, unique items only (no duplicates), mutable
# -----------------------------------------------------------------------
print("\n--- Sets ---")
unique_numbers = {1, 2, 2, 3, 3, 3}   # duplicates are automatically dropped
print("unique_numbers:", unique_numbers)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("union (a | b):", a | b)             # all items from both
print("intersection (a & b):", a & b)      # items in both
print("difference (a - b):", a - b)        # items only in a
print("symmetric diff (a ^ b):", a ^ b)    # items not shared by both

a.add(10)
a.discard(1)
print("a after add/discard:", a)

# Great real-world use: removing duplicates from a list
names_with_dupes = ["Amy", "Bob", "Amy", "Cho"]
unique_names = list(set(names_with_dupes))
print("unique_names (order not guaranteed):", unique_names)


# -----------------------------------------------------------------------
# 4. DICTIONARIES - key-value pairs, mutable, keys must be unique
# -----------------------------------------------------------------------
print("\n--- Dictionaries ---")
student = {
    "name": "Priya",
    "age": 21,
    "courses": ["Math", "Physics"],
}
print("student:", student)
print("name:", student["name"])

# .get() is safer than student["key"] because it won't crash if missing
print("gpa (missing key):", student.get("gpa", "not provided"))

# Adding/updating/removing keys
student["age"] = 22                  # update
student["gpa"] = 3.8                 # add new key
del student["courses"]               # remove a key
print("after edits:", student)

# Looping over a dictionary
print("looping with .items():")
for key, value in student.items():
    print(f"  {key}: {value}")

print("just the keys:", list(student.keys()))
print("just the values:", list(student.values()))

# Dictionary comprehension
squares_dict = {n: n ** 2 for n in range(1, 6)}
print("squares_dict:", squares_dict)

# Nested structures are common: a list of dictionaries
students = [
    {"name": "Priya", "age": 22},
    {"name": "Sam", "age": 19},
]
for s in students:
    print(f"{s['name']} is {s['age']} years old")


# -----------------------------------------------------------------------
# PRACTICE EXERCISES
# -----------------------------------------------------------------------
# TODO 1: Create a list of 5 numbers. Use a list comprehension to create a
#         new list containing only the numbers greater than 10.

# TODO 2: Create a tuple representing an RGB color (e.g. (120, 200, 50)).
#         Unpack it into r, g, b variables and print each one.

# TODO 3: Given two lists of numbers, convert them to sets and print their
#         intersection (the numbers that appear in both lists).

# TODO 4: Build a dictionary mapping 3 product names to their prices.
#         Loop through it and print "<name> costs $<price>" for each one.

# TODO 5: Given the list ["a", "b", "a", "c", "b", "a"], build a dictionary
#         that counts how many times each letter appears, e.g.
#         {"a": 3, "b": 2, "c": 1}. (Hint: loop through the list, and use
#         dict.get(letter, 0) to read the current count before adding 1.)
