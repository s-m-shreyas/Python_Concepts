# type: ignore

"""
===============================================================================
Topic    : The raise Statement
File     : 07_raise_statement.py
Folder   : 08_exception_handling
Author   : S.M. Shreyas

Description
-----------
This file explains Python's 'raise' statement, which allows developers to
create and trigger exceptions intentionally. It is commonly used for input
validation, enforcing business rules, and creating predictable program behavior.

Learning Objectives
-------------------
By the end of this file, you will understand:

1. What the raise statement is.
2. Why manually raising exceptions is useful.
3. Raising built-in exceptions.
4. Raising exceptions with custom messages.
5. Re-raising exceptions.
6. Real-world validation examples.
7. Best practices and common mistakes.

Run this file
-------------
python 07_raise_statement.py
===============================================================================
"""

print("=" * 80)
print("THE RAISE STATEMENT")
print("=" * 80)

# =============================================================================
# What is raise?
# =============================================================================

print("\n1. WHAT IS RAISE?")
print("-" * 40)

"""
The 'raise' statement creates an exception manually.

Normally, Python raises exceptions automatically.

Example:
    10 / 0

Python raises:
    ZeroDivisionError

Using raise allows us to create our own exceptions whenever
our program detects an invalid situation.
"""

print("Developers can intentionally stop execution using raise.")


# =============================================================================
# Basic Syntax
# =============================================================================

print("\n2. BASIC SYNTAX")
print("-" * 40)

"""
Syntax:

raise ExceptionType("Message")

Example:

raise ValueError("Invalid input")
"""

print("Basic syntax understood.")


# =============================================================================
# Raising a Built-in Exception
# =============================================================================

print("\n3. RAISING A BUILT-IN EXCEPTION")
print("-" * 40)

try:
    raise ValueError("Age cannot be negative.")

except ValueError as error:
    print("Caught:", error)

print("The exception was created manually.")


# =============================================================================
# Raising Different Built-in Exceptions
# =============================================================================

print("\n4. DIFFERENT BUILT-IN EXCEPTIONS")
print("-" * 40)

examples = [
    ("TypeError", TypeError("Expected a string.")),
    ("KeyError", KeyError("Missing 'email' field.")),
    ("RuntimeError", RuntimeError("Unexpected runtime failure."))
]

for name, exception in examples:

    try:
        raise exception

    except Exception as error:
        print(f"{name:<12} → {error}")


# =============================================================================
# Input Validation Example
# =============================================================================

print("\n5. INPUT VALIDATION")
print("-" * 40)

"""
One of the most common uses of raise is validating user input.
"""

def validate_age(age):

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print(f"Valid age: {age}")

test_ages = [25, -5]

for age in test_ages:

    try:
        validate_age(age)

    except ValueError as error:
        print("Validation failed:", error)


# =============================================================================
# Business Rule Validation
# =============================================================================

print("\n6. BUSINESS RULE VALIDATION")
print("-" * 40)

"""
Real applications often enforce business rules.

Example:
A bank should not allow withdrawing more money than available.
"""

def withdraw(balance, amount):

    if amount > balance:
        raise ValueError("Insufficient balance.")

    return balance - amount

try:
    remaining = withdraw(1000, 250)
    print(f"Remaining balance: ₹{remaining}")

    remaining = withdraw(remaining, 2000)

except ValueError as error:
    print("Transaction failed:", error)


# =============================================================================
# Raising Without a Message
# =============================================================================

print("\n7. RAISING WITHOUT A CUSTOM MESSAGE")
print("-" * 40)

try:
    raise RuntimeError

except RuntimeError as error:
    print("Caught:", error)

print("""
Custom messages make debugging much easier.
""")


# =============================================================================
# Re-raising Exceptions
# =============================================================================

print("\n8. RE-RAISING EXCEPTIONS")
print("-" * 40)

"""
Sometimes we want to perform logging and then allow
the exception to continue upward.

Use:

raise

without specifying an exception.
"""

def process_number(value):

    try:
        return int(value)

    except ValueError:
        print("Logging: Invalid number encountered.")
        raise

try:
    process_number("Python")

except ValueError as error:
    print("Caller received:", error)


# =============================================================================
# Real-World Example: Password Validation
# =============================================================================

print("\n9. REAL-WORLD EXAMPLE")
print("-" * 40)

"""
Password policies are a perfect example
of using raise for validation.
"""

def validate_password(password):

    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")

    print("Password accepted.")

passwords = ["abc123", "SecurePass123"]

for password in passwords:

    print(f"\nTesting: {password}")

    try:
        validate_password(password)

    except ValueError as error:
        print(error)


# =============================================================================
# raise vs Automatic Exceptions
# =============================================================================

print("\n10. RAISE VS AUTOMATIC EXCEPTIONS")
print("-" * 40)

print("""
Automatic:

10 / 0

Python automatically raises ZeroDivisionError.

Manual:

raise ValueError("Invalid age")

The programmer decides when the exception should occur.
""")


# =============================================================================
# Best Practices
# =============================================================================

print("\n11. BEST PRACTICES")
print("-" * 40)

best_practices = [
    "Raise specific exception types.",
    "Write clear error messages.",
    "Validate inputs early.",
    "Use re-raise after logging when appropriate.",
    "Choose exceptions that accurately describe the problem."
]

for item in best_practices:
    print(f"✓ {item}")


# =============================================================================
# Common Mistakes
# =============================================================================

print("\n12. COMMON MISTAKES")
print("-" * 40)

print("""
❌ Raising generic Exception unnecessarily.

Bad:

raise Exception("Error")

Better:

raise ValueError("Invalid age")

Specific exceptions make debugging easier.
""")


# =============================================================================
# Interview Tip
# =============================================================================

print("\n13. INTERVIEW TIP")
print("-" * 40)

print("""
Question:
What is the purpose of the raise statement?

Answer:
The raise statement allows developers to create exceptions manually
whenever the program detects an invalid or unexpected condition.
""")


# =============================================================================
# Quick Revision
# =============================================================================

print("\n14. QUICK REVISION")
print("-" * 40)

revision = [
    ("raise ValueError()", "Manual exception"),
    ("raise", "Re-raise current exception"),
    ("Custom message", "Better debugging"),
    ("Validation", "Common real-world use")
]

for concept, meaning in revision:
    print(f"{concept:<25} → {meaning}")


# =============================================================================
# Key Takeaways
# =============================================================================

print("\n15. KEY TAKEAWAYS")
print("-" * 40)

takeaways = [
    "raise creates exceptions manually.",
    "Use it for validation and business rules.",
    "Specific exceptions improve readability.",
    "Custom messages make debugging easier.",
    "Re-raising preserves the original exception."
]

for item in takeaways:
    print(f"✓ {item}")

print("\n" + "=" * 80)
print("End of 07_raise_statement.py")
print("=" * 80)