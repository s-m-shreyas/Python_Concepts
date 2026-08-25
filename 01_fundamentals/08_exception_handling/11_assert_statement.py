# type: ignore

"""
===============================================================================
Topic    : The assert Statement
File     : 11_assert_statement.py
Folder   : 08_exception_handling
Author   : S.M. Shreyas

Description
-----------
This file explains Python's 'assert' statement, which is used to verify
assumptions during development. Assertions help developers detect bugs early
by stopping execution whenever an expected condition becomes false.

Learning Objectives
-------------------
By the end of this file, you will understand:

1. What the assert statement is.
2. How AssertionError works.
3. Writing assertions with custom messages.
4. Using assertions for debugging.
5. The difference between assert and raise.
6. Why assertions should not validate user input.
7. The effect of Python's -O optimization flag.

Run this file
-------------
python 11_assert_statement.py
===============================================================================
"""

print("=" * 80)
print("THE ASSERT STATEMENT")
print("=" * 80)

# =============================================================================
# What is assert?
# =============================================================================

print("\n1. WHAT IS ASSERT?")
print("-" * 40)

"""
The assert statement checks whether a condition is True.

If the condition is True:
    Program continues normally.

If the condition is False:
    Python raises an AssertionError.

Syntax:

assert condition
assert condition, "Custom message"

Assertions are mainly used during development to detect programming errors.
"""

print("Assertions verify assumptions made by the programmer.")


# =============================================================================
# Basic Example
# =============================================================================

print("\n2. BASIC EXAMPLE")
print("-" * 40)

number = 10

assert number > 0

print("Assertion passed because the number is positive.")


# =============================================================================
# Assertion Failure
# =============================================================================

print("\n3. ASSERTION FAILURE")
print("-" * 40)

try:

    number = -5

    assert number > 0

except AssertionError as error:

    print("Assertion failed:", error)

print("""
The program did not crash because we handled
the AssertionError using try-except.
""")


# =============================================================================
# Custom Assertion Message
# =============================================================================

print("\n4. CUSTOM ASSERTION MESSAGE")
print("-" * 40)

try:

    age = -1

    assert age >= 0, "Age cannot be negative."

except AssertionError as error:

    print(error)

print("Custom messages make debugging easier.")


# =============================================================================
# Assertions for Debugging
# =============================================================================

print("\n5. ASSERTIONS FOR DEBUGGING")
print("-" * 40)

"""
Assertions help verify assumptions inside code.

Example:
A sorting function expects a non-empty list.
"""

numbers = [1, 2, 3]

assert len(numbers) > 0

print("List contains data.")

print("""
If the list unexpectedly became empty,
the assertion would immediately reveal the bug.
""")


# =============================================================================
# Real-World Example: Banking System
# =============================================================================

print("\n6. REAL-WORLD EXAMPLE")
print("-" * 40)

"""
Assertions are useful for checking internal program logic,
not user mistakes.
"""

def process_transaction(balance):

    assert balance >= 0, "Internal error: Balance became negative."

    print(f"Processing balance: ₹{balance}")

process_transaction(2500)

try:

    process_transaction(-100)

except AssertionError as error:

    print(error)


# =============================================================================
# assert vs raise
# =============================================================================

print("\n7. ASSERT VS RAISE")
print("-" * 40)

print("""
assert
------
Purpose:
    Detect programmer mistakes.

Disabled?
    Yes, using the -O optimization flag.

Example:
    assert x > 0

raise
-----
Purpose:
    Handle expected runtime situations.

Disabled?
    Never.

Example:
    raise ValueError("Invalid age")
""")

print("Use assert for debugging, raise for application logic.")


# =============================================================================
# Why Not Validate User Input with assert?
# =============================================================================

print("\n8. WHY NOT VALIDATE USER INPUT?")
print("-" * 40)

print("""
Bad Example

assert age >= 18

Why?

Assertions can disappear when Python runs with:

python -O script.py

The validation disappears too.

Instead:

if age < 18:
    raise ValueError("Age must be at least 18.")

User validation should always use raise.
""")


# =============================================================================
# The -O Optimization Flag
# =============================================================================

print("\n9. THE -O OPTIMIZATION FLAG")
print("-" * 40)

print("""
Python's optimization mode:

python -O script.py

Effects:
- Removes assert statements.
- Improves performance slightly.
- Keeps normal exceptions unchanged.

Example

assert False

Normally:
    AssertionError

With -O:
    The assertion is skipped.
""")

print("Assertions should never contain essential business logic.")


# =============================================================================
# AssertionError Class
# =============================================================================

print("\n10. ASSERTIONERROR")
print("-" * 40)

print("""
AssertionError is a built-in exception.

Hierarchy

BaseException
    └── Exception
         └── AssertionError

It behaves like other exceptions and can be caught normally.
""")

try:

    assert False, "Example AssertionError"

except AssertionError as error:

    print("Caught:", error)


# =============================================================================
# Best Practices
# =============================================================================

print("\n11. BEST PRACTICES")
print("-" * 40)

best_practices = [
    "Use assertions for internal consistency checks.",
    "Write meaningful assertion messages.",
    "Keep assertions simple.",
    "Use raise for user validation.",
    "Remember that assertions can be disabled."
]

for item in best_practices:
    print(f"✓ {item}")


# =============================================================================
# Common Mistakes
# =============================================================================

print("\n12. COMMON MISTAKES")
print("-" * 40)

print("""
❌ Using assert for user input validation.

Bad:

assert age >= 18

Better:

if age < 18:
    raise ValueError(...)

❌ Relying on assertions for business logic.

Assertions may disappear with -O.
""")


# =============================================================================
# Interview Tip
# =============================================================================

print("\n13. INTERVIEW TIP")
print("-" * 40)

print("""
Question:
What is the difference between assert and raise?

Answer:

assert
- Used for debugging.
- Raises AssertionError.
- Can be disabled with -O.

raise
- Used for expected runtime conditions.
- Raises any exception type.
- Always remains active.
""")


# =============================================================================
# Quick Revision
# =============================================================================

print("\n14. QUICK REVISION")
print("-" * 40)

revision = [
    ("assert condition", "Checks assumption"),
    ("AssertionError", "Raised when assertion fails"),
    ("assert x, message", "Custom message"),
    ("python -O", "Disables assertions"),
    ("raise", "Runtime validation")
]

for concept, meaning in revision:
    print(f"{concept:<22} → {meaning}")


# =============================================================================
# Key Takeaways
# =============================================================================

print("\n15. KEY TAKEAWAYS")
print("-" * 40)

takeaways = [
    "Assertions verify programmer assumptions.",
    "Failed assertions raise AssertionError.",
    "Custom messages improve debugging.",
    "Assertions can be disabled using -O.",
    "Use raise instead of assert for user validation."
]

for item in takeaways:
    print(f"✓ {item}")

print("\n" + "=" * 80)
print("End of 11_assert_statement.py")
print("=" * 80)