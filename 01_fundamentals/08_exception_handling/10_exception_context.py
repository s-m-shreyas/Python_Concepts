# type: ignore

"""
===============================================================================
Topic    : Exception Context
File     : 10_exception_context.py
Folder   : 08_exception_handling
Author   : S.M. Shreyas

Description
-----------
This file explains Exception Context in Python. Unlike exception chaining,
which is explicit ('raise ... from ...'), exception context is created
automatically whenever a new exception occurs while another exception is
being handled.

Learning Objectives
-------------------
By the end of this file, you will understand:

1. What exception context is.
2. How Python automatically creates __context__.
3. Difference between __context__ and __cause__.
4. Suppressing context using 'from None'.
5. Real-world debugging examples.
6. Best practices and common mistakes.

Run this file
-------------
python 10_exception_context.py
===============================================================================
"""

print("=" * 80)
print("EXCEPTION CONTEXT IN PYTHON")
print("=" * 80)

# =============================================================================
# What is Exception Context?
# =============================================================================

print("\n1. WHAT IS EXCEPTION CONTEXT?")
print("-" * 40)

"""
Exception Context is Python's automatic mechanism for remembering
the previous exception when another exception occurs while handling it.

Unlike exception chaining:

    raise NewError() from old_error

Context requires no 'from' statement.
Python creates it automatically.
"""

print("Python automatically remembers previous exceptions.")


# =============================================================================
# Basic Example
# =============================================================================

print("\n2. BASIC EXAMPLE")
print("-" * 40)

try:

    int("Python")

except ValueError:

    try:

        raise RuntimeError("Processing failed.")

    except RuntimeError as error:

        print("Current Exception :", error)
        print("Context Exception :", error.__context__)

print("""
The RuntimeError automatically remembers
the previous ValueError.
""")


# =============================================================================
# Understanding __context__
# =============================================================================

print("\n3. UNDERSTANDING __context__")
print("-" * 40)

try:

    numbers = [1, 2, 3]
    print(numbers[10])

except IndexError:

    try:

        raise ValueError("Invalid list operation.")

    except ValueError as error:

        print("Current Exception:", type(error).__name__)
        print("Context Type     :", type(error.__context__).__name__)
        print("Context Message  :", error.__context__)

print("""
The __context__ attribute stores
the automatically remembered exception.
""")


# =============================================================================
# __context__ vs __cause__
# =============================================================================

print("\n4. __CONTEXT__ VS __CAUSE__")
print("-" * 40)

print("""
__context__
-----------
Created automatically.

Example:
    ValueError
        ↓
    RuntimeError

Python connects them automatically.

__cause__
---------
Created explicitly.

Example:
    raise RuntimeError() from ValueError()

The programmer creates this relationship.
""")


# =============================================================================
# Comparing Both
# =============================================================================

print("\n5. COMPARING BOTH")
print("-" * 40)

class ApplicationError(Exception):
    pass

# Automatic context
try:

    int("Python")

except ValueError:

    try:
        raise ApplicationError("Automatic context example.")

    except ApplicationError as error:

        print("Automatic Context")
        print("Context:", type(error.__context__).__name__)
        print("Cause  :", error.__cause__)

# Explicit cause
try:

    int("Python")

except ValueError as original:

    try:
        raise ApplicationError("Explicit cause example.") from original

    except ApplicationError as error:

        print("\nExplicit Cause")
        print("Context:", type(error.__context__).__name__)
        print("Cause  :", type(error.__cause__).__name__)

print("""
Notice:
Automatic context creates __context__.
Using 'from' creates __cause__.
""")


# =============================================================================
# Suppressing Context with from None
# =============================================================================

print("\n6. SUPPRESSING CONTEXT")
print("-" * 40)

"""
Sometimes the original exception is not useful
for end users.

Python allows hiding it using:

raise NewException() from None
"""

try:

    int("Python")

except ValueError:

    try:
        raise RuntimeError("Only show this message.") from None

    except RuntimeError as error:

        print("Current Exception:", error)
        print("Context:", error.__context__)
        print("Cause:", error.__cause__)

print("""
Using 'from None' suppresses the displayed context
in the traceback.
""")


# =============================================================================
# Real-World Example: Configuration Loader
# =============================================================================

print("\n7. REAL-WORLD EXAMPLE: CONFIGURATION LOADER")
print("-" * 40)

class ConfigurationError(Exception):
    pass

try:

    raise FileNotFoundError("config.json missing.")

except FileNotFoundError:

    try:
        raise ConfigurationError(
            "Application configuration failed."
        )

    except ConfigurationError as error:

        print(error)
        print("Original Problem:", error.__context__)

print("""
The application reports a meaningful error
while still preserving debugging information.
""")


# =============================================================================
# Nested Exception Example
# =============================================================================

print("\n8. NESTED EXCEPTION EXAMPLE")
print("-" * 40)

try:

    raise ValueError("First error")

except ValueError:

    try:

        raise KeyError("Second error")

    except KeyError:

        try:

            raise RuntimeError("Third error")

        except RuntimeError as error:

            print("Current :", error)
            print("Context :", error.__context__)
            print("Previous Context:", error.__context__.__context__)

print("""
Multiple exceptions create a chain of contexts.
""")


# =============================================================================
# Best Practices
# =============================================================================

print("\n9. BEST PRACTICES")
print("-" * 40)

best_practices = [
    "Use __context__ while debugging.",
    "Use 'raise ... from ...' when creating meaningful wrappers.",
    "Use 'from None' only when hiding unnecessary internal details.",
    "Avoid suppressing useful debugging information."
]

for item in best_practices:
    print(f"✓ {item}")


# =============================================================================
# Common Mistakes
# =============================================================================

print("\n10. COMMON MISTAKES")
print("-" * 40)

print("""
❌ Confusing __context__ with __cause__.

Remember:

__context__
    Automatic

__cause__
    Explicit

❌ Using 'from None' everywhere.

It should only be used when internal implementation
details should be hidden.
""")


# =============================================================================
# Interview Tip
# =============================================================================

print("\n11. INTERVIEW TIP")
print("-" * 40)

print("""
Question:
What is the difference between __context__ and __cause__?

Answer:

__context__
- Created automatically.
- Stores the previous exception during exception handling.

__cause__
- Created using 'raise ... from ...'.
- Explicitly connects two exceptions.
""")


# =============================================================================
# Quick Revision
# =============================================================================

print("\n12. QUICK REVISION")
print("-" * 40)

revision = [
    ("__context__", "Automatic previous exception"),
    ("__cause__", "Explicit chained exception"),
    ("from None", "Suppress displayed context"),
    ("Nested exceptions", "Create multiple contexts")
]

for concept, meaning in revision:
    print(f"{concept:<22} → {meaning}")


# =============================================================================
# Key Takeaways
# =============================================================================

print("\n13. KEY TAKEAWAYS")
print("-" * 40)

takeaways = [
    "Python automatically creates exception context.",
    "__context__ stores the previous exception.",
    "__cause__ is created explicitly with 'from'.",
    "'from None' hides context from tracebacks.",
    "Understanding context makes debugging easier."
]

for item in takeaways:
    print(f"✓ {item}")

print("\n" + "=" * 80)
print("End of 10_exception_context.py")
print("=" * 80)