# type: ignore

"""
===============================================================================
Topic    : Exception Chaining
File     : 09_exception_chaining.py
Folder   : 08_exception_handling
Author   : S.M. Shreyas

Description
-----------
This file explains Exception Chaining in Python using 'raise ... from ...'.
Exception chaining allows developers to preserve the original cause of an
error while raising a more meaningful exception for higher-level code.

Learning Objectives
-------------------
By the end of this file, you will understand:

1. What exception chaining is.
2. Why preserving the original error matters.
3. Using 'raise ... from ...'.
4. Difference between chained and unchained exceptions.
5. Understanding __cause__.
6. Real-world examples.
7. Best practices and common mistakes.

Run this file
-------------
python 09_exception_chaining.py
===============================================================================
"""

print("=" * 80)
print("EXCEPTION CHAINING IN PYTHON")
print("=" * 80)

# =============================================================================
# What is Exception Chaining?
# =============================================================================

print("\n1. WHAT IS EXCEPTION CHAINING?")
print("-" * 40)

"""
Sometimes a low-level operation fails, but we want to expose a
more meaningful application-level error.

Instead of hiding the original error, Python allows us to connect
both exceptions together.

Syntax:

raise NewException(...) from original_exception
"""

print("Exception chaining preserves the original cause of an error.")


# =============================================================================
# Why Do We Need Exception Chaining?
# =============================================================================

print("\n2. WHY IS IT USEFUL?")
print("-" * 40)

"""
Imagine this situation:

- Reading a configuration file
- File doesn't exist
- Your application should report:
    ConfigurationError

Without chaining:
    Original FileNotFoundError is lost.

With chaining:
    Both errors become visible.
"""

print("Both low-level and high-level errors remain available.")


# =============================================================================
# Basic Example
# =============================================================================

print("\n3. BASIC EXAMPLE")
print("-" * 40)

class ConfigurationError(Exception):
    """Raised when configuration cannot be loaded."""


try:

    open("missing_config.json")

except FileNotFoundError as error:

    try:
        raise ConfigurationError(
            "Failed to load configuration."
        ) from error

    except ConfigurationError as chained_error:

        print("New Exception:", chained_error)
        print("Original Cause:", chained_error.__cause__)


# =============================================================================
# Without Exception Chaining
# =============================================================================

print("\n4. WITHOUT EXCEPTION CHAINING")
print("-" * 40)

try:

    open("another_missing_file.txt")

except FileNotFoundError:

    try:
        raise ConfigurationError("Configuration failed.")

    except ConfigurationError as error:
        print("New Exception:", error)
        print("Cause:", error.__cause__)

print("""
Notice:
Without 'from', __cause__ becomes None.
""")


# =============================================================================
# Understanding __cause__
# =============================================================================

print("\n5. UNDERSTANDING __cause__")
print("-" * 40)

try:

    int("Python")

except ValueError as error:

    try:
        raise RuntimeError("Number conversion failed.") from error

    except RuntimeError as new_error:

        print("Current Exception :", new_error)
        print("Original Exception:", new_error.__cause__)
        print("Cause Type        :", type(new_error.__cause__).__name__)

print("""
The __cause__ attribute stores the original exception.
""")


# =============================================================================
# Real-World Example: Database Layer
# =============================================================================

print("\n6. REAL-WORLD EXAMPLE: DATABASE")
print("-" * 40)

class DatabaseConnectionError(Exception):
    """Raised when the application cannot connect to the database."""


def connect_database():

    try:

        raise TimeoutError("Database server timed out.")

    except TimeoutError as error:

        raise DatabaseConnectionError(
            "Application cannot connect to the database."
        ) from error


try:

    connect_database()

except DatabaseConnectionError as error:

    print(error)
    print("Original Cause:", error.__cause__)


# =============================================================================
# Real-World Example: API Wrapper
# =============================================================================

print("\n7. REAL-WORLD EXAMPLE: API WRAPPER")
print("-" * 40)

class APIError(Exception):
    """Raised when an API request fails."""


def fetch_user():

    try:

        raise ConnectionError("Network unavailable.")

    except ConnectionError as error:

        raise APIError(
            "Unable to fetch user profile."
        ) from error


try:

    fetch_user()

except APIError as error:

    print(error)
    print("Underlying Error:", error.__cause__)


# =============================================================================
# Multiple Levels of Chaining
# =============================================================================

print("\n8. MULTIPLE LEVELS OF CHAINING")
print("-" * 40)

class ServiceError(Exception):
    pass


class ApplicationError(Exception):
    pass


try:

    try:

        raise ValueError("Invalid input.")

    except ValueError as error:

        raise ServiceError("Service failed.") from error

except ServiceError as error:

    try:
        raise ApplicationError("Application stopped.") from error

    except ApplicationError as final_error:

        print("Final Error:", final_error)
        print("Immediate Cause:", final_error.__cause__)

print("""
Errors can be chained across multiple application layers.
""")


# =============================================================================
# When Should You Use Chaining?
# =============================================================================

print("\n9. WHEN SHOULD YOU USE IT?")
print("-" * 40)

print("""
Good situations:

✓ Wrapping database errors
✓ Wrapping file errors
✓ Wrapping API errors
✓ Creating domain-specific exceptions

Avoid using chaining when the original exception
is completely unrelated.
""")


# =============================================================================
# Best Practices
# =============================================================================

print("\n10. BEST PRACTICES")
print("-" * 40)

best_practices = [
    "Use 'raise ... from ...' when wrapping exceptions.",
    "Preserve low-level debugging information.",
    "Create meaningful high-level exceptions.",
    "Keep exception messages clear.",
    "Avoid hiding original errors."
]

for item in best_practices:
    print(f"✓ {item}")


# =============================================================================
# Common Mistakes
# =============================================================================

print("\n11. COMMON MISTAKES")
print("-" * 40)

print("""
❌ Raising a new exception without preserving the original one.

Bad:

except FileNotFoundError:
    raise ConfigurationError()

Better:

except FileNotFoundError as error:
    raise ConfigurationError() from error
""")


# =============================================================================
# Interview Tip
# =============================================================================

print("\n12. INTERVIEW TIP")
print("-" * 40)

print("""
Question:
What does 'raise NewError() from original_error' do?

Answer:
It raises a new exception while preserving the original exception
as its cause, allowing both errors to appear in the traceback.
""")


# =============================================================================
# Quick Revision
# =============================================================================

print("\n13. QUICK REVISION")
print("-" * 40)

revision = [
    ("raise ... from ...", "Chain exceptions"),
    ("__cause__", "Original exception"),
    ("Chaining", "Preserves debugging information"),
    ("Without from", "__cause__ becomes None")
]

for concept, meaning in revision:
    print(f"{concept:<24} → {meaning}")


# =============================================================================
# Key Takeaways
# =============================================================================

print("\n14. KEY TAKEAWAYS")
print("-" * 40)

takeaways = [
    "Exception chaining preserves the original cause.",
    "Use 'raise ... from ...' when wrapping exceptions.",
    "__cause__ stores the original exception.",
    "Chaining improves debugging and tracebacks.",
    "It is widely used in production applications."
]

for item in takeaways:
    print(f"✓ {item}")

print("\n" + "=" * 80)
print("End of 09_exception_chaining.py")
print("=" * 80)