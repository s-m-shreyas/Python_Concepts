# type: ignore

"""
04_name_mangling.py

Demonstrates Python name mangling.

When a method or attribute begins with two underscores and does
not end with two underscores, Python internally rewrites its
name to include the class name.

This prevents accidental overriding between parent and child
classes with the same attribute or method name.
"""


# ============================================================
# 1. BASIC NAME MANGLING
# ============================================================

class Parent:
    """Parent class with a private method."""

    def __secret(self) -> str:
        """Return a private parent message."""
        return "Parent secret"

    def public_method(self) -> str:
        """Call the parent-private method."""
        return self.__secret()


class Child(Parent):
    """Child class with a different private method."""

    def __secret(self) -> str:
        """Return a private child message."""
        return "Child secret"


parent = Parent()
child = Child()

print(parent.public_method())
print(child.public_method())

# The child class does not override the parent's private method.
# Their names are stored differently internally.

print(parent._Parent__secret())
print(child._Child__secret())


# ============================================================
# 2. WHY THIS MATTERS
# ============================================================

# Both classes can define __secret without colliding.
# Python renames them to:
#   Parent._Parent__secret
#   Child._Child__secret

# This is especially useful in large inheritance hierarchies,
# where separate classes may accidentally use the same private
# name for different implementation details.


# ============================================================
# 3. NAME MANGLING FOR ATTRIBUTES
# ============================================================

class A:
    """First class."""

    def __init__(self) -> None:
        self.__value = 10


class B:
    """Second class."""

    def __init__(self) -> None:
        self.__value = 20


obj_a = A()
obj_b = B()

print(obj_a._A__value)
print(obj_b._B__value)


# ============================================================
# INTERVIEW NOTE
# ============================================================

# Name mangling is not a replacement for good design.
# It helps avoid accidental collisions between classes,
# but proper encapsulation still depends on how the class is
# designed and how its interfaces are exposed.
