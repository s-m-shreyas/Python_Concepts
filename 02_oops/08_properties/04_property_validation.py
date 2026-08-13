# type: ignore

"""
04_property_validation.py

Demonstrates property validation.

Properties are often used to validate values before assigning them
to private attributes.
"""


# ============================================================
# 1. VALIDATING RANGE
# ============================================================

class Person:
    """Person with a validated age property."""

    def __init__(self, age: int) -> None:
        self._age = 0
        self.age = age

    @property
    def age(self) -> int:
        """Return the person's age."""
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Age cannot be negative.")
        if value > 120:
            raise ValueError("Age seems unrealistic.")
        self._age = value


p = Person(25)
print(p.age)

# Person(-1)  # raises ValueError
# Person(500) # raises ValueError

"""
This ensures that the object never receives invalid age values.
"""


# ============================================================
# 2. VALIDATING STRING INPUT
# ============================================================

class User:
    """User with validated username."""

    def __init__(self, username: str) -> None:
        self._username = ""
        self.username = username

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Username cannot be empty.")
        self._username = value.strip()


user = User("  shreyas  ")
print(user.username)

"""
The setter applies normalization while protecting against invalid
empty input.
"""


# ============================================================
# 3. WHY VALIDATION MATTERS
# ============================================================

# - It keeps object state consistent.
# - It prevents invalid values.
# - It centralizes checks in one place.
# - It makes the class easier to reason about.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - Properties can be used for validation.
# - They help preserve valid object state.
# - They improve encapsulation without annoying object access syntax.
# - They are a cleaner alternative to exposing raw attributes.
