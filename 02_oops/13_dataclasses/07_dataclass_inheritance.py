# type: ignore

"""
07_dataclass_inheritance.py

Demonstrates dataclass inheritance.

Dataclasses can inherit from other dataclasses and extend fields.
"""

from dataclasses import dataclass


# ============================================================
# 1. BASE DATACLASS
# ============================================================

@dataclass
class Employee:
    """Base employee model."""

    name: str
    department: str


# ============================================================
# 2. SUBCLASS DATACLASS
# ============================================================

@dataclass
class Manager(Employee):
    """A manager is also an employee."""

    level: str


manager = Manager("Ravi", "Engineering", "Senior")
print(manager)

"""
The subclass adds a new field while still inheriting the parent fields.
"""


# ============================================================
# 3. OVERRIDING DEFAULTS
# ============================================================

@dataclass
class Person:
    """A person with a default role."""

    name: str
    age: int = 18


@dataclass
class Student(Person):
    """A student extends a person."""

    grade: str = "A"


student = Student("Asha")
print(student)

"""
Dataclass inheritance preserves common fields and allows extension.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - dataclasses work naturally with inheritance
# - subclass fields are added on top of base fields
# - this supports clean modeling of related data objects
