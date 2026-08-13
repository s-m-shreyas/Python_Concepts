# type: ignore

"""
05_post_init.py

Demonstrates the __post_init__ method in a dataclass.

__post_init__ runs after the generated __init__ method.
It is useful for validation or derived calculations.
"""

from dataclasses import dataclass


# ============================================================
# 1. VALIDATION IN __post_init__
# ============================================================

@dataclass
class Book:
    """Book record."""

    title: str
    pages: int

    def __post_init__(self) -> None:
        if self.pages < 0:
            raise ValueError("Pages cannot be negative.")


book = Book("Python Guide", 250)
print(book)

# Book("Invalid", -5)  # raises ValueError

"""
The class validates the data right after initialization.
"""


# ============================================================
# 2. DERIVED VALUES
# ============================================================

@dataclass
class Circle:
    """Circle with radius."""

    radius: float
    area: float = 0.0

    def __post_init__(self) -> None:
        self.area = 3.14 * self.radius * self.radius


c = Circle(5)
print(c.area)

"""
__post_init__ can calculate additional values after the normal
initialization.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - __post_init__ runs after generated __init__
# - it is useful for validation and computed fields
# - it keeps initialization logic centralized and clean
