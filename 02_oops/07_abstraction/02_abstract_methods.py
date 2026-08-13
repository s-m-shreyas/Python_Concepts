# type: ignore

"""
02_abstract_methods.py

Demonstrates abstract methods in Python.

An abstract method is a method declared in a base class without
an implementation. It acts as a required behaviour contract for
all subclasses.
"""

from abc import ABC, abstractmethod


# ============================================================
# 1. BUILDING A BASE CLASS WITH AN ABSTRACT METHOD
# ============================================================

class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self) -> str:
        """Return the sound the animal makes."""
        pass


# ============================================================
# 2. A CONCRETE SUBCLASS MUST IMPLEMENT IT
# ============================================================

class Dog(Animal):
    """Dog subclass."""

    def sound(self) -> str:
        return "Bark"


class Cat(Animal):
    """Cat subclass."""

    def sound(self) -> str:
        return "Meow"


animals = [Dog(), Cat()]

for animal in animals:
    print(type(animal).__name__, "->", animal.sound())

"""
Both Dog and Cat implement sound().
The abstract method ensures that each subclass exposes the same
interface but with different behaviour.
"""


# ============================================================
# 3. REMAINING ABSTRACT IF NOT IMPLEMENTED
# ============================================================

# class Bird(Animal):
#     pass
#
# This would raise TypeError because Bird is still abstract.

"""
A subclass remains abstract until all abstract methods are
implemented.
"""


# ============================================================
# 4. ABSTRACT METHOD WITH DIFFERENT IMPLEMENTATIONS
# ============================================================

class Vehicle(ABC):
    """Abstract vehicle class."""

    @abstractmethod
    def start(self) -> str:
        """Start the vehicle."""
        pass


class Car(Vehicle):
    """Electric car implementation."""

    def start(self) -> str:
        return "Car starts with a key"


class Bike(Vehicle):
    """Bike implementation."""

    def start(self) -> str:
        return "Bike starts with a kick"


vehicles = [Car(), Bike()]

for vehicle in vehicles:
    print(vehicle.start())

"""
Same abstract method name, different real implementation.
This is a core idea behind polymorphism.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - Abstract methods define required behavior.
# - Subclasses must implement them to become concrete.
# - They enforce a common interface across class families.
# - They support polymorphic design.
# - They help keep class hierarchies consistent.
