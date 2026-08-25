# type: ignore

"""
===============================================================================
Topic    : Exception Alias (Using 'as')
File     : 04_exception_alias.py
Folder   : 08_exception_handling
Author   : S.M. Shreyas

Description
-----------
This file explains how to capture exception objects using the 'as' keyword.
Instead of only catching an exception, you'll learn how to access its message,
type, and other useful information for debugging and logging.

Learning Objectives
-------------------
By the end of this file, you will understand:

1. What an exception object is.
2. Why 'except ... as e' is useful.
3. How to read exception messages.
4. How to identify exception types.
5. Real-world debugging examples.
6. Best practices for using exception aliases.

Run this file
-------------
python 04_exception_alias.py
===============================================================================
"""

print("=" * 80)
print("EXCEPTION ALIAS (USING 'AS')")
print("=" * 80)

# =============================================================================
# What is an Exception Alias?
# =============================================================================

print("\n1. WHAT IS AN EXCEPTION ALIAS?")
print("-" * 40)

"""
When an exception occurs, Python creates an exception object.

Using 'as' allows us to store that object in a variable.

Syntax:

try:
    ...
except ValueError as error:
    ...

The variable 'error' now contains information about what went wrong.
"""

print("Exception objects contain useful debugging information.")


# =============================================================================
# Basic Example
# =============================================================================

print("\n2. BASIC EXAMPLE")
print("-" * 40)

try:
    number = int("Python")
except ValueError as error:
    print("Exception message:", error)

print("""
Instead of displaying a generic message,
we can display the actual reason for failure.
""")


# =============================================================================
# Accessing Exception Messages
# =============================================================================

print("\n3. ACCESSING EXCEPTION MESSAGES")
print("-" * 40)

try:
    result = 100 / 0
except ZeroDivisionError as error:
    print("Error message:", error)

print("""
The exception object automatically stores
a human-readable error message.
""")


# =============================================================================
# Finding the Exception Type
# =============================================================================

print("\n4. FINDING THE EXCEPTION TYPE")
print("-" * 40)

try:
    values = [1, 2, 3]
    print(values[10])
except Exception as error:
    print("Exception object:", error)
    print("Exception type:", type(error))
    print("Exception class:", error.__class__.__name__)

print("""
Useful attributes:

type(error)
error.__class__.__name__
""")


# =============================================================================
# Printing Complete Exception Information
# =============================================================================

print("\n5. PRINTING COMPLETE INFORMATION")
print("-" * 40)

try:
    data = {"name": "Shreyas"}
    print(data["city"])
except KeyError as error:
    print("Exception:", error)
    print("Type:", type(error).__name__)
    print("Arguments:", error.args)

print("""
The args attribute stores the original values
used to construct the exception.
""")


# =============================================================================
# Real-World Example: User Input
# =============================================================================

print("\n6. REAL-WORLD EXAMPLE")
print("-" * 40)

user_inputs = ["25", "hello", "99"]

for value in user_inputs:

    try:
        number = int(value)
        print(f"Accepted: {number}")

    except ValueError as error:
        print(f"Input '{value}' failed.")
        print("Reason:", error)

print("\nEach failure now provides useful information.")


# =============================================================================
# Logging Example
# =============================================================================

print("\n7. LOGGING EXCEPTIONS")
print("-" * 40)

"""
In real applications, exceptions are often logged instead of
only being printed.
"""

try:
    file = open("missing_file.txt")
except FileNotFoundError as error:
    print(f"[LOG] File operation failed: {error}")

print("""
Real logging libraries include:

- logging
- loguru
- structlog
""")


# =============================================================================
# Generic Exception with Alias
# =============================================================================

print("\n8. GENERIC EXCEPTION WITH ALIAS")
print("-" * 40)

try:
    value = None
    value.upper()
except Exception as error:
    print("Unexpected error:", error)
    print("Type:", type(error).__name__)

print("""
Even generic Exception becomes much more useful
when captured with 'as'.
""")


# =============================================================================
# Why Not Ignore the Exception?
# =============================================================================

print("\n9. WHY NOT IGNORE THE EXCEPTION?")
print("-" * 40)

print("""
Bad Practice:

except ValueError:
    print("Something went wrong.")

Better:

except ValueError as error:
    print(error)

The second approach helps during debugging.
""")


# =============================================================================
# Best Practices
# =============================================================================

print("\n10. BEST PRACTICES")
print("-" * 40)

best_practices = [
    "Use meaningful variable names like error or exc.",
    "Display useful messages during development.",
    "Log exception details in production.",
    "Catch specific exceptions whenever possible.",
    "Use type(error).__name__ for readable exception names."
]

for item in best_practices:
    print(f"✓ {item}")


# =============================================================================
# Common Mistakes
# =============================================================================

print("\n11. COMMON MISTAKES")
print("-" * 40)

print("""
❌ Ignoring the exception object.

except ValueError:
    print("Error")

Better:

except ValueError as error:
    print(error)

❌ Using generic Exception unnecessarily.

Prefer specific exception types whenever possible.
""")


# =============================================================================
# Interview Tip
# =============================================================================

print("\n12. INTERVIEW TIP")
print("-" * 40)

print("""
Question:
What does 'except Exception as e' do?

Answer:
- Exception catches the error.
- 'e' stores the exception object.
- The object contains useful information such as
  the error message and exception type.
""")


# =============================================================================
# Quick Revision
# =============================================================================

print("\n13. QUICK REVISION")
print("-" * 40)

revision = [
    ("as", "Stores exception object"),
    ("str(error)", "Returns error message"),
    ("type(error)", "Returns exception type"),
    ("error.args", "Original exception arguments")
]

for concept, meaning in revision:
    print(f"{concept:<18} → {meaning}")


# =============================================================================
# Key Takeaways
# =============================================================================

print("\n14. KEY TAKEAWAYS")
print("-" * 40)

takeaways = [
    "Exceptions are objects, not just messages.",
    "The 'as' keyword captures the exception object.",
    "Exception objects help with debugging and logging.",
    "Use type(error).__name__ to identify exception types.",
    "Logging exception details is a real-world best practice."
]

for item in takeaways:
    print(f"✓ {item}")

print("\n" + "=" * 80)
print("End of 04_exception_alias.py")
print("=" * 80)