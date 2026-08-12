# type: ignore
"""
03_attributes_and_methods.py

Introduces attributes and methods as the mechanisms used to
represent object state and behavior.

This file focuses on:

    - Attributes
    - Methods
    - Accessing attributes
    - Calling methods
    - Object attributes vs behavior
    - Attribute access using dot notation
    - The relationship between state, attributes, and methods

Custom classes are intentionally introduced only where
necessary to demonstrate attributes and methods.

Detailed instance attributes, class attributes, namespaces,
and method binding are covered in later files.
"""


# ============================================================
# 1. ATTRIBUTES REPRESENT OBJECT DATA
# ============================================================

"""
An attribute is a name associated with an object.

Attributes can represent information or state associated
with that object.

For example, strings provide attributes such as:

    real
    imag

for numeric objects such as integers and complex numbers.
"""

number = 10

print(number.real)
print(number.imag)


# ============================================================
# 2. ACCESSING ATTRIBUTES
# ============================================================

"""
Python uses dot notation to access an attribute:

    object.attribute

The object is on the left side of the dot.

The attribute name is on the right side.
"""

number = 10

print(number.real)
print(number.numerator)
print(number.denominator)


# ============================================================
# 3. METHODS ARE CALLABLE ATTRIBUTES
# ============================================================

"""
A method is an attribute that refers to callable behavior
associated with an object.

For example, strings provide methods such as:

    upper()
    lower()
    replace()

The method is accessed using dot notation and then called
using parentheses.
"""

message = "python"

print(message.upper())
print(message.lower())


# ============================================================
# 4. ATTRIBUTE ACCESS VS METHOD CALL
# ============================================================

"""
There is an important distinction:

    object.attribute

accesses an attribute.

    object.method()

accesses an attribute and then calls the resulting callable.

For example:

    message.upper

refers to the method object.

    message.upper()

calls that method.
"""

message = "python"

print(message.upper)
print(message.upper())


# ============================================================
# 5. ATTRIBUTES DO NOT HAVE TO BE METHODS
# ============================================================

"""
Not every attribute represents behavior.

Some attributes represent data.

For example, complex numbers expose:

    real
    imag

These are values rather than methods.
"""

number = 10 + 20j

print(number.real)
print(number.imag)


# ============================================================
# 6. OBJECTS CAN HAVE BOTH DATA AND BEHAVIOR
# ============================================================

"""
An object can expose:

    data attributes
        -> represent information

    methods
        -> represent behavior

For example, a complex number has data attributes such as
real and imag, while a string provides methods such as
upper() and replace().
"""

number = 10 + 20j
message = "python"

print("Real:", number.real)
print("Imaginary:", number.imag)

print("Uppercase:", message.upper())


# ============================================================
# 7. METHODS CAN RECEIVE ARGUMENTS
# ============================================================

"""
Methods can accept arguments just like functions.

For example:

    replace(old, new)

receives the text that should be replaced and its replacement.
"""

message = "Python is powerful"

result = message.replace("powerful", "useful")

print(result)


# ============================================================
# 8. METHODS CAN RETURN VALUES
# ============================================================

"""
Methods can return values.

The returned value can be stored in another variable or used
directly in an expression.
"""

message = "python"

uppercase_message = message.upper()

print(uppercase_message)


# ============================================================
# 9. METHODS CAN MODIFY MUTABLE OBJECTS
# ============================================================

"""
Some methods modify the state of mutable objects.

For example, list.append() modifies the existing list.
"""

numbers = [10, 20, 30]

print("Before:", numbers)

numbers.append(40)

print("After:", numbers)


# ============================================================
# 10. METHODS CAN ALSO RETURN NEW OBJECTS
# ============================================================

"""
Some methods do not modify the original object.

String methods return new strings because strings are
immutable.
"""

message = "python"

result = message.upper()

print("Original:", message)
print("Result:", result)


# ============================================================
# 11. ATTRIBUTES AND METHODS WITH BUILT-IN OBJECTS
# ============================================================

"""
Built-in Python objects already provide many attributes
and methods.

Examples:

    list
        append()
        sort()
        reverse()

    str
        upper()
        lower()
        split()

    dict
        get()
        keys()
        values()
"""

numbers = [30, 10, 20]

numbers.sort()

print(numbers)

message = "Python Programming"

print(message.split())

person = {
    "name": "Shreyas",
    "role": "Data Engineer",
}

print(person.keys())


# ============================================================
# 12. CUSTOM OBJECTS CAN HAVE ATTRIBUTES AND METHODS
# ============================================================

"""
We can create our own objects using classes.

A class defines the structure and behavior that its objects
can have.

This is only a preview.

Classes themselves are covered in detail in:

    02_classes/
"""

