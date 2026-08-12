# type: ignore
"""
07_class_namespace.py

Introduces the class namespace.

This file focuses on:

    - What a class namespace is
    - The class __dict__
    - Attributes stored directly on a class
    - Methods stored in the class namespace
    - Class attributes vs instance attributes
    - Reading the class namespace
    - Modifying class attributes
    - Attribute lookup involving the class namespace
    - Relationship between class and instance namespaces

The previous file covered:

    06_object_namespace.py

Detailed inheritance and method resolution are covered later
in the OOP section.
"""


# ============================================================
# 1. WHAT IS A CLASS NAMESPACE?
# ============================================================

"""
A class also has a namespace.

The class namespace contains names defined directly inside
the class body.

For example:

    class Person:
        species = "Human"

'species' becomes part of the class namespace.
"""


class Person:
    """Represent a person."""

    species = "Human"


print(Person.__dict__)


# ============================================================
# 2. CLASS __dict__
# ============================================================

"""
The class namespace can be inspected through:

    ClassName.__dict__

For ordinary Python classes, this exposes a mapping containing
names defined on the class.
"""


class Person:
    """Represent a person."""

    species = "Human"


print(type(Person.__dict__))
print(Person.__dict__)


# ============================================================
# 3. CLASS ATTRIBUTES APPEAR IN THE CLASS NAMESPACE
# ============================================================

"""
A class attribute defined directly in the class body becomes
an entry in the class namespace.
"""


class Person:
    """Represent a person."""

    species = "Human"
    category = "Mammal"


print(Person.__dict__["species"])
print(Person.__dict__["category"])


# ============================================================
# 4. METHODS ARE STORED IN THE CLASS NAMESPACE
# ============================================================

"""
Methods defined inside a class are also entries in the class
namespace.

The function object is stored under the method's name.
"""


class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


print(Person.__dict__["greet"])


# ============================================================
# 5. METHOD ACCESS THROUGH THE CLASS
# ============================================================

"""
The method can be accessed directly through the class.

At this level, the class contains the function object defined
under the name 'greet'.
"""


class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


print(Person.greet)
print(type(Person.greet))


# ============================================================
# 6. METHOD ACCESS THROUGH AN INSTANCE
# ============================================================

"""
When the same method is accessed through an instance:

    person.greet

Python performs attribute lookup involving the class and
creates a bound method.

This binding behavior will be studied more deeply later.
"""


class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


person = Person()

print(person.greet)
print(type(person.greet))


# ============================================================
# 7. INSTANCE __dict__ VS CLASS __dict__
# ============================================================

"""
Consider:

    class Person:
        species = "Human"

        def __init__(self, name):
            self.name = name

The class namespace contains:

    species
    __init__
    other class-level names

The instance namespace contains:

    name
"""


class Person:
    """Represent a person."""

    species = "Human"

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print("Instance namespace:")
print(person.__dict__)

print("\nClass namespace:")
print(Person.__dict__)


# ============================================================
# 8. INSTANCE ATTRIBUTES DO NOT APPEAR IN THE CLASS NAMESPACE
# ============================================================

"""
The statement:

    self.name = name

runs when an instance is created.

Therefore, 'name' is stored in the instance namespace, not
the class namespace.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print("name" in person.__dict__)
print("name" in Person.__dict__)


# ============================================================
# 9. CLASS ATTRIBUTES DO NOT APPEAR IN THE INSTANCE __dict__
# ============================================================

"""
The opposite is also true.

A class attribute is stored in the class namespace and does
not automatically appear in each instance's namespace.
"""


class Person:
    """Represent a person."""

    species = "Human"


person = Person()

print("species" in person.__dict__)
print("species" in Person.__dict__)


# ============================================================
# 10. ACCESSING A CLASS ATTRIBUTE THROUGH AN INSTANCE
# ============================================================

"""
Even though 'species' is not in the instance namespace,
the instance can access it.

Python can continue attribute lookup on the class.
"""


class Person:
    """Represent a person."""

    species = "Human"


person = Person()

print(person.species)
print(person.__dict__)
print(Person.__dict__["species"])


# ============================================================
# 11. CLASS ATTRIBUTE LOOKUP
# ============================================================

"""
A simplified model of:

    person.species

is:

    1. Look for 'species' on the instance.
    2. If not found, continue lookup on the class.
    3. Find 'species' in Person's namespace.
"""


class Person:
    """Represent a person."""

    species = "Human"


person = Person()

print("species" in person.__dict__)
print("species" in Person.__dict__)

print(person.species)


# ============================================================
# 12. INSTANCE ATTRIBUTE SHADOWING
# ============================================================

"""
An instance can define an attribute with the same name as a
class attribute.

