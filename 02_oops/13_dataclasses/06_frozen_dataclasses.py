# type: ignore

"""
06_frozen_dataclasses.py

Demonstrates frozen dataclasses.

A frozen dataclass is immutable: existing values cannot be changed
after creation.
"""

from dataclasses import dataclass


# ============================================================
# 1. FROZEN DATACLASS
# ============================================================

@dataclass(frozen=True)
class Point:
    """Immutable point.
    """

    x: int
    y: int


point = Point(3, 4)
print(point)

# point.x = 10  # raises FrozenInstanceError

"""
Frozen dataclasses prevent mutation after creation.
This is useful for value objects.
"""


# ============================================================
# 2. HASHABLE BY DEFAULT
# ============================================================

points = {Point(1, 2), Point(3, 4), Point(1, 2)}
print(points)

"""
Because Point is frozen and hashable, it can be used in sets.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - frozen=True makes dataclass instances immutable
# - it is useful for fixed values and safer designs
# - immutable objects work well in sets and as dictionary keys
