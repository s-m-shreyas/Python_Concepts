# type: ignore

"""
05_initialization_with_parameters.py

Demonstrates initializing instance attributes using values
provided during object creation.

Key idea:

    object creation
        ↓
    arguments passed to class
        ↓
    __init__(self, ...)
        ↓
    parameters receive those values
        ↓
    values assigned to instance attributes
        ↓
    initialized object

This file focuses on:

    - Parameters in __init__
    - Passing arguments during object creation
    - Assigning parameters to self
    - Instance-specific initialization
    - Multiple parameters
    - Type annotations
    - Different objects receiving different values
    - Combining parameters with default values
"""


# ============================================================
# 1. BASIC PARAMETERIZED INITIALIZATION
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Alice")

print(person.name)


# ============================================================
# 2. PARAMETER VALUE BECOMES INSTANCE STATE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Alice")

print(person.__dict__)

"""
The value:

    "Alice"

is passed to __init__ through the parameter:

    name

and then stored as:

    self.name
"""


# ============================================================
# 3. PARAMETER AND INSTANCE ATTRIBUTE ARE DIFFERENT
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Alice")

"""
Here:

    name
        → local parameter inside __init__

    self.name
        → attribute belonging to the current instance

The assignment:

    self.name = name

copies the value received by the parameter into the
instance's state.
"""

print(person.name)


# ============================================================
# 4. MULTIPLE PARAMETERS
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person("Alice", 30)

print(person.name)
print(person.age)


# ============================================================
# 5. DIFFERENT OBJECTS CAN RECEIVE DIFFERENT VALUES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person_1 = Person("Alice", 30)
person_2 = Person("Bob", 25)

print(person_1.__dict__)
print(person_2.__dict__)

"""
The same __init__ method is used for both objects,
but each invocation receives different arguments.
"""


# ============================================================
# 6. EACH __init__ CALL HAS ITS OWN PARAMETERS
# ============================================================

class Employee:
    """Represent an employee."""

    def __init__(self, name: str, department: str) -> None:
        self.name = name
        self.department = department


employee_1 = Employee("Alice", "Engineering")
employee_2 = Employee("Bob", "Finance")

print(employee_1.__dict__)
print(employee_2.__dict__)


# ============================================================
# 7. PARAMETER NAMES DO NOT HAVE TO MATCH ATTRIBUTE NAMES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, person_name: str) -> None:
        self.name = person_name


person = Person("Alice")

print(person.name)

"""
Parameter:

    person_name

Instance attribute:

    self.name

They have different names but refer to the same value.
"""


# ============================================================
# 8. PARAMETERIZED INITIALIZATION WITH MULTIPLE ATTRIBUTES
# ============================================================

class Product:
    """Represent a product."""

    def __init__(
        self,
        name: str,
        price: float,
        available: bool,
    ) -> None:
        self.name = name
        self.price = price
        self.available = available


product = Product(
    "Laptop",
    75000.0,
    True,
)

print(product.__dict__)


# ============================================================
# 9. POSITIONAL ARGUMENTS DURING INITIALIZATION
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person("Alice", 30)

print(person.__dict__)

"""
The values are matched according to their position:

    "Alice" → name
    30      → age
"""


# ============================================================
# 10. KEYWORD ARGUMENTS DURING INITIALIZATION
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person(
    name="Alice",
    age=30,
)

print(person.__dict__)

"""
Keyword arguments explicitly identify which parameter
receives each value.
"""


# ============================================================
# 11. MIXING POSITIONAL AND KEYWORD ARGUMENTS
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person("Alice", age=30)

print(person.__dict__)

"""
A positional argument can be followed by a keyword
argument, as long as Python's argument-ordering rules
are respected.
"""


# ============================================================
# 12. PARAMETERIZED INITIALIZATION WITH DEFAULT PARAMETERS
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int = 0) -> None:
        self.name = name
        self.age = age


person_1 = Person("Alice", 30)
person_2 = Person("Bob")

print(person_1.__dict__)
print(person_2.__dict__)

"""
For person_2:

    age

is not supplied, so the parameter's default value is used.
"""


# ============================================================
# 13. DEFAULT VALUE IS ASSIGNED THROUGH SELF
# ============================================================

class Account:
    """Represent a bank account."""

    def __init__(
        self,
        owner: str,
        balance: float = 0.0,
    ) -> None:
        self.owner = owner
        self.balance = balance


account_1 = Account("Alice", 5000.0)
account_2 = Account("Bob")

print(account_1.__dict__)
print(account_2.__dict__)


# ============================================================
# 14. PARAMETERIZED INITIALIZATION CREATES COMPLETE STATE
# ============================================================

class Employee:
    """Represent an employee."""

    def __init__(
        self,
        name: str,
        department: str,
        experience: int,
    ) -> None:
        self.name = name
        self.department = department
        self.experience = experience


employee = Employee(
    "Alice",
    "Data Engineering",
    3,
)

print(employee.__dict__)


# ============================================================
# 15. PARAMETERS CAN BE VALIDATED BEFORE INITIALIZATION
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        if age < 0:
            raise ValueError("Age cannot be negative.")

        self.name = name
        self.age = age


person = Person("Alice", 30)

print(person.__dict__)


# ============================================================
# 16. VALIDATION HAPPENS BEFORE STATE ASSIGNMENT
# ============================================================

