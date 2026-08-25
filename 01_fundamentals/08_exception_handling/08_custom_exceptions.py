# type: ignore

"""
===============================================================================
Topic    : Custom Exceptions
File     : 08_custom_exceptions.py
Folder   : 08_exception_handling
Author   : S.M. Shreyas

Description
-----------
This file explains how to create and use custom exceptions in Python.
Custom exceptions allow developers to represent application-specific errors,
making code more readable, maintainable, and easier to debug.

Learning Objectives
-------------------
By the end of this file, you will understand:

1. What custom exceptions are.
2. Why custom exceptions are useful.
3. Creating exceptions by inheriting from Exception.
4. Adding custom messages and attributes.
5. Using custom exceptions in real-world applications.
6. Best practices and common mistakes.

Run this file
-------------
python 08_custom_exceptions.py
===============================================================================
"""

print("=" * 80)
print("CUSTOM EXCEPTIONS IN PYTHON")
print("=" * 80)

# =============================================================================
# What are Custom Exceptions?
# =============================================================================

print("\n1. WHAT ARE CUSTOM EXCEPTIONS?")
print("-" * 40)

"""
Python provides many built-in exceptions like:

- ValueError
- TypeError
- IndexError
- KeyError

However, real-world applications often need errors that describe
business-specific problems.

Examples:

- InvalidAgeError
- InsufficientBalanceError
- AuthenticationError
- PaymentFailedError

These are called custom exceptions.
"""

print("Custom exceptions describe application-specific errors.")


# =============================================================================
# Creating Your First Custom Exception
# =============================================================================

print("\n2. CREATING YOUR FIRST CUSTOM EXCEPTION")
print("-" * 40)

"""
A custom exception is simply a class that inherits from Exception.
"""

class InvalidAgeError(Exception):
    """Raised when age is negative."""


try:

    age = -5

    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

except InvalidAgeError as error:
    print("Caught:", error)


# =============================================================================
# Why Inherit from Exception?
# =============================================================================

print("\n3. WHY INHERIT FROM EXCEPTION?")
print("-" * 40)

"""
Python's exception hierarchy looks like this:

BaseException
    │
    ├── Exception
    │      ├── ValueError
    │      ├── TypeError
    │      └── YourCustomException

By inheriting from Exception,
your custom error behaves exactly like built-in exceptions.
"""

print("Inheritance makes custom exceptions compatible with try-except.")


# =============================================================================
# Custom Exception with Default Message
# =============================================================================

print("\n4. DEFAULT ERROR MESSAGE")
print("-" * 40)

class PasswordTooShortError(Exception):

    def __init__(self, message="Password must contain at least 8 characters."):
        super().__init__(message)

try:

    raise PasswordTooShortError()

except PasswordTooShortError as error:
    print(error)


# =============================================================================
# Custom Exception with Additional Information
# =============================================================================

print("\n5. ADDING CUSTOM ATTRIBUTES")
print("-" * 40)

"""
Custom exceptions can store additional information.
"""

class InsufficientBalanceError(Exception):

    def __init__(self, balance, amount):

        self.balance = balance
        self.amount = amount

        super().__init__(
            f"Available balance: ₹{balance}, Requested: ₹{amount}"
        )


try:

    raise InsufficientBalanceError(1000, 2500)

except InsufficientBalanceError as error:

    print(error)
    print("Balance:", error.balance)
    print("Requested:", error.amount)


# =============================================================================
# Real-World Example: Banking System
# =============================================================================

print("\n6. REAL-WORLD EXAMPLE: BANKING")
print("-" * 40)

class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds available balance."""


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ₹{amount}. Available: ₹{self.balance}"
            )

        self.balance -= amount
        return self.balance


account = BankAccount(5000)

try:

    print("Remaining Balance:", account.withdraw(1500))
    print("Remaining Balance:", account.withdraw(4000))

except InsufficientFundsError as error:
    print("Transaction Failed:", error)


# =============================================================================
# Real-World Example: User Authentication
# =============================================================================

print("\n7. REAL-WORLD EXAMPLE: AUTHENTICATION")
print("-" * 40)

class AuthenticationError(Exception):
    """Raised when login credentials are invalid."""


def login(username, password):

    if username != "admin" or password != "python123":
        raise AuthenticationError("Invalid username or password.")

    return "Login Successful"


credentials = [
    ("admin", "wrongpass"),
    ("admin", "python123")
]

for username, password in credentials:

    try:
        print(login(username, password))

    except AuthenticationError as error:
        print(error)


# =============================================================================
# Exception Hierarchy with Custom Exceptions
# =============================================================================

print("\n8. CUSTOM EXCEPTION HIERARCHY")
print("-" * 40)

class ValidationError(Exception):
    """Base validation exception."""


class EmailValidationError(ValidationError):
    """Raised for invalid email."""


class PhoneValidationError(ValidationError):
    """Raised for invalid phone number."""


errors = [
    EmailValidationError("Invalid email."),
    PhoneValidationError("Invalid phone number.")
]

for error in errors:

    try:
        raise error

    except ValidationError as caught:
        print("Validation Error:", caught)

print("""
A parent custom exception allows multiple related errors
to be handled together.
""")


# =============================================================================
# Catching Custom and Built-in Exceptions Together
# =============================================================================

print("\n9. MIXING CUSTOM AND BUILT-IN EXCEPTIONS")
print("-" * 40)

try:

    number = int("Python")

except (ValueError, AuthenticationError) as error:
    print("Handled:", error)


# =============================================================================
# Best Practices
# =============================================================================

print("\n10. BEST PRACTICES")
print("-" * 40)

best_practices = [
    "Inherit from Exception.",
    "Choose meaningful class names.",
    "Use descriptive error messages.",
    "Group related exceptions under a parent class.",
    "Store additional information when useful."
]

for item in best_practices:
    print(f"✓ {item}")


# =============================================================================
# Common Mistakes
# =============================================================================

print("\n11. COMMON MISTAKES")
print("-" * 40)

print("""
❌ Using generic Exception for business errors.

Bad:

raise Exception("Login failed")

Better:

raise AuthenticationError("Invalid username or password")

Custom names make debugging much easier.
""")


# =============================================================================
# Interview Tip
# =============================================================================

print("\n12. INTERVIEW TIP")
print("-" * 40)

print("""
Question:
Why should custom exceptions inherit from Exception?

Answer:
Because Exception is Python's standard base class for application-level
runtime errors. Inheriting from it allows custom exceptions to work
naturally with try-except blocks.
""")


# =============================================================================
# Quick Revision
# =============================================================================

print("\n13. QUICK REVISION")
print("-" * 40)

revision = [
    ("class MyError(Exception)", "Create custom exception"),
    ("raise MyError()", "Raise custom exception"),
    ("except MyError", "Handle custom exception"),
    ("super().__init__", "Pass message to Exception"),
]

for concept, meaning in revision:
    print(f"{concept:<28} → {meaning}")


# =============================================================================
# Key Takeaways
# =============================================================================

print("\n14. KEY TAKEAWAYS")
print("-" * 40)

takeaways = [
    "Custom exceptions represent application-specific problems.",
    "Always inherit from Exception.",
    "Meaningful names improve readability.",
    "Custom attributes provide additional context.",
    "Parent exception classes simplify grouped handling."
]

for item in takeaways:
    print(f"✓ {item}")

print("\n" + "=" * 80)
print("End of 08_custom_exceptions.py")
print("=" * 80)