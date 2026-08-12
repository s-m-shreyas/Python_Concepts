# type: ignore
"""
01_objects_and_identity.py

Introduces Python objects and object identity.

This file focuses on:

    - Everything in Python is an object.
    - Objects have identity, type, and value/state.
    - id() exposes an object's identity.
    - type() identifies an object's type.
    - is checks object identity.
    - == checks value equality.

The goal is to understand what an object is before learning
how classes are used to create custom objects.
"""


# ============================================================
# 1. EVERYTHING IN PYTHON IS AN OBJECT
# ============================================================

"""
Python represents data as objects.

Examples of objects include:

    integers
    strings
    lists
    tuples
    functions
    classes
    modules

Variables do not contain the object itself in the conceptual
model. They refer to objects.
"""

number = 42
message = "Hello"
numbers = [10, 20, 30]

print(number)
print(message)
print(numbers)


# ============================================================
# 2. OBJECTS HAVE IDENTITY
# ============================================================

"""
Every object has an identity.

The identity distinguishes one object from another during
that object's lifetime.

Python provides id() to expose an object's identity.
"""

number = 42

print(id(number))


# ============================================================
# 3. OBJECTS HAVE A TYPE
# ============================================================

"""
Every object has a type.

The type determines what kind of object it is and therefore
what operations can be performed on it.

The type() function can be used to inspect an object's type.
"""

number = 42
message = "Hello"
numbers = [10, 20, 30]

print(type(number))
print(type(message))
print(type(numbers))


# ============================================================
# 4. OBJECTS HAVE A VALUE OR STATE
# ============================================================

"""
Objects also have a value or state.

For simple immutable objects, the value can be observed
directly.

For example:

    42
    "Python"
    True

For mutable objects, state can change during the object's
lifetime.
"""

number = 42
message = "Python"

print(number)
print(message)


# ============================================================
# 5. THE OBJECT MODEL
# ============================================================

"""
A useful conceptual model is:

    Object
       |
       +-- Identity
       |
       +-- Type
       |
       +-- Value / State

For example:

    number = 42

The name 'number' refers to an integer object.

That object has:

    Identity -> represented by id(number)
    Type     -> int
    Value    -> 42
"""

number = 42

print("Identity:", id(number))
print("Type:", type(number))
print("Value:", number)


# ============================================================
# 6. TWO NAMES CAN REFER TO THE SAME OBJECT
# ============================================================

"""
Multiple variables can refer to the same object.

The variables are different names, but the object they refer
to can be the same object.
"""

first = [10, 20, 30]
second = first

print(first)
print(second)

print(id(first))
print(id(second))


# ============================================================
# 7. SAME IDENTITY MEANS SAME OBJECT
# ============================================================

"""
Because first and second refer to the same object, their
identities are the same.
"""

first = [10, 20, 30]
second = first

print(id(first) == id(second))


# ============================================================
# 8. THE is OPERATOR
# ============================================================

"""
The 'is' operator checks whether two references point to
the exact same object.

It checks object identity.

    first is second

means:

    "Do first and second refer to the same object?"
"""

first = [10, 20, 30]
second = first

print(first is second)


# ============================================================
# 9. DIFFERENT OBJECTS CAN HAVE EQUAL VALUES
# ============================================================

"""
Two different objects can contain equal values.

Example:

    first = [10, 20, 30]
    second = [10, 20, 30]

The lists contain the same values, but they are separate
list objects.
"""

first = [10, 20, 30]
second = [10, 20, 30]

print(first == second)
print(first is second)


# ============================================================
# 10. == VS is
# ============================================================

"""
The operators answer different questions.

    ==
        Checks equality.

        "Do these objects compare as equal?"


    is
        Checks identity.

        "Are these the exact same object?"
"""

first = [10, 20, 30]
second = [10, 20, 30]
third = first

print(first == second)
print(first is second)

print(first == third)
print(first is third)


# ============================================================
# 11. IDENTITY AND EQUALITY ARE DIFFERENT CONCEPTS
# ============================================================

"""
Two objects can be equal without being identical.

    first == second
        True

    first is second
        False

This means:

    Same value
        does not necessarily mean
    Same object
"""

