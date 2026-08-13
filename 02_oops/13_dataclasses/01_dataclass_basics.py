# type: ignore

"""
01_dataclass_basics.py

Demonstrates the basics of Python dataclasses.

A dataclass is a convenient way to create classes intended mainly
for storing data. Python generates boilerplate methods such as
__init__, __repr__, and __eq__ automatically.
"""

from dataclasses import dataclass


# ============================================================
# 1. BASIC DATACLASS
# ============================================================

@dataclass
class Person:
    """Represents a person."""

    name: str
    age: int


person = Person("Alice", 25)
print(person)
print(person.name)
print(person.age)

"""
The dataclass automatically creates an __init__ method.
We can create Person("Alice", 25) without writing a constructor manually.
"""


# ============================================================
# 2. GENERATED __repr__
# ============================================================

print(repr(person))

"""
Dataclasses also generate a readable __repr__ so objects print
clearly in debugging and logs.
"""


# ============================================================
# 3. GENERATED __eq__
# ============================================================

person_2 = Person("Alice", 25)
print(person == person_2)

"""
Two dataclass instances with the same values compare equal by default.
This is a major convenience over regular classes.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - dataclass reduces boilerplate for data-focused classes
# - it auto-generates __init__
# - it auto-generates __repr__
# - it auto-generates __eq__
# - this makes small value objects easy to write and read
