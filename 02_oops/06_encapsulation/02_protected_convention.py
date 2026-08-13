# type: ignore

"""
02_protected_convention.py

Demonstrates the protected-member convention in Python.

A protected member is usually identified by a single leading
underscore, such as _salary or _internal_data.

This does not enforce strict access control, but it signals to
other developers that the member is intended for internal use.
"""


# ============================================================
# 1. PROTECTED ATTRIBUTE
# ============================================================

class Employee:
    """Employee with a protected salary attribute."""

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self._salary = salary

    def get_salary(self) -> float:
        """Return the protected salary."""
        return self._salary


employee = Employee("Amit", 50000.0)
print(employee.name)
print(employee.get_salary())

"""
_salary is protected by convention.
It means: "this is internal and should not be used freely
outside the class".
"""


# ============================================================
# 2. PROTECTED MEMBERS ARE STILL ACCESSIBLE
# ============================================================

employee._salary = 60000.0
print(employee.get_salary())

"""
This direct assignment is technically allowed in Python.
The single underscore is only a warning signal, not a blocker.
"""


# ============================================================
# 3. SUBCLASSES MAY USE PROTECTED MEMBERS
# ============================================================

class Manager(Employee):
    """A manager can use the protected salary field."""

    def give_bonus(self, amount: float) -> None:
        self._salary += amount


manager = Manager("Neha", 70000.0)
manager.give_bonus(5000.0)
print(manager.get_salary())

"""
A subclass is allowed to work with the protected member because
it is part of the class hierarchy and is intended for inheritance.
"""


# ============================================================
# 4. PROTECTED METHODS
# ============================================================

class Order:
    """Example of a protected method."""

    def __init__(self, total: float) -> None:
        self.total = total

    def calculate_tax(self) -> float:
        return self._compute_tax()

    def _compute_tax(self) -> float:
        return self.total * 0.18


order = Order(1000.0)
print(order.calculate_tax())

"""
_compute_tax() is protected because it is designed for internal
operation. The public method calculate_tax() provides access.
"""


# ============================================================
# 5. WHY THIS CONVENTION EXISTS
# ============================================================

# - It communicates intent.
# - It warns other developers not to use it directly.
# - It allows subclasses to work with internal data.
# - It provides a middle ground between public and private access.

# Just because a name begins with one underscore does not mean it
# is truly hidden. It is a recommendation, not a security barrier.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - _name is a protected naming convention.
# - It signals internal or inherited usage.
# - It does not strictly restrict access.
# - It is useful for class design and teamwork.
# - It encourages cleaner interfaces and controlled access.
