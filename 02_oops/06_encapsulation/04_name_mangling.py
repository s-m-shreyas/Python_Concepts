# type: ignore

"""
04_name_mangling.py

Demonstrates Python name mangling.

When a method or attribute begins with two underscores and does
not end with two underscores, Python internally rewrites the
name to include the class name.

This avoids accidental collisions between parent and child class
members that share the same name.
"""


# ============================================================
# 1. NAME MANGLING FOR METHODS
# ============================================================

class Parent:
    """Parent class with a private method."""

    def __secret(self) -> str:
        return "Parent secret"

    def call_secret(self) -> str:
        return self.__secret()


class Child(Parent):
    """Child class with its own private method."""

    def __secret(self) -> str:
        return "Child secret"


parent = Parent()
child = Child()

print(parent.call_secret())
print(child.call_secret())

"""
Although both classes define __secret, they are not the same.
Python stores them as different names internally.
"""

print(parent._Parent__secret())
print(child._Child__secret())


# ============================================================
# 2. ILLUSTRATING THE REAL REWRITING
# ============================================================

class A:
    """Class A."""

    def __init__(self) -> None:
        self.__value = 10


class B:
    """Class B."""

    def __init__(self) -> None:
        self.__value = 20


obj_a = A()
obj_b = B()

print(obj_a._A__value)
print(obj_b._B__value)

"""
Even though both classes use __value, they are kept separate
because Python mangles the names to include the class identity.
"""


# ============================================================
# 3. AVOIDING UNINTENDED OVERWRITING
# ============================================================

class Animal:
    """Base class."""

    def __init__(self) -> None:
        self.__sound = "Generic sound"

    def get_sound(self) -> str:
        return self.__sound


class Dog(Animal):
    """Child class."""

    def __init__(self) -> None:
        self.__sound = "Bark"


dog = Dog()
print(dog.get_sound())
print(dog._Animal__sound)
print(dog._Dog__sound)

"""
The base class and child class can both use __sound without
colliding, because their internal names are different.
"""


# ============================================================
# 4. IMPORTANT LIMITATION
# ============================================================

# Name mangling is not a true security mechanism.
# It helps avoid accidental collisions, not protect data from all
# forms of access.
# A developer can still access the mangled name directly if they
# choose to do so.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# - Python rewrites private names with the class name.
# - This is called name mangling.
# - It prevents accidental method/attribute collision in inheritance.
# - It helps design safer class hierarchies.
# - It is not a substitute for proper API design.
