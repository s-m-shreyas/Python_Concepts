# type: ignore

"""
04_field_function.py

Demonstrates the dataclasses.field() helper.

field() gives more control over default values and metadata.
"""

from dataclasses import dataclass, field


# ============================================================
# 1. DEFAULT FACTORY
# ============================================================

@dataclass
class Team:
    """A team with a list of members."""

    members: list[str] = field(default_factory=list)


team_1 = Team()
team_2 = Team(["Riya", "Sam"])

print(team_1)
print(team_2)

"""
default_factory=list creates a fresh list for each instance.
This avoids sharing a mutable default across objects.
"""


# ============================================================
# 2. METADATA
# ============================================================

@dataclass
class Employee:
    """Employee record."""

    name: str
    department: str = field(default="Engineering", metadata={"source": "HR"})


emp = Employee("Nina")
print(emp)
print(emp.department)
print(Employee.__dataclass_fields__["department"].metadata)

"""
field() can attach metadata to a dataclass field.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - field() is useful for custom default behavior
# - default_factory solves mutable default bug patterns
# - metadata can store extra information about fields
# - it gives more control than plain defaults
