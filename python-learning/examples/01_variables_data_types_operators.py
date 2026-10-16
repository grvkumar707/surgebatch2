"""
TOPIC 1: Variables, Data Types and Operators
=============================================
Run this file with:  python 01_variables_data_types_operators.py

Read the comments, run the file, then do the exercises at the bottom.
"""

# -----------------------------------------------------------------------
# 1. VARIABLES
# -----------------------------------------------------------------------
# A variable is just a name that points to a value in memory.
# Python figures out the type automatically - you don't declare it.

age = 25                 # an integer
height_m = 1.75          # a float (decimal number)
name = "Ada"             # a string
is_student = True        # a boolean (True/False)

print("--- Variables ---")
print(name, "is", age, "years old and", height_m, "m tall.")

# Naming rules: letters, numbers, underscores; cannot start with a number;
# case-sensitive; use snake_case by convention (e.g. first_name, total_count).
first_name = "Grace"
_private_value = 42      # leading underscore = "internal use" by convention

# Multiple assignment in one line
x, y, z = 1, 2, 3
print("x, y, z =", x, y, z)

# Reassigning a variable
score = 10
score = score + 5        # score is now 15
score += 5                # shorthand, score is now 20 (see operators below)
print("score =", score)


# -----------------------------------------------------------------------
# 2. DATA TYPES
# -----------------------------------------------------------------------
# The core built-in types you'll use constantly:
#   int    -> whole numbers        e.g. 10, -3
#   float  -> decimal numbers      e.g. 3.14, -0.5
#   str    -> text                 e.g. "hello"
#   bool   -> True / False
#   complex-> rarely used, e.g. 2 + 3j

print("\n--- Data Types ---")
print(type(age))          # <class 'int'>
print(type(height_m))     # <class 'float'>
print(type(name))         # <class 'str'>
print(type(is_student))   # <class 'bool'>

# Type conversion ("casting") - converting between types
age_as_text = str(age)          # int -> str:  "25"
text_number = "100"
number = int(text_number)       # str -> int:  100
pi_text = "3.14"
pi_float = float(pi_text)       # str -> float: 3.14
print("age_as_text:", age_as_text, type(age_as_text))
print("number:", number, type(number))

# Careful: int("3.14") would crash (ValueError). Convert to float first,
# then to int if you need to drop the decimal part:
# int(float("3.14")) -> 3

# f-strings (formatted strings) - the modern, readable way to build text
print(f"\n{name} is {age} years old ({height_m} m tall).")
print(f"Next year {name} will be {age + 1}.")


# -----------------------------------------------------------------------
# 3. OPERATORS
# -----------------------------------------------------------------------
print("\n--- Arithmetic Operators ---")
a, b = 7, 2
print("a + b  =", a + b)   # addition        -> 9
print("a - b  =", a - b)   # subtraction     -> 5
print("a * b  =", a * b)   # multiplication  -> 14
print("a / b  =", a / b)   # true division   -> 3.5 (always returns a float)
print("a // b =", a // b)  # floor division  -> 3 (drops the remainder)
print("a % b  =", a % b)   # modulo          -> 1 (the remainder)
print("a ** b =", a ** b)  # exponent        -> 49 (7 squared)

print("\n--- Comparison Operators (return True/False) ---")
print("a == b:", a == b)   # equal to
print("a != b:", a != b)   # not equal to
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n--- Logical Operators (combine booleans) ---")
is_adult = age >= 18
has_id = True
print("is_adult and has_id:", is_adult and has_id)  # both must be True
print("is_adult or has_id :", is_adult or has_id)   # at least one True
print("not is_adult       :", not is_adult)         # flips True/False

print("\n--- Assignment Operators (shorthand update-and-store) ---")
counter = 10
counter += 1   # same as counter = counter + 1
counter -= 2   # counter = counter - 2
counter *= 3   # counter = counter * 3
print("counter after +=1 -=2 *=3:", counter)

print("\n--- Membership Operators ---")
vowels = "aeiou"
print("'a' in vowels:", "a" in vowels)
print("'z' not in vowels:", "z" not in vowels)


# -----------------------------------------------------------------------
# PRACTICE EXERCISES
# -----------------------------------------------------------------------
# TODO 1: Create variables for a product's `price` (float) and `quantity`
#         (int). Calculate and print the `total_cost` using an f-string.

# TODO 2: Ask yourself: what type does `10 / 2` return? What about `10 // 2`?
#         Write both expressions in a print() statement and check your guess.

# TODO 3: Given celsius = 30, convert it to Fahrenheit using the formula
#         F = C * 9/5 + 32, and print the result with an f-string.

# TODO 4: Create two boolean variables `is_raining` and `has_umbrella`.
#         Print whether the person "will_stay_dry" using a logical operator.

# TODO 5: Convert the string "42" to an int, add 8 to it, then convert the
#         result back to a string and print it concatenated with " items".
