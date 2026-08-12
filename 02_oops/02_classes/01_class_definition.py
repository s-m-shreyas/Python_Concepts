# type: ignore
"""
01_class_definition.py

Introduces class definitions in Python.

This file focuses on:

    - What a class definition is
    - The class statement
    - Class naming
    - The class body
    - Defining attributes inside a class
    - Defining methods inside a class
    - Creating a class object
    - Inspecting the resulting class
    - Basic class structure

The following topics are covered separately:

    02_class_body_execution.py
    03_object_creation.py
    04_instance_methods.py
    05_self_parameter.py
    06_class_methods.py
    07_static_methods.py
    08_method_binding.py
"""


# ============================================================
# 1. WHAT IS A CLASS?
# ============================================================

"""
A class is a blueprint-like definition used to create objects.

A class can define:

    - Attributes
    - Methods
    - Other class-level definitions

For example:

    class Person:
        ...

creates a class named Person.
"""


class Person:
    """Represent a person."""

    pass


print(Person)


# ============================================================
# 2. BASIC CLASS DEFINITION SYNTAX
# ============================================================

"""
The basic syntax is:

    class ClassName:
        class_body

The class name follows the class keyword.

The class body must be indented.
"""


class Employee:
    """Represent an employee."""

    pass


print(Employee)


# ============================================================
# 3. CLASS NAMES USE PASCAL CASE
# ============================================================

"""
Python convention uses PascalCase for class names.

Examples:

    Person
    Employee
    BankAccount
    ShoppingCart

Avoid names such as:

    person
    employee
    bank_account

for classes.

Those naming styles are normally used for variables,
functions, and other non-class names.
"""


class BankAccount:
    """Represent a bank account."""

    pass


class ShoppingCart:
    """Represent a shopping cart."""

    pass


print(BankAccount)
print(ShoppingCart)


# ============================================================
# 4. THE CLASS BODY
# ============================================================

"""
Everything indented below the class statement belongs to the
class body.

The class body can contain:

    - Class attributes
    - Methods
    - Nested definitions
    - Documentation strings
    - Other executable statements
"""


class Person:
    """Represent a person."""

    species = "Human"

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


print(Person.species)
print(Person.greet)


# ============================================================
# 5. A CLASS CREATES A CLASS OBJECT
# ============================================================

"""
When Python processes a class definition, it creates a class
object.

The name:

    Person

refers to that class object.
"""


class Person:
    """Represent a person."""

    pass


print(Person)
print(type(Person))


# ============================================================
# 6. A CLASS ITSELF IS AN OBJECT
# ============================================================

"""
Classes are themselves objects in Python.

Therefore:

    Person

is an object representing the class.

Its type is:

    type
"""


class Person:
    """Represent a person."""

    pass


print(type(Person))


# ============================================================
# 7. CLASS NAME REFERENCES THE CLASS OBJECT
# ============================================================

"""
The class name is a name bound to the resulting class object.

For example:

    class Person:
        pass

creates a class object and binds the name 'Person' to it.
"""


class Person:
    """Represent a person."""

    pass


person_class = Person

print(Person)
print(person_class)

print(Person is person_class)


# ============================================================
# 8. CLASS DEFINITIONS CAN CONTAIN ATTRIBUTES
# ============================================================

"""
Attributes defined directly inside the class body become
class-level attributes.
"""


class Person:
    """Represent a person."""

    species = "Human"
    category = "Mammal"


print(Person.species)
print(Person.category)


# ============================================================
# 9. CLASS DEFINITIONS CAN CONTAIN METHODS
# ============================================================

"""
A function defined inside a class body becomes part of the
class definition.

Such a function is commonly used as a method when accessed
through an instance.
"""


class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


print(Person.greet)


# ============================================================
# 10. CLASS DEFINITIONS CAN CONTAIN BOTH ATTRIBUTES
#     AND METHODS
# ============================================================

"""
A typical class combines data definitions and behavior.
"""


class Person:
    """Represent a person."""

    species = "Human"

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


print(Person.species)
print(Person.greet)


# ============================================================
# 11. THE CLASS BODY DEFINES THE CLASS STRUCTURE
# ============================================================

