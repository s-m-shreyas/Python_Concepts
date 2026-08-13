# type: ignore

"""
01_property_function.py

Demonstrates how the @property decorator works in Python.

A property lets us expose a method as if it were an attribute.
In other words, we can call getter logic without needing explicit
method syntax like obj.get_name().
"""


# ============================================================
# 1. SIMPLE PROPERTY EXAMPLE
# ============================================================

class Student:
    """Represent a student."""

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        """Return the student's name."""
        return self._name


student = Student("Alice")
print(student.name)

"""
Calling student.name triggers the property getter.
The value is not stored directly as a public attribute; it is
exposed through a controlled method.
"""


# ============================================================
# 2. EXTERNAL CODE DOES NOT CALL A METHOD
# ============================================================

class Employee:
    """Employee with a property-based interface."""

    def __init__(self, employee_id: int) -> None:
        self._employee_id = employee_id

    @property
    def employee_id(self) -> int:
        return self._employee_id


a = Employee(101)
print(a.employee_id)

"""
This reads cleanly and naturally:
    a.employee_id
rather than:
    a.get_employee_id()
"""


# ============================================================
# 3. PROPERTIES CAN HIDE INTERNAL STORAGE
# ============================================================

class Circle:
    """A circle represented with a radius."""

    def __init__(self, radius: float) -> None:
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius


c = Circle(5.5)
print(c.radius)

"""
The actual storage is _radius, but the class exposes a clean,
readable radius property.
"""


# ============================================================
# 4. WHY THIS IS USEFUL
# ============================================================

# - The class interface is cleaner.
# - Internal data can be renamed later without changing external code.
# - We can add logic before returning data.
# - It improves encapsulation without making access awkward.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - @property creates a getter-style method that behaves like an attribute.
# - It gives a clean interface from outside the class.
# - It allows you to hide internal implementation details.
# - It is a common Python pattern for controlled access.
