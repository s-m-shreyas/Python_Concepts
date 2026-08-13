# type: ignore

"""
04_composition_vs_inheritance.py

Compares composition and inheritance.

Inheritance models an is-a relationship.
Composition models a has-a relationship.
"""


# ============================================================
# 1. INHERITANCE: IS-A RELATIONSHIP
# ============================================================

class Animal:
    """A generic animal."""

    def move(self) -> None:
        print("Animal moves.")


class Dog(Animal):
    """A dog is an animal."""

    def bark(self) -> None:
        print("Dog barks.")


dog = Dog()
dog.move()
dog.bark()

"""
Dog inherits from Animal, so it is an Animal.
This is the is-a relationship.
"""


# ============================================================
# 2. COMPOSITION: HAS-A RELATIONSHIP
# ============================================================

class Engine:
    """A car engine."""

    def start(self) -> None:
        print("Engine starts.")


class Car:
    """A car has an engine."""

    def __init__(self) -> None:
        self.engine = Engine()

    def start(self) -> None:
        self.engine.start()


car = Car()
car.start()

"""
Car does not inherit from Engine.
It simply contains an Engine and uses it.
This is the has-a relationship.
"""


# ============================================================
# 3. WHEN TO CHOOSE WHICH
# ============================================================

# Use inheritance when:
# - the child really is a specialized form of the parent
# - the relationship is naturally hierarchical

# Use composition when:
# - behavior is assembled from independent parts
# - you want flexibility and easier change
# - you want to avoid deep inheritance trees


# ============================================================
# 4. PRACTICAL EXAMPLE
# ============================================================

class Calculator:
    """Reusable calculator behavior."""

    def add(self, a: int, b: int) -> int:
        return a + b


class Report:
    """A report uses a Calculator."""

    def __init__(self) -> None:
        self.calculator = Calculator()

    def generate_total(self, a: int, b: int) -> int:
        return self.calculator.add(a, b)


report = Report()
print(report.generate_total(5, 7))

"""
The report benefits from reusable calculator logic through
composition rather than inheritance.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - Inheritance models is-a.
# - Composition models has-a.
# - Composition is often more flexible and maintainable.
# - Use inheritance for true specialization.
# - Use composition for reusable building blocks.
