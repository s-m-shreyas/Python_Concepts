# type: ignore

"""
01_has_a_relationship.py

Demonstrates the "has-a" relationship in object-oriented design.

A class has-a relationship means one object contains another object
as a component or collaborator.
"""


# ============================================================
# 1. HAS-A RELATIONSHIP
# ============================================================

class Engine:
    """Represents a car engine."""

    def start(self) -> None:
        print("Engine started.")


class Car:
    """A car contains an engine."""

    def __init__(self) -> None:
        self.engine = Engine()

    def start(self) -> None:
        print("Car is starting...")
        self.engine.start()


car = Car()
car.start()

"""
This is a classic has-a relationship:
    Car has an Engine.
The engine is a separate object used by the car.
"""


# ============================================================
# 2. MULTIPLE COMPONENTS
# ============================================================

class Wheel:
    """A wheel object."""

    def rotate(self) -> None:
        print("Wheel rotates.")


class Bicycle:
    """A bicycle has wheels."""

    def __init__(self) -> None:
        self.front_wheel = Wheel()
        self.rear_wheel = Wheel()

    def ride(self) -> None:
        print("Bicycle is moving.")
        self.front_wheel.rotate()
        self.rear_wheel.rotate()


bike = Bicycle()
bike.ride()

"""
The bicycle is made of smaller objects that work together.
"""


# ============================================================
# 3. WHY THIS MATTERS
# ============================================================

# - Objects often depend on other objects.
# - The relationship is structural, not inheritance-based.
# - This helps group behavior into manageable components.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - Has-a relationship = one object contains another object.
# - This is common in real systems.
# - It encourages modular design.
# - It is different from is-a inheritance.
