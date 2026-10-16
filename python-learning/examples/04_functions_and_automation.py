"""
TOPIC 4: Functions and Basic Scripting for Automation
========================================================
Run this file with:  python 04_functions_and_automation.py
"""

import os
import datetime


# -----------------------------------------------------------------------
# 1. DEFINING AND CALLING FUNCTIONS
# -----------------------------------------------------------------------
# A function is a reusable, named block of code. Define it once with `def`,
# then "call" it as many times as you need.

def greet(name):
    """Return a greeting for the given name.

    The text in triple quotes right under `def` is a docstring - it
    documents what the function does and shows up in help(greet).
    """
    return f"Hello, {name}!"


print("--- Basic function ---")
print(greet("Ada"))
print(greet("Sam"))


# -----------------------------------------------------------------------
# 2. PARAMETERS: defaults, *args, **kwargs
# -----------------------------------------------------------------------
print("\n--- Default parameters ---")


def greet_with_title(name, title="Mx."):
    return f"Hello, {title} {name}!"


print(greet_with_title("Lopez"))                 # uses default title
print(greet_with_title("Lopez", title="Dr."))     # overrides default

print("\n--- *args: accept any number of positional arguments ---")


def total(*numbers):
    """`numbers` becomes a tuple of everything passed in."""
    return sum(numbers)


print("total(1, 2, 3)      =", total(1, 2, 3))
print("total(10, 20, 30, 40) =", total(10, 20, 30, 40))

print("\n--- **kwargs: accept any number of named arguments ---")


def build_profile(**details):
    """`details` becomes a dictionary of the keyword arguments passed in."""
    return details


profile = build_profile(name="Priya", age=22, city="Delhi")
print("profile:", profile)


# -----------------------------------------------------------------------
# 3. RETURN VALUES AND SCOPE
# -----------------------------------------------------------------------
print("\n--- Return values ---")


def add(a, b):
    return a + b


result = add(3, 4)      # the returned value is stored in `result`
print("add(3, 4) =", result)

# A function with no `return` statement returns None
def say_hi():
    print("hi!")


value = say_hi()
print("say_hi() returned:", value)  # None

print("\n--- Variable scope ---")
counter = 0   # this is a "global" variable


def increment():
    # Variables created inside a function are "local" - they only exist
    # while the function runs, and don't affect variables of the same
    # name outside the function unless you use the `global` keyword.
    counter = 100   # this creates a NEW local variable, separate from the global one
    return counter


print("increment() returns:", increment())
print("global counter is still:", counter)


def increment_global():
    global counter   # explicitly say we mean the global variable
    counter += 1
    return counter


print("increment_global() returns:", increment_global())
print("global counter is now:", counter)


# -----------------------------------------------------------------------
# 4. LAMBDA FUNCTIONS (small, one-line anonymous functions)
# -----------------------------------------------------------------------
print("\n--- Lambda functions ---")
square = lambda n: n ** 2
print("square(5):", square(5))

# Commonly used with sorted(), map(), filter()
words = ["banana", "kiwi", "fig", "watermelon"]
by_length = sorted(words, key=lambda w: len(w))
print("sorted by length:", by_length)

lengths = list(map(lambda w: len(w), words))
print("lengths:", lengths)

short_words = list(filter(lambda w: len(w) <= 4, words))
print("short words:", short_words)


# -----------------------------------------------------------------------
# 5. BASIC SCRIPTING FOR AUTOMATION
# -----------------------------------------------------------------------
# A "script" just means a .py file that does something useful end-to-end
# when you run it, usually by combining functions + loops + conditionals +
# the standard library (modules like `os`, `datetime`, `sys`, `pathlib`).
#
# Below is a small, realistic automation example: scan a folder for .txt
# files and report how many lines/words are in each one.

def count_lines_and_words(file_path):
    """Return (line_count, word_count) for a text file."""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    return line_count, word_count


def scan_folder_for_txt_files(folder_path):
    """Return a list of (filename, line_count, word_count) for every .txt
    file directly inside folder_path."""
    report = []
    for entry in os.listdir(folder_path):
        full_path = os.path.join(folder_path, entry)
        if os.path.isfile(full_path) and entry.lower().endswith(".txt"):
            lines, words = count_lines_and_words(full_path)
            report.append((entry, lines, words))
    return report


def print_report(report):
    if not report:
        print("No .txt files found.")
        return
    # Sort by word count, highest first
    report.sort(key=lambda row: row[2], reverse=True)
    print(f"{'File':30} {'Lines':>8} {'Words':>8}")
    for filename, lines, words in report:
        print(f"{filename:30} {lines:>8} {words:>8}")


if __name__ == "__main__":
    print("\n--- Automation example: scan this project for .txt files ---")
    # This file lives in <repo_root>/python-learning/examples/, so we need
    # to go up three levels (examples -> python-learning -> repo_root).
    examples_dir = os.path.dirname(os.path.abspath(__file__))
    python_learning_dir = os.path.dirname(examples_dir)
    repo_root = os.path.dirname(python_learning_dir)
    report = scan_folder_for_txt_files(repo_root)
    print_report(report)
    print(f"\nScan finished at {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")


# -----------------------------------------------------------------------
# PRACTICE EXERCISES
# -----------------------------------------------------------------------
# TODO 1: Write a function `is_palindrome(text)` that returns True if a
#         string reads the same forwards and backwards (ignore case),
#         e.g. is_palindrome("Racecar") -> True.

# TODO 2: Write a function `average(*numbers)` that accepts any number of
#         numeric arguments and returns their average.

# TODO 3: Write a function `describe_person(name, **extra_info)` that
#         prints the name plus every extra keyword argument, e.g.
#         describe_person("Sam", age=30, city="Pune").

# TODO 4: Extend `scan_folder_for_txt_files` (or write a similar function)
#         so it also writes the report to a file called "report.txt" in
#         the same folder, using a `with open(...) as f: f.write(...)`
#         block instead of just printing.

# TODO 5: Write a small automation script using a function + a loop that
#         renames every file in a given folder by adding today's date as
#         a prefix, e.g. "notes.txt" -> "2024-01-01_notes.txt". (Hint:
#         use os.listdir(), os.rename(), and datetime.date.today().)
