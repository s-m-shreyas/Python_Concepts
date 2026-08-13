# type: ignore

"""
02_getter_and_setter.py

Demonstrates getter and setter methods using the @property
decorator.

The property getter reads the value and the setter assigns it,
allowing logic such as validation and transformation.
"""


# ============================================================
# 1. PROPERTY WITH GETTER AND SETTER
# ============================================================

class Student:
    """Student with a property for name."""

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        """Get the student's name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the student's name."""
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value


student = Student("Priya")
print(student.name)

student.name = "Meera"
print(student.name)

"""
Reading and writing student.name uses the property methods.
This means we can validate assignments before storing them.
"""


# ============================================================
# 2. THE SETTER CAN ENFORCE RULES
# ============================================================

class Employee:
    """Employee model."""

    def __init__(self, salary: float) -> None:
        self._salary = salary

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value


emp = Employee(45000.0)
print(emp.salary)

emp.salary = 48000.0
print(emp.salary)

# emp.salary = -1000  # raises ValueError

"""
This prevents invalid object state and centralizes validation.
"""


# ============================================================
# 3. WHY GETTERS AND SETTERS MATTER
# ============================================================

# - They allow controlled updates.
# - They can validate data.
# - They can transform values before storing them.
# - They improve encapsulation while keeping object access simple.

# This is often better than exposing raw attributes publicly.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - getter: reads the value
# - setter: validates and writes the value
# - properties keep a clean API while protecting internal state
# - setters are useful for enforcing object invariants