The instance-level attribute then takes precedence for that
instance.
"""


class Person:
    """Represent a person."""

    species = "Human"


person = Person()

person.species = "Robot"

print(person.species)
print(Person.species)

print(person.__dict__)
print(Person.__dict__["species"])


# ============================================================
# 13. CLASS ATTRIBUTE MODIFICATION
# ============================================================

"""
A class attribute can be modified through the class.

Instances that do not have a shadowing instance attribute
will observe the updated class-level value.
"""


class Person:
    """Represent a person."""

    species = "Human"


first = Person()
second = Person()

Person.species = "Homo sapiens"

print(first.species)
print(second.species)
print(Person.species)


# ============================================================
# 14. CLASS NAMESPACE CAN BE INSPECTED WITHOUT AN INSTANCE
# ============================================================

"""
Because the namespace belongs to the class, it can be
inspected without creating an instance.
"""


class Configuration:
    """Store application configuration."""

    version = "1.0"
    debug = False


print(Configuration.__dict__)


# ============================================================
# 15. CLASS NAMESPACE CONTAINS SPECIAL ATTRIBUTES
# ============================================================

"""
The class namespace contains more than explicitly written
attributes.

Python also creates special class attributes.

Examples include:

    __name__
    __module__
    __doc__

These provide metadata about the class.
"""


class Person:
    """Represent a person."""

    species = "Human"


print(Person.__dict__["__name__"])
print(Person.__dict__["__module__"])
print(Person.__dict__["__doc__"])


# ============================================================
# 16. __name__ IS A CLASS ATTRIBUTE
# ============================================================

"""
A class automatically receives a __name__ attribute containing
the class's name.
"""


class Person:
    """Represent a person."""


print(Person.__name__)
print(Person.__dict__["__name__"])


# ============================================================
# 17. __doc__ IS STORED IN THE CLASS NAMESPACE
# ============================================================

"""
A class docstring becomes the value of the class's __doc__
attribute.
"""


class Person:
    """Represent a person."""


print(Person.__doc__)
print(Person.__dict__["__doc__"])


# ============================================================
# 18. __module__ IDENTIFIES THE DEFINING MODULE
# ============================================================

"""
Python stores the name of the module where the class was
defined in __module__.
"""


class Person:
    """Represent a person."""


print(Person.__module__)
print(Person.__dict__["__module__"])


# ============================================================
# 19. CLASS NAMESPACE CONTAINS CLASS-LEVEL FUNCTIONS
# ============================================================

"""
Functions defined inside a class body become entries in the
class namespace.

When accessed through an instance, Python's descriptor
mechanism can turn them into bound methods.

The descriptor mechanism is covered much later.
"""


class Calculator:
    """Provide calculator behavior."""

    def add(self, first: int, second: int) -> int:
        """Return the sum of two numbers."""
        return first + second


print(Calculator.__dict__["add"])


# ============================================================
# 20. CLASS NAMESPACE IS CREATED WHEN THE CLASS IS CREATED
# ============================================================

"""
When Python executes a class definition, it creates the class
and establishes its namespace.

Names defined inside the class body become class-level names.
"""


class Example:
    """Demonstrate a class namespace."""

    value = 100

    def show(self) -> int:
        """Return the class-level value."""
        return self.value


print(Example.__dict__["value"])
print(Example.__dict__["show"])


# ============================================================
# 21. ADDING A CLASS ATTRIBUTE AFTER CLASS CREATION
# ============================================================

"""
A class can receive a new attribute after it has already been
created.
"""


class Person:
    """Represent a person."""


print(Person.__dict__)

Person.species = "Human"

print(Person.__dict__["species"])


# ============================================================
# 22. MODIFYING A CLASS ATTRIBUTE THROUGH __dict__
# ============================================================

"""
The class namespace mapping can be inspected through
__dict__, but it should not generally be treated like an
ordinary mutable dictionary.

Normal class attribute assignment should be used when
changing class attributes:

    Person.species = "Human"

rather than attempting to modify the mapping returned by
Person.__dict__ directly.
"""


class Person:
    """Represent a person."""

    species = "Human"


Person.species = "Homo sapiens"

print(Person.species)


# ============================================================
# 23. CLASS NAMESPACE AND INSTANCE NAMESPACE WORK TOGETHER
# ============================================================

"""
A useful model is:

    Class namespace
        |
        | provides class-level attributes and methods
        |
        v
    Instance
        |
        +-- Instance namespace
        |       |
        |       +-- instance-specific attributes
        |
        +-- Attribute lookup can reach the class


Example:

    Person.species
        -> class namespace

    person.name
        -> instance namespace

    person.species
        -> instance lookup, then class namespace