"""
The class body describes what belongs to the class.

For example:

    class Employee:
        company = "ABC"

        def work(self):
            ...

defines a class containing:

    company
    work
"""


class Employee:
    """Represent an employee."""

    company = "ABC"

    def work(self) -> str:
        """Return a work description."""
        return "Employee is working."


print(Employee.company)
print(Employee.work)


# ============================================================
# 12. CLASS DEFINITIONS CAN HAVE A DOCSTRING
# ============================================================

"""
A string placed immediately inside the class body becomes the
class docstring.
"""


class Person:
    """Represent a person."""

    pass


print(Person.__doc__)


# ============================================================
# 13. CLASS DEFINITIONS CAN CONTAIN MULTIPLE ATTRIBUTES
# ============================================================

"""
Multiple class-level attributes can be defined in the class
body.
"""


class Product:
    """Represent a product."""

    category = "Electronics"
    currency = "INR"
    tax_rate = 18


print(Product.category)
print(Product.currency)
print(Product.tax_rate)


# ============================================================
# 14. CLASS DEFINITIONS CAN CONTAIN MULTIPLE METHODS
# ============================================================

"""
A class can contain multiple methods.

The methods become part of the class definition.
"""


class Calculator:
    """Provide calculator operations."""

    def add(self, first: int, second: int) -> int:
        """Return the sum."""
        return first + second

    def multiply(self, first: int, second: int) -> int:
        """Return the product."""
        return first * second


print(Calculator.add)
print(Calculator.multiply)


# ============================================================
# 15. CLASS DEFINITIONS CAN CONTAIN TYPE ANNOTATIONS
# ============================================================

"""
Class-level attributes can also have type annotations.
"""


class Product:
    """Represent a product."""

    name: str = "Laptop"
    price: float = 75000.0


print(Product.name)
print(Product.price)


# ============================================================
# 16. CLASS DEFINITION DOES NOT CREATE AN INSTANCE
# ============================================================

"""
Defining a class does not automatically create an instance of
that class.

The class object and an instance of that class are different
objects.

For example:

    class Person:
        pass

creates the class.

An instance requires a separate operation:

    person = Person()

Object creation is covered in:

    03_object_creation.py
"""


class Person:
    """Represent a person."""

    pass


print(Person)

person = Person()

print(person)


# ============================================================
# 17. CLASS AND INSTANCE ARE DIFFERENT OBJECTS
# ============================================================

"""
The class object and an instance created from it are separate
objects.

Here:

    Person

is the class.

    person

is an instance of Person.
"""


class Person:
    """Represent a person."""

    pass


person = Person()

print(Person)
print(person)

print(Person is person)


# ============================================================
# 18. isinstance() CONNECTS AN INSTANCE TO ITS CLASS
# ============================================================

"""
After an instance is created, isinstance() can be used to
check whether the object is an instance of a particular class.
"""


class Person:
    """Represent a person."""

    pass


person = Person()

print(isinstance(person, Person))


# ============================================================
# 19. type() REVEALS AN INSTANCE'S CLASS
# ============================================================

"""
For a normal instance:

    type(instance)

returns its class.
"""


class Person:
    """Represent a person."""

    pass


person = Person()

print(type(person))
print(type(person) is Person)


# ============================================================
# 20. A CLASS HAS A TYPE TOO
# ============================================================

"""
The class object itself has a type.

For ordinary Python classes:

    type(Person)

is:

    type
"""


class Person:
    """Represent a person."""

    pass


print(type(Person))
print(type(type(Person)))


# ============================================================
# 21. CLASS DEFINITION WITH AN EMPTY BODY
# ============================================================

"""
A class body cannot be completely empty.

If no definitions are needed, 'pass' can be used as a
placeholder.
"""


class EmptyClass:
    """A class with no custom definitions."""

    pass


print(EmptyClass)


# ============================================================
# 22. CLASS DEFINITION WITH ONLY A DOCSTRING
# ============================================================

"""
A docstring itself is a valid class-body statement, so pass is
not necessary when the class contains only a docstring.
"""


class DocumentationOnly:
    """This class contains only a documentation string."""


print(DocumentationOnly.__doc__)


