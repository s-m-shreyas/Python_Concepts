# type: ignore

"""
01_str_and_repr.py

Demonstrates __str__ and __repr__ in Python.

These are special methods used to produce readable string
representations of a custom object.
"""


# ============================================================
# 1. __str__
# ============================================================

class Person:
    """A person object."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """Return a user-friendly string."""
        return f"{self.name} is {self.age} years old."

    def __repr__(self) -> str:
        """Return a developer-friendly representation."""
        return f"Person(name={self.name!r}, age={self.age!r})"


person = Person("Alice", 25)

print(str(person))
print(person)
print(repr(person))

"""
print(person) calls __str__ by default.
repr(person) calls __repr__.

__str__ is meant for readable output.
__repr__ is meant for debugging and developer representation.
"""


# ============================================================
# 2. USING REPR IN A LIST
# ============================================================

people = [Person("Bob", 30), Person("Charlie", 28)]
print(people)

"""
When printing a list of objects, Python uses the repr() of each
object by default.
"""


# ============================================================
# 3. HOW THEY DIFFER
# ============================================================

# __str__ is used for user-facing output.
# __repr__ is used for debugging and unambiguous representation.

# Example:
# str(person) -> Alice is 25 years old.
# repr(person) -> Person(name='Alice', age=25)


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - __str__ is for readability.
# - __repr__ is for debugging and developer clarity.
# - If __str__ is missing, Python falls back to __repr__.
# - Writing good dunder methods makes objects easier to inspect.