"""


class Person:
    """Represent a person."""

    species = "Human"

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print("Instance:", person.__dict__)
print("Class species:", Person.__dict__["species"])

print(person.name)
print(person.species)


# ============================================================
# 24. CLASS NAMESPACE IS SHARED BY INSTANCES
# ============================================================

"""
All instances of the same class can access the same class
namespace.

Therefore, class-level data can be shared.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"

    def __init__(self, name: str) -> None:
        self.name = name


first = Employee("Shreyas")
second = Employee("Rahul")

print(first.company)
print(second.company)

print(first.__dict__)
print(second.__dict__)

print(Employee.__dict__["company"])


# ============================================================
# 25. CHANGING CLASS STATE
# ============================================================

"""
Changing a class attribute affects instances that obtain the
attribute from the class.

An instance that has its own attribute with the same name is
not affected by the class-level change.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"


first = Employee()
second = Employee()

first.company = "XYZ"

Employee.company = "DEF"

print(first.company)
print(second.company)
print(Employee.company)


# ============================================================
# 26. CLASS NAMESPACE IS NOT INSTANCE STATE
# ============================================================

"""
The class namespace and instance namespace represent
different levels of state.

    Class namespace:
        state associated with the class.

    Instance namespace:
        state associated with one object.

They should not be treated as the same storage location.
"""


class Account:
    """Represent an account."""

    account_type = "Savings"

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance


account = Account("Shreyas", 5000.0)

print("Class namespace:")
print(Account.__dict__)

print("\nInstance namespace:")
print(account.__dict__)


# ============================================================
# 27. CONCEPTUAL MODEL
# ============================================================

"""
The complete model for this section is now:

    Class
       |
       +-- Class Namespace
       |       |
       |       +-- Class Attributes
       |       +-- Methods
       |       +-- Special Attributes
       |
       | creates
       v
    Instance
       |
       +-- Instance Namespace
               |
               +-- Instance Attributes


Attribute access:

    instance.attribute

can involve:

    1. Instance namespace
    2. Class namespace
    3. Further lookup through inheritance

The complete lookup mechanism will be covered later.
"""


# ============================================================
# 28. OBJECT-ORIENTED MODEL SO FAR
# ============================================================

"""
We can now connect all seven files in this section:

    01_objects_and_identity.py
        ->
        Objects have identity, type, and value.

    02_object_state_and_behavior.py
        ->
        Objects have state and behavior.

    03_attributes_and_methods.py
        ->
        Attributes represent data/state.
        Methods represent behavior.

    04_instance_attributes.py
        ->
        Instances can have their own attributes/state.

    05_class_attributes.py
        ->
        Classes can have shared class-level attributes.

    06_object_namespace.py
        ->
        Instances can have their own namespaces.

    07_class_namespace.py
        ->
        Classes have their own namespaces containing
        class attributes and methods.
"""


# ============================================================
# 29. FINAL COMPARISON
# ============================================================

"""
Instance namespace:

    person.__dict__

Example:

    {
        "name": "Shreyas",
        "age": 29
    }

Class namespace:

    Person.__dict__

Contains things such as:

    species
    __init__
    greet
    __name__
    __doc__
    ...

The key distinction:

    Instance namespace
        -> belongs to one object.

    Class namespace
        -> belongs to the class.
"""


class Person:
    """Represent a person."""

    species = "Human"

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        """Return a greeting."""
        return f"Hello, {self.name}!"


person = Person("Shreyas", 29)

print("INSTANCE NAMESPACE")
print(person.__dict__)

print("\nCLASS NAMESPACE")
print(Person.__dict__)

print("\nATTRIBUTE ACCESS")
print(person.name)
print(person.species)
print(person.greet())


# ============================================================
# 30. KEY TAKEAWAYS
# ============================================================

"""
Key concepts:

1. A class has its own namespace.

2. A class namespace can be inspected through Class.__dict__.

3. Class attributes are stored in the class namespace.

4. Methods are stored in the class namespace.

5. Python also places special attributes in the class
   namespace.

6. Instance attributes are stored in the instance namespace.

7. Instance and class namespaces are separate.

8. A class attribute does not normally appear in an instance's
   __dict__.

9. An instance can access class attributes through attribute
   lookup.

10. An instance attribute can shadow a class attribute.

11. Modifying a class attribute can affect instances that
    obtain that attribute from the class.

12. Methods are defined in the class namespace but can be
    accessed through instances.

13. Class namespace represents class-level definitions.

14. Instance namespace represents instance-specific state.

15. Attribute lookup can move from the instance to the class.

16. Inheritance introduces additional namespaces into the
    lookup process.

This completes the foundational object model section.

The next OOP section can now move into:

    Classes and Objects

where we formally study class definition, object creation,
constructors, instance methods, class methods, static methods,
and related mechanics.
"""