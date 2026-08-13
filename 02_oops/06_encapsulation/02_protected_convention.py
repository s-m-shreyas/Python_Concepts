# type: ignore

"""
02_protected_convention.py

Demonstrates the protected-member convention in Python.

A single leading underscore, such as _salary, is a convention.
It tells other developers that the attribute or method is
intended for internal use and should not be accessed directly
outside the class.

Python does not enforce it strongly. It is a design signal,
not a hard restriction.
"""


# ============================================================
# 1. PROTECTED ATTRIBUTE
# ============================================================

class Employee:
    """Represent an employee with a protected salary field."""

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self._salary = salary

    def get_salary(self) -> float:
        """Return the employee salary."""
        return self._salary

    def _apply_bonus(self, bonus: float) -> None:
        """Internal helper for salary adjustment."""
        self._salary += bonus


employee = Employee("Rahul", 50000.0)
print(employee.name)
print(employee.get_salary())

# The attribute is still accessible, but it is considered
# protected and intended for internal use.
employee._salary = 55000.0
print(employee.get_salary())


# ============================================================
# 2. SUBCLASS CAN USE PROTECTED MEMBERS
# ============================================================

class Manager(Employee):
    """A manager who can apply a bonus internally."""

    def give_bonus(self, amount: float) -> float:
        self._apply_bonus(amount)
        return self._salary


manager = Manager("Priya", 70000.0)
print(manager.give_bonus(5000.0))


# ============================================================
# 3. WHY THIS CONVENTION EXISTS
# ============================================================

# A single underscore communicates intent.
# It says: "This is internal to the class or its subclasses."
# It does not completely block access, but it discourages use.

# ============================================================
# INTERVIEW NOTE
# ============================================================

# Using _name is a convention, not a security measure.
# It is helpful for readability and team collaboration.
# Developers should avoid direct access unless necessary.
