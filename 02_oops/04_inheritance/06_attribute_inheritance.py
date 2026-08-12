# type: ignore

"""
06_attribute_inheritance.py

Demonstrates attribute inheritance in Python.

Attribute inheritance means a child class can access
attributes defined by its parent class.

Attributes may be:

    - Class attributes
    - Instance attributes

This file focuses specifically on attribute inheritance,
attribute lookup, and attribute overriding.
"""


# ============================================================
# 1. BASIC CLASS ATTRIBUTE INHERITANCE
# ============================================================

class Animal:
    """Represent an animal."""

    kingdom = "Animalia"


class Dog(Animal):
    """Represent a dog."""

    pass


dog = Dog()

print(dog.kingdom)
print(Dog.kingdom)
print(Animal.kingdom)

"""
Dog inherits kingdom from Animal.

The attribute exists only in Animal.__dict__.

Python finds it through inheritance.
"""


# ============================================================
# 2. CLASS ATTRIBUTE IS NOT COPIED
# ============================================================

class Parent:
    """Parent class."""

    value = 100


class Child(Parent):
    """Child class."""

    pass


print("value" in Parent.__dict__)
print("value" in Child.__dict__)

"""
Result:

    True
    False

The attribute is not copied into Child.

Python finds it through inheritance.
"""


# ============================================================
# 3. CHILD CAN ACCESS PARENT CLASS ATTRIBUTES
# ============================================================

class Vehicle:
    """Represent a vehicle."""

    category = "Transport"


class Car(Vehicle):
    """Represent a car."""

    pass


print(Car.category)

"""
Car inherits category from Vehicle.
"""


# ============================================================
# 4. CHILD CAN DEFINE ITS OWN CLASS ATTRIBUTES
# ============================================================

class Animal:
    """Represent an animal."""

    kingdom = "Animalia"


class Dog(Animal):
    """Represent a dog."""

    species = "Canis familiaris"


print(Dog.kingdom)
print(Dog.species)

"""
Dog contains:

    inherited attribute:
        kingdom

    own attribute:
        species
"""


# ============================================================
# 5. CHILD CAN OVERRIDE A CLASS ATTRIBUTE
# ============================================================

class Animal:
    """Represent an animal."""

    category = "Animal"


class Dog(Animal):
    """Represent a dog."""

    category = "Dog"


print(Animal.category)
print(Dog.category)

"""
Dog defines category itself.

Python finds Dog.category first.
"""


# ============================================================
# 6. ATTRIBUTE LOOKUP ORDER
# ============================================================

class Parent:
    """Parent class."""

    value = 10


class Child(Parent):
    """Child class."""

    pass


child = Child()

print(child.value)

"""
Lookup order:

    child
       ↓
    Child
       ↓
    Parent
       ↓
    object
"""


# ============================================================
# 7. INSTANCE ATTRIBUTE SHADOWS CLASS ATTRIBUTE
# ============================================================

class Person:
    """Represent a person."""

    role = "Person"


person = Person()

print(person.role)

person.role = "Developer"

print(person.role)
print(Person.role)

"""
Instance attributes take precedence over class attributes.
"""


# ============================================================
# 8. INSTANCE ATTRIBUTE LOOKUP
# ============================================================

class Employee:
    """Represent an employee."""

    company = "TechCorp"

    def __init__(self, name: str) -> None:
        self.name = name


employee = Employee("Alice")

print(employee.name)
print(employee.company)

"""
Lookup for:

    name

finds an instance attribute.

Lookup for:

    company

finds a class attribute.
"""


# ============================================================
# 9. INSTANCE ATTRIBUTES FROM A PARENT CLASS
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


class Student(Person):
    """Represent a student."""

    pass


student = Student("Alice")

print(student.name)

"""
name was created by Person.__init__().

Student objects still receive it.
"""


# ============================================================
# 10. MULTIPLE INSTANCE ATTRIBUTES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


class Employee(Person):
    """Represent an employee."""

    def __init__(self, name: str, employee_id: int) -> None:
        self.name = name
        self.employee_id = employee_id


employee = Employee("Alice", 101)

