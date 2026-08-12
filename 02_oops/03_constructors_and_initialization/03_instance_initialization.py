# type: ignore

"""
03_instance_initialization.py

Demonstrates how instance attributes are initialized for
individual objects.

Key idea:

    Instance initialization
        ↓
    assigning data to self
        ↓
    each object gets its own instance state

This file focuses on:

    - Instance attributes
    - Initializing attributes through self
    - Each object having independent state
    - Instance state stored separately for each object
    - Inspecting instance state
    - Modifying instance state
    - Avoiding accidental class-level state

Detailed constructor mechanics are covered separately.
"""


# ============================================================
# 1. INSTANCE ATTRIBUTES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"
        self.age = 30


person = Person()

print(person.name)
print(person.age)


# ============================================================
# 2. SELF REFERS TO THE CURRENT INSTANCE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

print(person.name)

"""
Inside __init__:

    self.name = "Alice"

means:

    "Store the value 'Alice' on this particular object."

self refers to the instance currently being initialized.
"""


# ============================================================
# 3. EACH INSTANCE HAS ITS OWN STATE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Unknown"
        self.age = 0


person_1 = Person()
person_2 = Person()

person_1.name = "Alice"
person_1.age = 30

person_2.name = "Bob"
person_2.age = 25

print(person_1.name)
print(person_1.age)

print(person_2.name)
print(person_2.age)


# ============================================================
# 4. INSTANCE ATTRIBUTES ARE INDEPENDENT
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Unknown"


person_1 = Person()
person_2 = Person()

person_1.name = "Alice"

print(person_1.name)
print(person_2.name)

"""
Changing:

    person_1.name

does not change:

    person_2.name

because each instance has its own instance state.
"""


# ============================================================
# 5. INSTANCE __dict__
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"
        self.age = 30


person = Person()

print(person.__dict__)

"""
Output:

    {'name': 'Alice', 'age': 30}

The instance dictionary contains attributes stored
directly on that object.
"""


# ============================================================
# 6. DIFFERENT INSTANCES HAVE DIFFERENT __dict__ OBJECTS
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Unknown"


person_1 = Person()
person_2 = Person()

print(person_1.__dict__)
print(person_2.__dict__)

print(person_1.__dict__ is person_2.__dict__)

"""
Each normal instance has its own __dict__.

Therefore:

    person_1.__dict__ is person_2.__dict__

is False.
"""


# ============================================================
# 7. ADDING AN INSTANCE ATTRIBUTE AFTER INITIALIZATION
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

print(person.__dict__)

person.age = 30

print(person.__dict__)

"""
Instance attributes can normally be added after the object
has been initialized.
"""


# ============================================================
# 8. INSTANCE STATE CAN BE MODIFIED
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"
        self.age = 30


person = Person()

print(person.name)
print(person.age)

person.name = "Bob"
person.age = 35

print(person.name)
print(person.age)


# ============================================================
# 9. INSTANCE ATTRIBUTE CREATION
# ============================================================

class Product:
    """Represent a product."""

    def __init__(self) -> None:
        self.name = "Laptop"
        self.price = 75000


product = Product()

"""
The following assignments create instance attributes:

    self.name
    self.price

Conceptually:

    product
       ↓
    __dict__
       ├── name  → "Laptop"
       └── price → 75000
"""

print(product.__dict__)


# ============================================================
# 10. INSTANCE ATTRIBUTES CAN HAVE DIFFERENT VALUES
# ============================================================

class Product:
    """Represent a product."""

    def __init__(self) -> None:
        self.name = "Unknown"
        self.price = 0


product_1 = Product()
product_2 = Product()

product_1.name = "Laptop"
product_1.price = 75000

product_2.name = "Phone"
product_2.price = 30000

print(product_1.__dict__)
print(product_2.__dict__)


# ============================================================
# 11. INSTANCE INITIALIZATION HAPPENS FOR EACH OBJECT
# ============================================================

class Counter:
    """Represent a counter."""

    def __init__(self) -> None:
        self.value = 0


counter_1 = Counter()
counter_2 = Counter()

counter_1.value += 1

print(counter_1.value)
print(counter_2.value)

"""
Both objects started with:

    value = 0

But they maintain independent instance state.
"""


# ============================================================
# 12. INSTANCE ATTRIBUTE VS CLASS ATTRIBUTE
# ============================================================

class Person:
    """Represent a person."""

    species = "Human"

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

print(person.name)
print(person.species)

"""
name:

    Instance attribute
    ↓
    stored on person

species:

    Class attribute
    ↓
    defined on Person
"""


