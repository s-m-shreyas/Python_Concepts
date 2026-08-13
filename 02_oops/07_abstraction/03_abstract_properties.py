# type: ignore

"""
03_abstract_properties.py

Demonstrates abstract properties in Python.

A property may also be defined as abstract in an abstract base
class. This means every subclass must provide a real property
implementation.
"""

from abc import ABC, abstractmethod


# ============================================================
# 1. ABSTRACT PROPERTY DEFINITION
# ============================================================

class Employee(ABC):
    """Abstract employee base class."""

    @property
    @abstractmethod
    def salary(self) -> float:
        """Return the salary for the employee."""
        pass


# ============================================================
# 2. SUBCLASS IMPLEMENTS A CONCRETE PROPERTY
# ============================================================

class FullTimeEmployee(Employee):
    """Concrete employee with salary property."""

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


employee = FullTimeEmployee(60000.0)
print(employee.salary)

employee.salary = 65000.0
print(employee.salary)

"""
The property exists in the base class as a contract.
The subclass provides a working implementation.
"""


# ============================================================
# 3. REMAINING ABSTRACT IF PROPERTY IS NOT DEFINED
# ============================================================

# class ContractEmployee(Employee):
#     pass
#
# This class would remain abstract because salary is not implemented.

"""
The property acts like a requirement. Unless the subclass defines
it, the class cannot become concrete.
"""


# ============================================================
# 4. ABSTRACT PROPERTY WITH VALIDATION
# ============================================================

class Intern(Employee):
    """Example of a subclass that validates salary."""

    def __init__(self, salary: float) -> None:
        self._salary = salary

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value < 0:
            raise ValueError("Intern salary cannot be negative.")
        self._salary = value


intern = Intern(30000.0)
print(intern.salary)

# intern.salary = -5
# This will raise ValueError.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - Abstract properties define required attribute contracts.
# - Subclasses must implement them to become concrete.
# - They support validation and consistency.
# - They are useful when many related classes need the same field.
# - They improve design clarity and maintainability.
