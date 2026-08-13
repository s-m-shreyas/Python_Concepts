# type: ignore

"""
04_arithmetic_methods.py

Demonstrates arithmetic dunder methods such as __add__ and __sub__.

These methods allow custom objects to work with operators like +,
-, *, and /.
"""


# ============================================================
# 1. ADDING TWO CUSTOM OBJECTS
# ============================================================

class Vector:
    """A 2D vector."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: object) -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: object) -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)
print(v1 - v2)

"""
The + and - operators now work naturally for custom Vector objects.
"""


# ============================================================
# 2. MULTIPLICATION WITH SCALARS
# ============================================================

class Number:
    """A wrapper around an integer value."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __mul__(self, other: int) -> "Number":
        return Number(self.value * other)

    def __repr__(self) -> str:
        return f"Number({self.value})"


n = Number(5)
print(n * 3)

"""
This allows Number objects to behave like numbers in a limited way.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - __add__ handles +
# - __sub__ handles -
# - __mul__ handles *
# - arithmetic dunder methods allow custom objects to support operator syntax
# - they make custom types feel more natural and Pythonic