print(employee.name)
print(employee.employee_id)

"""
The child object contains both attributes.
"""


# ============================================================
# 11. ATTRIBUTE INHERITANCE IN MULTILEVEL INHERITANCE
# ============================================================

class Animal:
    """Represent an animal."""

    kingdom = "Animalia"


class Mammal(Animal):
    """Represent a mammal."""

    category = "Mammal"


class Dog(Mammal):
    """Represent a dog."""

    species = "Dog"


dog = Dog()

print(dog.kingdom)
print(dog.category)
print(dog.species)

"""
Dog inherits attributes through multiple levels.
"""


# ============================================================
# 12. ATTRIBUTE INHERITANCE IN HIERARCHICAL INHERITANCE
# ============================================================

class Vehicle:
    """Represent a vehicle."""

    category = "Transport"


class Car(Vehicle):
    """Represent a car."""

    pass


class Bike(Vehicle):
    """Represent a bike."""

    pass


print(Car.category)
print(Bike.category)

"""
Both children inherit category.
"""


# ============================================================
# 13. ATTRIBUTE INHERITANCE IN MULTIPLE INHERITANCE
# ============================================================

class A:
    """First parent."""

    first = "A"


class B:
    """Second parent."""

    second = "B"


class C(A, B):
    """Child."""

    pass


c = C()

print(c.first)
print(c.second)

"""
C inherits attributes from both parents.
"""


# ============================================================
# 14. ATTRIBUTE NAME CONFLICT
# ============================================================

class ParentA:
    """First parent."""

    value = "A"


class ParentB:
    """Second parent."""

    value = "B"


class Child(ParentA, ParentB):
    """Child."""

    pass


print(Child.value)

"""
Both parents define value.

MRO determines which value is selected.

ParentA appears first.
"""


# ============================================================
# 15. REVERSING PARENT ORDER
# ============================================================

class ParentA:
    """First parent."""

    value = "A"


class ParentB:
    """Second parent."""

    value = "B"


class Child(ParentB, ParentA):
    """Child."""

    pass


print(Child.value)

"""
ParentB now appears first in the MRO.
"""


# ============================================================
# 16. ATTRIBUTE LOOKUP THROUGH __mro__
# ============================================================

class A:
    """Parent A."""

    pass


class B(A):
    """Parent B."""

    pass


class C(B):
    """Parent C."""

    pass


print(C.__mro__)

"""
MRO controls attribute lookup as well as method lookup.
"""


# ============================================================
# 17. CHILD OVERRIDES PARENT ATTRIBUTE
# ============================================================

class Employee:
    """Represent an employee."""

    company = "TechCorp"


class Developer(Employee):
    """Represent a developer."""

    company = "DevCorp"


print(Employee.company)
print(Developer.company)

"""
Developer defines its own company attribute.
"""


# ============================================================
# 18. INSTANCE ATTRIBUTE DOES NOT MODIFY CLASS ATTRIBUTE
# ============================================================

class Person:
    """Represent a person."""

    role = "Person"


person = Person()

person.role = "Developer"

print(person.role)
print(Person.role)

"""
The assignment creates an instance attribute.

The class attribute remains unchanged.
"""


# ============================================================
# 19. ATTRIBUTE LOOKUP CAN BE INSPECTED
# ============================================================

class Parent:
    """Parent class."""

    value = 10


class Child(Parent):
    """Child class."""

    pass


print(Child.__dict__.keys())
print(Parent.__dict__.keys())

"""
value exists only in Parent.__dict__.

Child accesses it through inheritance.
"""


# ============================================================
# 20. KEY TAKEAWAY
# ============================================================

"""
Attribute inheritance allows child classes to access
attributes defined by parent classes.

Example:

    class Animal:
        kingdom = "Animalia"


    class Dog(Animal):
        pass


    print(Dog.kingdom)

Lookup order:

    instance
       ↓
    child class
       ↓
    parent class
       ↓
    object

Important points:

    - Attributes are inherited.
    - Attributes are not copied.
    - Child classes can override attributes.
    - Instance attributes take precedence over
      class attributes.
    - MRO controls attribute lookup.
"""