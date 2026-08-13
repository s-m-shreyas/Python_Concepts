# type: ignore

"""
01_abstract_base_classes.py

Demonstrates abstract base classes (ABCs) in Python.

An abstract base class is a class that is meant to be inherited
from, not directly instantiated.

It defines a common interface or contract that subclasses should
implement.
"""

from abc import ABC, abstractmethod


# ============================================================
# 1. BASIC ABSTRACT BASE CLASS
# ============================================================

class Shape(ABC):
    """Base class for different shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass


"""
Shape cannot be instantiated because it includes abstract methods.
"""

# Uncommenting the next line will raise TypeError:
# shape = Shape()


# ============================================================
# 2. CONCRETE SUBCLASS
# ============================================================

class Rectangle(Shape):
    """Rectangle implementation of Shape."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


rect = Rectangle(4, 5)
print(rect.area())
print(rect.perimeter())

"""
Rectangle implements the required abstract methods, so it is a
concrete class and can be instantiated.
"""


# ============================================================
# 3. MULTIPLE CONCRETE CLASSES
# ============================================================

class Circle(Shape):
    """Circle implementation of Shape."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius


circle = Circle(3)
print(circle.area())
print(circle.perimeter())

"""
Different concrete classes can share the same interface while
using different logic behind the scenes.
"""


# ============================================================
# 4. WHY ABCS ARE USEFUL
# ============================================================

# - They define a common contract.
# - They ensure required behavior is implemented.
# - They reduce inconsistent class design.
# - They help enforce standards in large programs.

# Example concept:
# Every shape must provide area() and perimeter().
# A shape that does not implement these cannot be instantiated.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - ABCs are used to define a general interface.
# - They cannot be instantiated directly.
# - Subclasses must implement the abstract methods.
# - This creates consistency across related classes.
# - ABCs help design scalable, maintainable systems.