class Product:
    """Represent a product."""

    def __init__(self, name: str, price: float) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.name = name
        self.price = price


product = Product("Laptop", 75000.0)

print(product.__dict__)

"""
The object is initialized only after the input values pass
validation.
"""


# ============================================================
# 17. PARAMETERIZED INITIALIZATION WITH CALCULATED STATE
# ============================================================

class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
        self.area = width * height


rectangle = Rectangle(10.0, 5.0)

print(rectangle.width)
print(rectangle.height)
print(rectangle.area)

"""
Not every instance attribute needs to directly correspond
to a parameter.

area is derived from:

    width
    height
"""


# ============================================================
# 18. PARAMETERIZED INITIALIZATION WITH NORMALIZATION
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name.strip()


person = Person("  Alice  ")

print(person.name)

"""
The supplied parameter can be transformed before being
stored in the instance.
"""


# ============================================================
# 19. PARAMETERIZED INITIALIZATION WITH MULTIPLE VALUES
# ============================================================

class Student:
    """Represent a student."""

    def __init__(
        self,
        name: str,
        subjects: tuple[str, ...],
    ) -> None:
        self.name = name
        self.subjects = subjects


student = Student(
    "Alice",
    ("Python", "SQL", "Algorithms"),
)

print(student.__dict__)


# ============================================================
# 20. EACH OBJECT GETS ITS OWN INITIALIZED STATE
# ============================================================

class Counter:
    """Represent a counter with an initial value."""

    def __init__(self, value: int) -> None:
        self.value = value


counter_1 = Counter(0)
counter_2 = Counter(100)

print(counter_1.value)
print(counter_2.value)


# ============================================================
# 21. PARAMETERS CAN REPRESENT REQUIRED STATE
# ============================================================

class DatabaseConnection:
    """Represent a database connection configuration."""

    def __init__(
        self,
        host: str,
        port: int,
        database: str,
    ) -> None:
        self.host = host
        self.port = port
        self.database = database


connection = DatabaseConnection(
    "localhost",
    5432,
    "analytics",
)

print(connection.__dict__)

"""
The object cannot be created without providing the required
initialization values.
"""


# ============================================================
# 22. PARAMETERIZED INITIALIZATION VS DEFAULT INITIALIZATION
# ============================================================

class Server:
    """Represent a server."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 8000,
    ) -> None:
        self.host = host
        self.port = port


server_1 = Server()

server_2 = Server(
    host="example.com",
    port=443,
)

print(server_1.__dict__)
print(server_2.__dict__)

"""
The same class supports:

    Server()

and:

    Server("example.com", 443)

because the parameters have default values.
"""


# ============================================================
# 23. INITIALIZATION WITH KEYWORD-ONLY PARAMETERS
# ============================================================

class User:
    """Represent a user."""

    def __init__(
        self,
        name: str,
        *,
        active: bool = True,
    ) -> None:
        self.name = name
        self.active = active


user = User(
    "Alice",
    active=False,
)

print(user.__dict__)

"""
The * means that active must be supplied as a keyword
argument when explicitly provided.
"""


# ============================================================
# 24. INITIALIZATION WITH POSITIONAL-ONLY PARAMETERS
# ============================================================

class Point:
    """Represent a point."""

    def __init__(
        self,
        x: float,
        y: float,
        /,
    ) -> None:
        self.x = x
        self.y = y


point = Point(10.0, 20.0)

print(point.__dict__)

"""
The / means that x and y are positional-only parameters.

Therefore this would not be valid:

    Point(x=10.0, y=20.0)
"""


# ============================================================
# 25. PARAMETERIZED INITIALIZATION AND INSTANCE IDENTITY
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person_1 = Person("Alice")
person_2 = Person("Alice")

print(person_1.name)
print(person_2.name)

print(person_1 is person_2)

"""
Both objects contain the same initial value, but they are
still two separate instances.
"""


# ============================================================
# 26. PARAMETERS ARE LOCAL TO __init__
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Alice")

print(person.name)

"""
The parameter:

    name

exists during the execution of __init__.

After __init__ finishes, the parameter itself does not
become an attribute.

The value survives because it was assigned to:

    self.name
"""


# ============================================================
# 27. INSTANCE STATE IS WHAT SURVIVES INITIALIZATION
# ============================================================

class Employee:
    """Represent an employee."""

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary


employee = Employee("Alice", 75000.0)

print(employee.__dict__)

"""
After __init__ completes:

    name
    salary

remain as part of the object's instance state.

The local parameters:

    name
    salary

do not exist as separate local variables anymore.
"""


# ============================================================
# 28. KEY TAKEAWAY
# ============================================================

"""
Parameterized initialization allows an object to receive
its initial state from values supplied during creation.

Basic pattern:

    class Person:

        def __init__(self, name, age):
            self.name = name
            self.age = age


Then:

    person = Person("Alice", 30)


The flow is:

    Person("Alice", 30)
            ↓
        __init__()
            ↓
    name = "Alice"
    age = 30
            ↓
    self.name = name
    self.age = age
            ↓
    initialized instance


Important distinction:

    parameter
        ↓
    temporary value available during __init__

    self.attribute
        ↓
    persistent state belonging to the instance


Parameterized initialization is therefore the mechanism
that allows different objects of the same class to begin
with different initial states.
"""