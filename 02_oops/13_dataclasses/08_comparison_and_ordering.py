# type: ignore

"""
08_comparison_and_ordering.py

Demonstrates dataclass comparison and ordering.

Setting order=True generates comparison methods such as __lt__,
__le__, __gt__, and __ge__.
"""

from dataclasses import dataclass


# ============================================================
# 1. ORDERED DATACLASS
# ============================================================

@dataclass(order=True)
class Person:
    """Person ordered by age."""

    age: int
    name: str


p1 = Person(25, "Alice")
p2 = Person(30, "Bob")

print(p1 < p2)
print(p1 > p2)
print(sorted([p2, p1]))

"""
The dataclass compares objects by the field order defined in the class.
"""


# ============================================================
# 2. COMPARISON AND REPR
# ============================================================

@dataclass
class TeamMember:
    """A team member."""

    name: str
    score: int


member_1 = TeamMember("Asha", 10)
member_2 = TeamMember("Asha", 10)

print(member_1 == member_2)
print(repr(member_1))

"""
Even without order=True, dataclasses already compare by value.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - dataclasses generate comparison logic by default for equality
# - order=True adds ordering methods
# - this makes dataclass objects easy to sort and compare
# - it is useful for value-like domain objects
