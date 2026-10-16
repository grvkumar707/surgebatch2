# This is a sample Python file

# name = input("enter your name: ")
# print("Hello, " + name + "!")

# a = "hello jatin"
# print (a)
# print (a)
# print (a)
# print (a)


# item_count = 4
# item_count += 1
# print(item_count)

# x = input("enter a value: ")
# print("You entered: " + x)
# y = input("enter another value: ")
# print("You entered: " + y)

# x,y,z = input("enter three values separated by a space: ").split()
# print("You entered: " + x)
# print("You entered: " + y)
# print("You entered: " + z)


# name = [0]
# name = "python"
# a = name[1:4]
# print(a)


#arithmetic operator   +,-,*,/,%

# a = 15
# b= 4

# print ("addition", a + b)
# print ("subtraction", a - b)
# print ("multiplication", a * b)
# print ("division", a / b)
# print ("modulus", a % b)
# print ("exponentiation", a ** b)
# print ("floor division", a // b)

# relational operators  <,<=,>,>=,==,!=
# a = 15
# b = 2
# print("a < b:", a < b)
# print("a <= b:", a <= b)
# print("a > b:", a > b)
# print("a >= b:", a >= b)
# print("a == b:", a == b)
# print("a != b:", a != b)

# logical operators  and, or, not
# a = True
# b = False
# print("a and b:", a and b)
# print("a or b:", a or b)
# print("not a:", not a)

# bitwise operators  &, |, ^, ~, <<, >>
# a = 5
# b = 3
# print("a & b:", a & b)
# print("a | b:", a | b)
# print("a ^ b:", a ^ b)
# print("~a:", ~a)
# print("a << 1:", a << 1)
# print("a >> 1:", a >> 1)


# assignment operators  =, +=, -=, *=, /=, %=, **=, //=
# a = 10
# b = 5
# a += b
# print("a += b:", a)
# a -= b
# print("a -= b:", a)
# a *= b
# print("a *= b:", a)
# a /= b
# print("a /= b:", a)
# a %= b
# print("a %= b:", a)
# a **= b
# print("a **= b:", a)
# a //= b
# print("a //= b:", a)

# identity operators  is, is not

# is = true if the operands are identical
# is not true if the operands are not identical

# a = 10
# b = 10
# print("a is b:", a is b)
# print("a is not b:", a is not b)

#if else statement
# a = 4
# if a > 5:
#     print("a is greater than 5")
# else:
#     print("a is not greater than 5")

#short if statement
# a = 4
# print("a is greater than 5") if a > 5 else print("a is not greater than 5")

#if-elif-else statement
# a = 10
# if a > 5:
#     print("a is greater than 5")
# elif a == 5:
#     print("a is equal to 5")
# else:
#     print("a is not greater than 5")


#nested if statement
# a = 15
# if a > 5:
#     if a < 15:
#         print("a is greater than 5 and less than 15")
#     else:
#         print("a is greater than or equal to 15")
# else:
#     print("a is not greater than 5")

#ternary operator
# a = 4
# result = "a is greater than 5" if a > 5 else "a is not greater than 5"
# print(result)

#match statement

# a = 5
# match a:
#     case 1:
#         print("a is 1")
#     case 2:
#         print("a is 2")
#     case _:
#         print("a is something else")


#for loops

# n = 20
# for i in range (10, 20):
#     print(i)

# a = ["jatin", "test", "bhalla"]
# for idx in range(len(a)):
#     print(idx, a[idx])

#while loops
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# nested loops
for i in range(3):
    for j in range(3):
        print(i, j)   