class Person:
    """Represent a person with simple data and behavior."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


person = Person()

print(person.greet())


# ============================================================
# 13. AN ATTRIBUTE CAN STORE DATA
# ============================================================

"""
Custom objects can have attributes representing their state.

Here, name is an attribute of the object.

Detailed instance attribute creation and behavior will be
covered in the next file.
"""

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.name)


# ============================================================
# 14. A METHOD CAN USE AN OBJECT'S ATTRIBUTE
# ============================================================

"""
A method can access data associated with its object.

Here:

    self.name

refers to the name attribute belonging to the current object.
"""

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a greeting using the person's name."""
        return f"Hello, {self.name}!"


person = Person("Shreyas")

print(person.greet())


# ============================================================
# 15. STATE THROUGH ATTRIBUTES, BEHAVIOR THROUGH METHODS
# ============================================================

"""
This gives us the basic OOP relationship:

    Object
       |
       +-- Attributes
       |      |
       |      +-- represent state
       |
       +-- Methods
              |
              +-- represent behavior

Example:

    Person
       |
       +-- name
       |
       +-- greet()

The name attribute represents state.

The greet() method represents behavior.
"""

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a greeting."""
        return f"Hello, {self.name}!"


person = Person("Shreyas")

print("State:", person.name)
print("Behavior:", person.greet())


# ============================================================
# 16. DIFFERENT OBJECTS CAN HAVE DIFFERENT ATTRIBUTE VALUES
# ============================================================

"""
Objects created from the same class can have different
attribute values.

The behavior remains defined by the class, while the state
can differ between objects.
"""

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a greeting."""
        return f"Hello, {self.name}!"


first = Person("Shreyas")
second = Person("Rahul")

print(first.name)
print(second.name)

print(first.greet())
print(second.greet())


# ============================================================
# 17. DOT NOTATION
# ============================================================

"""
Dot notation is the standard syntax for accessing attributes
and methods.

General form:

    object.attribute

or:

    object.method()

Examples:

    person.name
    person.greet()
"""

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a greeting."""
        return f"Hello, {self.name}!"


person = Person("Shreyas")

print(person.name)
print(person.greet())


# ============================================================
# 18. ATTRIBUTE ACCESS IS NOT THE SAME AS FUNCTION CALLING
# ============================================================

"""
Consider:

    person.greet

This accesses the method attribute.

Consider:

    person.greet()

This calls the method.

The parentheses perform the call.
"""

class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


person = Person()

greeting_method = person.greet

print(greeting_method)
print(greeting_method())


# ============================================================
# 19. METHODS ARE OBJECTS TOO
# ============================================================

"""
Methods are themselves objects.

Accessing a method without calling it gives us a callable
object.

This reinforces Python's object model:

    Functions are objects.
    Methods are objects.
    Classes are objects.
    Instances are objects.
"""

class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


person = Person()

method = person.greet

print(type(method))
print(callable(method))


# ============================================================
# 20. ATTRIBUTES CAN BE INSPECTED
# ============================================================

"""
Python provides built-in tools for inspecting objects.

dir() returns names associated with an object.

This is useful for exploring available attributes and
methods.
"""

message = "python"

print("upper" in dir(message))
print("lower" in dir(message))
print("replace" in dir(message))


# ============================================================
# 21. ATTRIBUTES AND METHODS FORM THE OBJECT INTERFACE
# ============================================================

"""
The collection of attributes and methods exposed by an object
forms an important part of the way other code interacts with
that object.

For example, a list exposes operations such as:

    append()
    remove()
    sort()

and information such as:

    __class__
    __len__

The detailed meaning of special attributes and methods will
be explored later.
"""

numbers = [10, 20, 30]

print("append" in dir(numbers))
print("sort" in dir(numbers))


# ============================================================
# 22. CONCEPTUAL MODEL
# ============================================================

"""
At this point, we can extend our object model:

    Object
       |
       +-- Identity
       |
       +-- Type
       |
       +-- State
       |     |
       |     +-- Attributes
       |
       +-- Behavior
             |
             +-- Methods

This is the foundation for understanding classes and
instances.

The next file focuses specifically on instance attributes.
"""


# ============================================================
# 23. KEY TAKEAWAYS
# ============================================================

"""
Key concepts:

1. Attributes are names associated with objects.

2. Attributes can represent object data or behavior.

3. Methods are callable attributes associated with objects.

4. Dot notation is used to access attributes and methods.

5. object.attribute accesses an attribute.

6. object.method() accesses and calls a method.

7. Methods can accept arguments.

8. Methods can return values.

9. Methods can modify mutable objects.

10. Methods can also produce new objects.

11. Objects can contain both state and behavior.

12. Custom objects can have attributes and methods.

13. Attributes commonly represent state.

14. Methods commonly represent behavior.

15. Objects created from the same class can have different
    attribute values.

The next file focuses specifically on instance attributes and
how each object can maintain its own state.
"""