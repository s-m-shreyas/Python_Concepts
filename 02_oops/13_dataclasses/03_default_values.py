# type: ignore

"""
03_default_values.py

Demonstrates default values in dataclasses.

Fields can have defaults so the dataclass constructor stays flexible.
"""

from dataclasses import dataclass


# ============================================================
# 1. DEFAULT VALUE FOR A FIELD
# ============================================================

@dataclass
class User:
    """User profile."""

    username: str
    active: bool = True
    role: str = "member"


user_1 = User("sanjay")
user_2 = User("meera", False, "admin")

print(user_1)
print(user_2)

"""
The fields active and role have default values, so they are optional
when creating an instance.
"""


# ============================================================
# 2. DEFAULTS CAN BE OVERIDDEN
# ============================================================

@dataclass
class Book:
    """A book record."""

    title: str
    pages: int = 200


book = Book("Python Guide", 350)
print(book)

print(Book("Another Book"))

"""
The default pages value is used if no value is provided.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - dataclass fields can have defaults
# - default values make constructors more convenient
# - defaults reduce the need for custom __init__ logic
# - later arguments can override the defaults
