# type: ignore

"""
02_eq_and_ne.py

Demonstrates __eq__ and __ne__ for equality and inequality.

These methods define how custom objects compare to one another.
"""


# ============================================================
# 1. COMPARING OBJECTS BY VALUE
# ============================================================

class Point:
    """Represents a point in 2D space."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: object) -> bool:
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not result


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(2, 3)

print(p1 == p2)
print(p1 == p3)
print(p1 != p3)

"""
Without __eq__, object identity is used, meaning two separate
objects with the same data would not compare equal.
"""


# ============================================================
# 2. USING EQUALITY FOR BUSINESS LOGIC
# ============================================================

class Product:
    """A simple product model."""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price


p1 = Product("Laptop", 80000)
p2 = Product("Laptop", 80000)
p3 = Product("Phone", 30000)

print(p1 == p2)
print(p1 == p3)

"""
This lets the objects compare by meaningful data rather than by
memory location.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - __eq__ defines equality behavior.
# - __ne__ defines inequality behavior.
# - Custom classes can compare by their attributes instead of object identity.
# - Returning NotImplemented is a standard way to say the comparison is not supported.