first = {"language": "Python"}
second = {"language": "Python"}

print(first == second)
print(first is second)


# ============================================================
# 12. ASSIGNMENT CREATES ANOTHER REFERENCE
# ============================================================

"""
Assignment does not necessarily create a new object.

When:

    second = first

Python makes 'second' refer to the object already referenced
by 'first'.
"""

first = [1, 2, 3]
second = first

print(first is second)


# ============================================================
# 13. MODIFYING A SHARED OBJECT
# ============================================================

"""
When two variables refer to the same mutable object, a
modification through one reference is visible through the
other reference.
"""

first = [10, 20, 30]
second = first

first.append(40)

print(first)
print(second)


# ============================================================
# 14. CREATING A SEPARATE OBJECT
# ============================================================

"""
Creating another list with the same values creates a
different list object.
"""

first = [10, 20, 30]
second = [10, 20, 30]

print(first == second)
print(first is second)


# ============================================================
# 15. id() IS NOT A VALUE
# ============================================================

"""
The value returned by id() should not be confused with the
object's actual value.

For example:

    number = 42

The object value is:

    42

The value returned by:

    id(number)

is an identity value supplied by Python.
"""

number = 42

print("Object value:", number)
print("Object identity:", id(number))


# ============================================================
# 16. OBJECT IDENTITY IS VALID DURING THE OBJECT'S LIFETIME
# ============================================================

"""
An object's identity uniquely identifies that object during
its lifetime.

After an object is no longer alive, Python may reuse the
identity value for another object.

Therefore, id() should not normally be used as a permanent
identifier.
"""


# ============================================================
# 17. FUNCTIONS ARE ALSO OBJECTS
# ============================================================

"""
Functions are objects in Python as well.

A function can therefore have:

    identity
    type
    value/state

The function object can be referenced by a variable.
"""


def greet() -> str:
    """Return a greeting message."""
    return "Hello"


print(type(greet))
print(id(greet))
print(greet())


# ============================================================
# 18. CLASSES ARE ALSO OBJECTS
# ============================================================

"""
Classes are objects too.

Classes are instances of a metaclass, which is an advanced
topic covered later.

For now, the important point is simply:

    A class itself is also an object.
"""

class Example:
    """A simple example class."""

    pass


print(type(Example))
print(id(Example))


# ============================================================
# 19. NONE AND IDENTITY
# ============================================================

"""
None is a special singleton object representing the absence
of a value.

Because there is only one None object, identity comparison
with None uses 'is'.

Preferred:

    value is None

rather than:

    value == None
"""

value = None

print(value is None)


# ============================================================
# 20. PRACTICAL OBJECT IDENTITY EXAMPLE
# ============================================================

"""
Consider three variables:

    original
    alias
    copy

original and alias refer to the same object.

copy refers to a separate object containing the same values.
"""

original = [10, 20, 30]
alias = original
copy = [10, 20, 30]

print(original == alias)
print(original is alias)

print(original == copy)
print(original is copy)


# ============================================================
# 21. OBJECT IDENTITY SUMMARY
# ============================================================

"""
For an object:

    identity
        -> distinguishes the object

    type
        -> identifies what kind of object it is

    value / state
        -> represents the object's data

Remember:

    is
        -> identity comparison

    ==
        -> equality comparison

Also remember:

    second = first

does not necessarily create a new object.

It can simply create another reference to the same object.
"""


# ============================================================
# 22. KEY TAKEAWAYS
# ============================================================

"""
Key concepts:

1. Everything in Python is an object.

2. Objects have identity.

3. Objects have a type.

4. Objects have a value or state.

5. id() exposes an object's identity.

6. type() identifies an object's type.

7. Multiple names can refer to the same object.

8. 'is' checks object identity.

9. '==' checks equality.

10. Two different objects can have equal values.

11. Assignment can create another reference instead of
    creating a new object.

12. Functions and classes are objects too.

13. None is a singleton object and should normally be
    compared using 'is'.

This object model forms the foundation for understanding
classes, instances, attributes, methods, inheritance, and
the rest of Python's object-oriented programming model.
"""