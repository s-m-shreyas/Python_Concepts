# type: ignore

"""
===============================================================================
Topic    : Try and Except
File     : 02_try_except.py
Folder   : 08_exception_handling
Author   : S.M. Shreyas

Description
-----------
This file explains Python's 'try' and 'except' statements, which allow
programs to handle runtime errors gracefully instead of crashing.

Learning Objectives
-------------------
By the end of this file, you will understand:

1. Why try-except is needed.
2. Basic try-except syntax.
3. How execution flows when an exception occurs.
4. What happens when no exception occurs.
5. Real-world examples of error handling.
6. Best practices for using try-except.

Run this file
-------------
python 02_try_except.py
===============================================================================
"""

print("=" * 80)
print("PYTHON TRY AND EXCEPT")
print("=" * 80)

# =============================================================================
# Why Do We Need try-except?
# =============================================================================

print("\n1. WHY DO WE NEED TRY-EXCEPT?")
print("-" * 40)

"""
Without exception handling, a runtime error immediately stops the program.

Example (DO NOT RUN):

number = int("Python")

Output:
ValueError

The program terminates.

Using try-except allows the program to continue running.
"""

print("try-except prevents unexpected program termination.")


# =============================================================================
# Basic Syntax
# =============================================================================

print("\n2. BASIC SYNTAX")
print("-" * 40)

"""
Structure:

try:
    risky_code()
except ExceptionType:
    handle_error()

Python first executes the try block.
If an exception occurs, the matching except block executes.
"""

print("Basic syntax understood.")


# =============================================================================
# Example 1: Handling ValueError
# =============================================================================

print("\n3. EXAMPLE: VALUEERROR")
print("-" * 40)

try:
    number = int("Python")
    print(number)
except ValueError:
    print("Invalid number entered.")

print("Program continues after handling the exception.")


# =============================================================================
# Example 2: Successful Execution
# =============================================================================

print("\n4. EXAMPLE: SUCCESSFUL EXECUTION")
print("-" * 40)

try:
    number = int("25")
    print(f"Converted number: {number}")
except ValueError:
    print("Conversion failed.")

print("Since no exception occurred, except was skipped.")


# =============================================================================
# Execution Flow
# =============================================================================

print("\n5. EXECUTION FLOW")
print("-" * 40)

print("Scenario A: No Exception")

try:
    print("Step 1")
    print("Step 2")
    print("Step 3")
except Exception:
    print("This never executes.")

print("\nScenario B: Exception Occurs")

try:
    print("Step 1")
    print(10 / 0)
    print("Step 3")
except ZeroDivisionError:
    print("Division by zero handled.")

print("""
Notice:
- Step 1 executed.
- Division caused an exception.
- Step 3 never executed.
- Control moved directly to except.
""")


# =============================================================================
# Real-World Example: User Input
# =============================================================================

print("\n6. REAL-WORLD EXAMPLE")
print("-" * 40)

"""
Imagine a calculator asking users for numbers.

Users may accidentally enter invalid text.

Instead of crashing, we handle the error.
"""

user_inputs = ["42", "hello", "100"]

for value in user_inputs:
    try:
        number = int(value)
        print(f"Accepted: {number}")
    except ValueError:
        print(f"Rejected: '{value}' is not a valid integer.")


# =============================================================================
# Multiple Operations Inside try
# =============================================================================

print("\n7. MULTIPLE OPERATIONS INSIDE TRY")
print("-" * 40)

"""
Everything inside the try block is monitored.

As soon as an exception occurs,
the remaining statements inside try are skipped.
"""

try:
    print("Opening resource...")
    value = int("50")
    print(f"Value: {value}")
    result = value / 0
    print("This line never executes.")
except ZeroDivisionError:
    print("Caught division error.")


# =============================================================================
# What Happens Without try-except?
# =============================================================================

print("\n8. WITHOUT TRY-EXCEPT")
print("-" * 40)

"""
The following would terminate the program.

Example:

print(10 / 0)

Instead, we safely handle it.
"""

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Program recovered safely.")


# =============================================================================
# Best Practices
# =============================================================================

print("\n9. BEST PRACTICES")
print("-" * 40)

best_practices = [
    "Keep try blocks as small as possible.",
    "Catch specific exceptions instead of generic ones.",
    "Write meaningful error messages.",
    "Avoid hiding errors unnecessarily.",
    "Allow programs to continue when appropriate."
]

for item in best_practices:
    print(f"✓ {item}")


# =============================================================================
# Common Mistakes
# =============================================================================

print("\n10. COMMON MISTAKES")
print("-" * 40)

print("""
❌ Catching every exception unnecessarily.

Bad:
    except Exception:
        pass

Why?

- Hides real bugs.
- Makes debugging difficult.

Instead, catch only the exceptions you expect.
""")


# =============================================================================
# Interview Tip
# =============================================================================

print("\n11. INTERVIEW TIP")
print("-" * 40)

print("""
Question:
What happens when an exception occurs inside a try block?

Answer:
1. Python immediately stops executing the remaining statements inside try.
2. It searches for a matching except block.
3. If found, that block executes.
4. Program execution continues after the exception handler.
""")


# =============================================================================
# Key Takeaways
# =============================================================================

print("\n12. KEY TAKEAWAYS")
print("-" * 40)

takeaways = [
    "try contains code that may fail.",
    "except handles matching exceptions.",
    "Remaining try statements are skipped after an exception.",
    "Programs can continue running after handling errors.",
    "Specific exception handling is better than generic handling."
]

for item in takeaways:
    print(f"✓ {item}")

print("\n" + "=" * 80)
print("End of 02_try_except.py")
print("=" * 80)