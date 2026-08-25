# type: ignore

"""
===============================================================================
Topic    : Exception Basics
File     : 01_exception_basics.py
Folder   : 08_exception_handling
Author   : S.M. Shreyas

Description
-----------
This file introduces Python Exceptions, how they occur, and how Python handles
them. It demonstrates common built-in exceptions with practical examples.

Learning Objectives
-------------------
By the end of this file, you will understand:

1. What an exception is.
2. How exceptions differ from syntax errors.
3. How Python stops execution when an exception occurs.
4. Common built-in exceptions.
5. How to read exception messages and tracebacks.

Run this file
-------------
python 01_exception_basics.py
===============================================================================
"""

print("=" * 80)
print("PYTHON EXCEPTION BASICS")
print("=" * 80)

# =============================================================================
# What is an Exception?
# =============================================================================

print("\n1. WHAT IS AN EXCEPTION?")
print("-" * 40)

"""
An Exception is an error that occurs while a program is running.

Python immediately stops normal execution when an exception occurs.
If the exception is not handled, the program terminates and displays
a traceback.
"""

print("Program started successfully.")


# =============================================================================
# Syntax Error vs Exception
# =============================================================================

print("\n2. SYNTAX ERROR VS EXCEPTION")
print("-" * 40)

"""
Syntax Error
------------
Happens before the program starts running.

Example (DO NOT RUN):

if True
    print("Hello")

Output:
SyntaxError: expected ':'

Exceptions
----------
Occur while the program is already running.
"""

print("Syntax errors prevent execution before runtime.")


# =============================================================================
# Example: ZeroDivisionError
# =============================================================================

print("\n3. ZeroDivisionError")
print("-" * 40)

try:
    result = 10 / 0
except ZeroDivisionError as error:
    print("Caught Exception:", error)


# =============================================================================
# Example: ValueError
# =============================================================================

print("\n4. ValueError")
print("-" * 40)

try:
    number = int("Python")
except ValueError as error:
    print("Caught Exception:", error)


# =============================================================================
# Example: TypeError
# =============================================================================

print("\n5. TypeError")
print("-" * 40)

try:
    answer = "Age: " + 25
except TypeError as error:
    print("Caught Exception:", error)


# =============================================================================
# Example: IndexError
# =============================================================================

print("\n6. IndexError")
print("-" * 40)

numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError as error:
    print("Caught Exception:", error)


# =============================================================================
# Example: KeyError
# =============================================================================

print("\n7. KeyError")
print("-" * 40)

student = {
    "name": "Shreyas",
    "age": 22
}

try:
    print(student["city"])
except KeyError as error:
    print("Caught Exception:", error)


# =============================================================================
# Example: FileNotFoundError
# =============================================================================

print("\n8. FileNotFoundError")
print("-" * 40)

try:
    open("unknown_file.txt")
except FileNotFoundError as error:
    print("Caught Exception:", error)


# =============================================================================
# What Happens Internally?
# =============================================================================

print("\n9. HOW PYTHON HANDLES EXCEPTIONS")
print("-" * 40)

"""
When an exception occurs, Python performs these steps:

Step 1
------
Stops normal execution.

Step 2
------
Creates an Exception object.

Step 3
------
Searches for a matching exception handler.

Step 4
------
Executes the matching 'except' block.

Step 5
------
If no handler exists, Python prints a traceback and terminates.
"""

print("Python successfully found matching exception handlers above.")


# =============================================================================
# Common Built-in Exceptions
# =============================================================================

print("\n10. COMMON BUILT-IN EXCEPTIONS")
print("-" * 40)

common_exceptions = [
    ("ZeroDivisionError", "Division by zero"),
    ("ValueError", "Invalid value"),
    ("TypeError", "Wrong data type"),
    ("IndexError", "Invalid list index"),
    ("KeyError", "Missing dictionary key"),
    ("FileNotFoundError", "File does not exist"),
    ("AttributeError", "Object has no attribute"),
    ("ImportError", "Module import failed"),
    ("NameError", "Variable not defined"),
    ("RuntimeError", "General runtime issue")
]

for name, cause in common_exceptions:
    print(f"{name:<20} → {cause}")


# =============================================================================
# Interview Tip
# =============================================================================

print("\n11. INTERVIEW TIP")
print("-" * 40)

print("""
Question:
What is the difference between a Syntax Error and an Exception?

Answer:
- Syntax Errors happen before execution begins.
- Exceptions occur while the program is already running.
- Exceptions can be handled using try and except.
""")


# =============================================================================
# Key Takeaways
# =============================================================================

print("\n12. KEY TAKEAWAYS")
print("-" * 40)

takeaways = [
    "Exceptions occur during program execution.",
    "Syntax errors occur before execution.",
    "Python stops execution when an exception occurs.",
    "Exceptions are objects.",
    "Built-in exceptions describe different kinds of runtime errors.",
    "Proper exception handling makes programs more reliable."
]

for item in takeaways:
    print(f"✓ {item}")

print("\n" + "=" * 80)
print("End of 01_exception_basics.py")
print("=" * 80)