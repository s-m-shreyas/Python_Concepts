# type: ignore

"""
03_inheritance_vs_composition.py

Explains when to use inheritance and when to use composition.
"""


# ============================================================
# 1. INHERITANCE: IS-A RELATIONSHIP
# ============================================================

class Animal:
    """Base animal model."""

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
Dog subclasses Animal, so it naturally fits the is-a model.
"""


# ============================================================
# 2. COMPOSITION: HAS-A RELATIONSHIP
# ============================================================

class Engine:
    """Engine component."""

    def start(self) -> None:
        print("Engine started.")


class Car:
    """A car has an engine."""

    def __init__(self) -> None:
        self.engine = Engine()

    def start(self) -> None:
        self.engine.start()


car = Car()
car.start()

"""
A car is not an engine. It merely contains one.
This is composition.
"""


# ============================================================
# 3. WHICH TO CHOOSE?
# ============================================================

# Prefer inheritance when:
# - the subclass truly specializes the parent
# - the relationship is naturally hierarchical

# Prefer composition when:
# - you need reusable building blocks
# - the relationship is more about containing or using another object
# - you want flexibility and less coupling


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - inheritance models is-a
# - composition models has-a
# - use inheritance carefully
# - composition is often more flexible and maintainable
# - choose based on the actual relationship, not convenience
