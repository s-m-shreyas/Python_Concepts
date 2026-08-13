# type: ignore

"""
03_read_only_properties.py

Demonstrates read-only properties.

A read-only property has a getter but no setter, so outside code
can read the value but cannot assign to it directly.
"""


# ============================================================
# 1. READ-ONLY PROPERTY
# ============================================================

class Book:
    """Represent a book."""

    def __init__(self, title: str, pages: int) -> None:
        self._title = title
        self._pages = pages

    @property
    def title(self) -> str:
        """Return the title."""
        return self._title

    @property
    def pages(self) -> int:
        """Return the number of pages."""
        return self._pages


book = Book("Python Basics", 250)
print(book.title)
print(book.pages)

"""
The values are readable, but there is no setter.
So outside code cannot change them directly.
"""


# ============================================================
# 2. TRYING TO ASSIGN A READ-ONLY PROPERTY
# ============================================================

# book.title = "New Title"  # raises AttributeError

"""
This is because there is no setter defined for title.
The property is intentionally read-only.
"""


# ============================================================
# 3. WHEN READ-ONLY PROPERTIES ARE USEFUL
# ============================================================

class Account:
    """Account with a read-only creation date."""

    def __init__(self, balance: float, created_on: str) -> None:
        self._balance = balance
        self._created_on = created_on

    @property
    def created_on(self) -> str:
        return self._created_on

    @property
    def balance(self) -> float:
        return self._balance


account = Account(1000.0, "2026-08-13")
print(account.created_on)
print(account.balance)

# account.created_on = "2026-08-14"  # not allowed

"""
This kind of property is useful when a value should never change
once the object is created.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - Read-only properties have getter logic, but no setter.
# - They prevent accidental mutation.
# - They are useful for values that should remain constant.
# - They improve encapsulation and design clarity.
