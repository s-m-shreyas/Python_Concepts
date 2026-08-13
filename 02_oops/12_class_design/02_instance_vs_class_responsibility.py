# type: ignore

"""
02_instance_vs_class_responsibility.py

Demonstrates the difference between instance responsibilities and
class-level responsibilities.
"""


# ============================================================
# 1. INSTANCE METHOD
# ============================================================

class User:
    """A user object."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> None:
        """Operate on one user instance."""
        print(f"Hello, {self.name}!")


user = User("Riya")
user.greet()

"""
The greet() method works on one particular user object.
It is an instance responsibility.
"""


# ============================================================
# 2. CLASS METHOD
# ============================================================

class Employee:
    """Employee class with a class-level helper."""

    company_name = "TechCorp"

    @classmethod
    def get_company_name(cls) -> str:
        """Return the class-level company name."""
        return cls.company_name


print(Employee.get_company_name())

"""
This method does not depend on a single instance.
It works at the class level.
"""


# ============================================================
# 3. STATIC METHOD
# ============================================================

class MathHelper:
    """Utility functions."""

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b


print(MathHelper.add(5, 7))

"""
This operates without any instance or class state.
It is a general utility responsibility.
"""


# ============================================================
# 4. WHY THIS DISTINCTION MATTERS
# ============================================================

# - Instance methods use per-object state.
# - Class methods are shared across the class.
# - Static methods are independent helpers.
# - Class design becomes clearer when responsibilities are separated correctly.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - instance methods: operate on specific objects
# - class methods: operate on class-level data
# - static methods: do not rely on instance or class state
# - proper responsibility assignment improves clarity