# ============================================================
# 13. INSTANCE ATTRIBUTE SHADOWS CLASS ATTRIBUTE
# ============================================================

class Person:
    """Represent a person."""

    species = "Human"

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

print(person.species)

person.species = "Unknown"

print(person.species)
print(Person.species)

"""
The assignment:

    person.species = "Unknown"

creates an instance attribute.

It does not modify:

    Person.species

Therefore:

    person.species → "Unknown"
    Person.species  → "Human"
"""


# ============================================================
# 14. INSTANCE STATE IS CREATED USING SELF
# ============================================================

class Employee:
    """Represent an employee."""

    def __init__(self) -> None:
        self.name = "Alice"
        self.department = "Data Engineering"
        self.experience = 3


employee = Employee()

print(employee.name)
print(employee.department)
print(employee.experience)


# ============================================================
# 15. ATTRIBUTE NAMES ARE CREATED WHEN ASSIGNMENT OCCURS
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

print(person.__dict__)

"""
Before:

    self.name = "Alice"

the instance does not have a name attribute.

The assignment creates it.
"""

# ============================================================
# 16. INITIALIZATION CAN CREATE DIFFERENT ATTRIBUTES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, include_age: bool) -> None:
        self.name = "Alice"

        if include_age:
            self.age = 30


person_with_age = Person(True)
person_without_age = Person(False)

print(person_with_age.__dict__)
print(person_without_age.__dict__)


# ============================================================
# 17. MISSING INSTANCE ATTRIBUTES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

print(hasattr(person, "name"))
print(hasattr(person, "age"))

"""
name exists because it was initialized.

age does not exist because it was never assigned.
"""


# ============================================================
# 18. DELETING AN INSTANCE ATTRIBUTE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"
        self.age = 30


person = Person()

print(person.__dict__)

del person.age

print(person.__dict__)

"""
Deleting an instance attribute removes it from the
instance's state.

The object still exists, but age no longer exists on
that particular instance.
"""


# ============================================================
# 19. INSTANCE INITIALIZATION WITH A HELPER METHOD
# ============================================================

class Employee:
    """Represent an employee."""

    def __init__(self) -> None:
        self._initialize_details()

    def _initialize_details(self) -> None:
        self.name = "Alice"
        self.department = "Engineering"


employee = Employee()

print(employee.__dict__)

"""
The initialization logic can be delegated to another
instance method.

The attributes still belong to the individual instance
because they are assigned through self.
"""


# ============================================================
# 20. EACH OBJECT RECEIVES ITS OWN INITIALIZED STATE
# ============================================================

class Account:
    """Represent a bank account."""

    def __init__(self) -> None:
        self.balance = 0.0
        self.active = True


account_1 = Account()
account_2 = Account()

account_1.balance = 5000.0

print(account_1.__dict__)
print(account_2.__dict__)

"""
Changing account_1 does not change account_2.

Each object has its own instance state.
"""


# ============================================================
# 21. IMPORTANT: MUTABLE INSTANCE ATTRIBUTES
# ============================================================

class Student:
    """Represent a student."""

    def __init__(self) -> None:
        self.subjects = []


student_1 = Student()
student_2 = Student()

student_1.subjects.append("Python")

print(student_1.subjects)
print(student_2.subjects)

"""
Because subjects is created inside __init__:

    self.subjects = []

each Student receives a separate list.

This is different from creating one shared mutable
object at the class level.
"""


# ============================================================
# 22. WHY INSTANCE INITIALIZATION MATTERS
# ============================================================

"""
Good instance initialization ensures that an object starts
in a predictable state.

For example:

    class Employee:

        def __init__(self):
            self.name = "Unknown"
            self.department = "Unknown"
            self.experience = 0


Every Employee object starts with the same structure,
while still maintaining independent values.

Conceptually:

    Employee()
        ↓
    object created
        ↓
    __init__()
        ↓
    self.name
    self.department
    self.experience
        ↓
    initialized instance
"""


# ============================================================
# 23. KEY TAKEAWAY
# ============================================================

"""
Instance initialization means establishing the state of
one particular object.

The central mechanism is:

    self.attribute = value

For example:

    class Person:

        def __init__(self):
            self.name = "Alice"
            self.age = 30


Each call:

    Person()

creates a new object and initializes its own state.

Therefore:

    person_1.name
    person_2.name

are independent instance attributes.

Remember:

    self
      ↓
    current object
      ↓
    self.attribute
      ↓
    state belonging to that object
"""