# ============================================================
# 23. CLASS DEFINITIONS CAN BE NESTED
# ============================================================

"""
A class definition can technically appear inside another
scope, including another class.

Nested classes are an advanced topic and are not generally
required for everyday class design.

This example is included only to demonstrate that a class
definition is a Python statement.
"""


class Outer:
    """Represent an outer class."""

    class Inner:
        """Represent an inner class."""

        pass


print(Outer)
print(Outer.Inner)


# ============================================================
# 24. CLASS DEFINITIONS CAN BE ASSIGNED TO DIFFERENT NAMES
# ============================================================

"""
The class object can be assigned to another variable because
classes are objects.
"""


class Person:
    """Represent a person."""

    pass


person_type = Person

print(Person is person_type)


# ============================================================
# 25. CLASS DEFINITIONS SUPPORT ATTRIBUTE ACCESS
# ============================================================

"""
Once a class is created, its class-level attributes can be
accessed using dot notation.
"""


class Configuration:
    """Store application configuration."""

    version = "1.0"
    debug = False


print(Configuration.version)
print(Configuration.debug)


# ============================================================
# 26. CLASS DEFINITIONS AND NAMESPACES
# ============================================================

"""
The names defined directly inside a class body become part of
the class namespace.

The class namespace can be inspected using:

    ClassName.__dict__
"""


class Person:
    """Represent a person."""

    species = "Human"

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


print(Person.__dict__)


# ============================================================
# 27. CLASS DEFINITION IS DIFFERENT FROM OBJECT CREATION
# ============================================================

"""
Keep these two operations conceptually separate:

    class Person:
        ...

        ->
        defines the class.

    person = Person()

        ->
        creates an instance.

The next file focuses on what happens when Python executes
the class body.
"""


class Person:
    """Represent a person."""

    pass


person = Person()

print("Class:", Person)
print("Instance:", person)


# ============================================================
# 28. BASIC CLASS STRUCTURE
# ============================================================

"""
A basic class can therefore be visualized as:

    class ClassName:
        class_attribute = value

        def method(self):
            ...


The class definition establishes the class-level structure.

Instances created later receive their own instance state.
"""


class Employee:
    """Represent an employee."""

    company = "ABC"

    def work(self) -> str:
        """Return a work description."""
        return "Working."


print(Employee.company)
print(Employee.work)


# ============================================================
# 29. CLASS DEFINITION VS CLASS OBJECT
# ============================================================

"""
There is a useful distinction between:

    Class definition
        The source-code statement beginning with 'class'.

    Class object
        The object Python creates as a result of executing
        that class definition.

Example:

    class Person:
        pass

is the class definition.

After execution:

    Person

refers to the resulting class object.
"""


class Person:
    """Represent a person."""

    pass


person_class = Person

print(person_class)


# ============================================================
# 30. CONCEPTUAL MODEL
# ============================================================

"""
The process can be viewed conceptually as:

    class Person:
        ...
            |
            | Python executes class definition
            v
        Class object
            |
            | name 'Person' refers to it
            v
        Person


Later:

    person = Person()
            |
            | calls the class
            v
        Instance object
"""


class Person:
    """Represent a person."""

    pass


person = Person()

print("Class object:", Person)
print("Instance object:", person)


# ============================================================
# 31. KEY TAKEAWAYS
# ============================================================

"""
Key concepts:

1. A class is defined using the class statement.

2. The class body contains the definitions belonging to the
   class.

3. Class names conventionally use PascalCase.

4. Class attributes can be defined directly in the class body.

5. Methods are functions defined inside the class body.

6. A class definition creates a class object.

7. The class name refers to that class object.

8. Classes are themselves objects in Python.

9. The type of a normal user-defined class object is 'type'.

10. Defining a class does not automatically create an instance.

11. An instance is created separately, commonly by calling
    the class.

12. A class and an instance are different objects.

13. type(instance) identifies the instance's class.

14. isinstance() can check whether an object is an instance
    of a class.

15. The class namespace can be inspected through __dict__.

16. Class definition and class-body execution are related but
    distinct concepts.

The next file:

    02_class_body_execution.py

will explain what Python actually does when it executes the
body of a class definition.
"""