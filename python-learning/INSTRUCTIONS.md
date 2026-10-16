# Python Learning Path

Welcome! This folder contains a short, hands-on Python course covering four topics:

1. Variables, data types and operators
2. If-else conditions and loops
3. Data structures: lists, tuples, sets and dictionaries
4. Functions and basic scripting for automation

Each topic has a runnable `.py` file in [examples/](./examples) full of comments,
printed demonstrations, and practice exercises at the bottom.

## 1. Prerequisites

* Install Python 3.10+ from https://www.python.org/downloads/ (or via `winget install Python.Python.3.12`).
* Verify the install:
  ```powershell
  python --version
  ```
* (Optional but recommended) Use VS Code with the Python extension for syntax highlighting,
  debugging and IntelliSense.

## 2. How to use these files

1. Open a file in `examples/` and read it top to bottom like a tutorial — it's designed to be read, not just run.
2. Run it to see the output (see [section 3](#3-commands-to-run-each-file) for the full list of commands):
   ```powershell
   python python-learning\examples\01_variables_data_types_operators.py
   ```
3. Each file ends with a `PRACTICE EXERCISES` section containing `TODO` comments.
   Try to solve them yourself directly in the file (or in a scratch copy) before checking
   the hints. This is the most important step — reading alone won't build the skill.
4. Use `print()` liberally while experimenting; it's the fastest way to understand what a
   line of code actually does.

## 3. Commands to run each file

Run these from the repo root (`c:\Users\lenovo\Desktop\surgebatch2`):

```powershell
python python-learning\examples\01_variables_data_types_operators.py
python python-learning\examples\02_if_else_and_loops.py
python python-learning\examples\03_data_structures.py
python python-learning\examples\04_functions_and_automation.py
```

Or, if you `cd` into the examples folder first:

```powershell
cd python-learning\examples
python 01_variables_data_types_operators.py
python 02_if_else_and_loops.py
python 03_data_structures.py
python 04_functions_and_automation.py
```

## 4. Recommended learning order

Go through the files in this order — each one builds on the previous:

| # | File | Topic |
|---|------|-------|
| 1 | [01_variables_data_types_operators.py](./examples/01_variables_data_types_operators.py) | Variables, data types, type conversion, operators |
| 2 | [02_if_else_and_loops.py](./examples/02_if_else_and_loops.py) | Conditional logic, `for`/`while` loops, `break`/`continue` |
| 3 | [03_data_structures.py](./examples/03_data_structures.py) | Lists, tuples, sets, dictionaries and when to use each |
| 4 | [04_functions_and_automation.py](./examples/04_functions_and_automation.py) | Functions, arguments, scope, and a small automation script |

## 5. Suggested pace

* **Session 1 (45–60 min):** File 1 + exercises.
* **Session 2 (45–60 min):** File 2 + exercises.
* **Session 3 (60–90 min):** File 3 + exercises (this is the biggest topic).
* **Session 4 (60–90 min):** File 4 + exercises, then try the mini-project below.

## 6. Mini-project (after finishing all four files)

Write a script that:
1. Reads every `.txt` file in a folder.
2. Counts the number of lines and words in each file.
3. Prints a small report, sorted by word count (highest first).
4. Saves the report to a new file called `report.txt`.

This combines all four topics: variables/operators (counting), loops (iterating files/lines),
data structures (storing counts in a dictionary/list), and functions (organizing the logic into
reusable pieces). A worked example of something similar is in
[04_functions_and_automation.py](./examples/04_functions_and_automation.py) — try building
your own version before peeking at it.

## 7. Quick reference / cheat sheet

```python
# Variables & types
x = 5; y = 3.14; name = "Ada"; is_valid = True

# Conditionals
if x > 0:
    pass
elif x == 0:
    pass
else:
    pass

# Loops
for item in [1, 2, 3]:
    pass
while x > 0:
    x -= 1

# Data structures
a_list = [1, 2, 3]          # ordered, mutable, duplicates allowed
a_tuple = (1, 2, 3)         # ordered, immutable
a_set = {1, 2, 3}           # unordered, unique items only
a_dict = {"key": "value"}   # key-value pairs

# Functions
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

## 8. Where to go next

Once comfortable with all four topics, natural next steps are:
* Reading/writing files (`open()`, `with` statements)
* Error handling (`try`/`except`)
* Working with modules/packages and `pip`
* Object-oriented programming (classes)
