# type: ignore

"""
01_public_members.py

Demonstrates public members in Python classes.

A public attribute or method is one that has no underscore prefix.
This means it is accessible directly from outside the class.

In Python, public members are the default behavior.
"""


# ============================================================
# 1. SIMPLE PUBLIC ATTRIBUTE
# ============================================================

class Student:
    """Represent a student."""

    def __init__(self, name: str, marks: int) -> None:
        self.name = name
        self.marks = marks


student = Student("Alice", 90)

print(student.name)
print(student.marks)

"""
This is a public attribute because there is no underscore.
Anyone can read or modify it.
"""


# ============================================================
# 2. PUBLIC METHOD
# ============================================================

class Calculator:
    """A simple calculator class."""

    def add(self, a: int, b: int) -> int:
        return a + b


calc = Calculator()
print(calc.add(5, 7))

"""
The add() method is public and can be called from anywhere.
This is the default design in Python.
"""


# ============================================================
# 3. DIRECT MODIFICATION IS ALLOWED
# ============================================================

class BankAccount:
    """A bank account with a public balance."""

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance


account = BankAccount("Rahul", 1500.0)
account.balance = 5000.0

print(account.balance)

"""
This works because balance is public.
Python does not stop us from assigning a new value directly.
This can be useful for simple code, but it is not always safe.
"""


# ============================================================
# 4. WHY PUBLIC MEMBERS ARE NOT STRONG ENCAPSULATION
# ============================================================

class Product:
    """Represent a product."""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


p = Product("Laptop", 80000)

p.price = -500
print(p.price)

"""
The value becomes negative because the price is public.
There is no validation guard.
This is a common reason to use methods or protected/private
members when designing a class.
"""


# ============================================================
# 5. PUBLIC MEMBERS IN EVERYDAY PYTHON
# ============================================================

class User:
    """A simple user class."""

    def __init__(self, username: str) -> None:
        self.username = username


user = User("shreyas")
print(user.username)
user.username = "new_user"
print(user.username)

"""
This is valid and perfectly normal in Python.
Because the attribute is public, direct access is allowed.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - Public members are the default in Python.
# - They are easy to access and simple to use.
# - They do not enforce any restrictions.
# - Direct modification can lead to invalid states.
# - Good design often uses methods to validate and control access.
