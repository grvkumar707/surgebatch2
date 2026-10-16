"""
TOPIC 2: If-else Conditions and Loops
======================================
Run this file with:  python 02_if_else_and_loops.py
"""

# -----------------------------------------------------------------------
# 1. IF / ELIF / ELSE
# -----------------------------------------------------------------------
# Conditions let your program make decisions. Python checks conditions
# top to bottom and runs the first block whose condition is True.

print("--- if / elif / else ---")
temperature = 28

if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("It's warm outside.")
elif temperature > 10:
    print("It's cool outside.")
else:
    print("It's cold outside.")

# Nested if: an if statement inside another if statement
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Welcome to the concert!")
    else:
        print("You need a ticket.")
else:
    print("Sorry, 18+ only.")

# Combining conditions with logical operators keeps code flatter/cleaner
if age >= 18 and has_ticket:
    print("Welcome to the concert! (flattened version)")

# The "ternary" (one-line if-else) - handy for simple cases
status = "adult" if age >= 18 else "minor"
print("status:", status)


# -----------------------------------------------------------------------
# 2. FOR LOOPS
# -----------------------------------------------------------------------
# A for loop repeats a block of code once per item in a sequence
# (a string, list, range, etc).

print("\n--- for loop over range() ---")
for i in range(5):          # 0, 1, 2, 3, 4  (5 is excluded)
    print("i =", i)

print("\n--- for loop with start, stop, step ---")
for i in range(2, 10, 2):   # 2, 4, 6, 8
    print("even:", i)

print("\n--- for loop over a list ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("fruit:", fruit)

print("\n--- for loop with enumerate() (get index + value) ---")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("\n--- for loop over a string (iterates characters) ---")
for letter in "abc":
    print("letter:", letter)


# -----------------------------------------------------------------------
# 3. WHILE LOOPS
# -----------------------------------------------------------------------
# A while loop repeats as long as its condition stays True.
# You are responsible for changing something inside the loop so it
# eventually becomes False - otherwise you get an infinite loop!

print("\n--- while loop ---")
count = 0
while count < 5:
    print("count =", count)
    count += 1   # without this line, the loop would never end

# Simple countdown example
print("\n--- countdown ---")
countdown = 3
while countdown > 0:
    print(countdown, "...")
    countdown -= 1
print("Liftoff!")


# -----------------------------------------------------------------------
# 4. break, continue, and loop-else
# -----------------------------------------------------------------------
print("\n--- break (exit the loop early) ---")
for number in range(10):
    if number == 5:
        break            # stop the loop completely once we hit 5
    print("number:", number)

print("\n--- continue (skip to the next iteration) ---")
for number in range(10):
    if number % 2 != 0:
        continue         # skip odd numbers
    print("even number:", number)

# A for/while can have an else block, which runs only if the loop
# finished WITHOUT hitting a break. Useful for "search" patterns.
print("\n--- for/else (search pattern) ---")
target = 7
numbers = [1, 3, 5, 9]
for n in numbers:
    if n == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} was not found in the list.")


# -----------------------------------------------------------------------
# PRACTICE EXERCISES
# -----------------------------------------------------------------------
# TODO 1: Write an if/elif/else chain that takes a `score` (0-100) and
#         prints a letter grade: A (90+), B (80-89), C (70-79), else "F".

# TODO 2: Use a for loop with range() to print all multiples of 3 between
#         1 and 30 (inclusive).

# TODO 3: Use a while loop to repeatedly halve a number (start at 100)
#         until it drops below 1, printing the value each time.

# TODO 4: Loop through the list ["cat", "dog", "fish", "bird"] and use
#         `continue` to skip any word that doesn't contain the letter "i".

# TODO 5: Write a loop that sums the numbers from 1 to 100 and prints the
#         total (hint: the answer should be 5050).
