# type: ignore
"""
02_constructor_vs_initializer.py

Demonstrates the difference between object construction
and object initialization in Python.

Python's object creation process can be understood as:

    __new__()
        ↓
    creates the object
        ↓
    __init__()
        ↓
    initializes the object

Important terminology:

    __new__()
        → responsible for creating the instance

    __init__()
        → responsible for initializing the instance

In everyday Python discussion, __init__ is often called
the "constructor", but technically this is not precise.

This file focuses on understanding that distinction.
"""


# ============================================================
# 1. __new__ AND __init__ ARE DIFFERENT SPECIAL METHODS
# ============================================================

class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        print("__new__() called")
        return super().__new__(cls)

    def __init__(self) -> None:
        print("__init__() called")


person = Person()


# ============================================================
# 2. THE ORDER IS __new__ THEN __init__
# ============================================================

class Example:
    """Demonstrate the object creation sequence."""

    def __new__(cls) -> "Example":
        print("Step 1: __new__()")
        return super().__new__(cls)

    def __init__(self) -> None:
        print("Step 2: __init__()")


example = Example()


# ============================================================
# 3. __new__ CREATES THE INSTANCE
# ============================================================

class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        instance = super().__new__(cls)

        print(f"Created object: {instance}")

        return instance


person = Person()


# ============================================================
# 4. __init__ RECEIVES THE CREATED INSTANCE
# ============================================================

class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        return super().__new__(cls)

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

print(person.name)


# ============================================================
# 5. CONSTRUCTION VS INITIALIZATION
# ============================================================

"""
Think of the process in two conceptual stages:

    CONSTRUCTION
        ↓
    __new__()
        ↓
    "Give me a new object."

    INITIALIZATION
        ↓
    __init__()
        ↓
    "Configure that object."
"""

class Product:
    """Represent a product."""

    def __new__(cls) -> "Product":
        print("Constructing Product object...")
        return super().__new__(cls)

    def __init__(self) -> None:
        print("Initializing Product object...")
        self.name = "Laptop"
        self.price = 75000


product = Product()

print(product.name)
print(product.price)


# ============================================================
# 6. __new__ RECEIVES cls
# ============================================================

"""
__new__ is a class-level creation mechanism.

Its first parameter is conventionally:

    cls

because it receives the class from which the object should
be created.
"""

class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        print(f"Creating an instance of {cls.__name__}")
        return super().__new__(cls)

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()


# ============================================================
# 7. __init__ RECEIVES self
# ============================================================

"""
Once __new__ has produced the object, __init__ receives that
object as self.
"""

class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        return super().__new__(cls)

    def __init__(self) -> None:
        print(f"Initializing {self}")
        self.name = "Alice"


person = Person()


# ============================================================
# 8. __new__ MUST RETURN AN INSTANCE
# ============================================================

"""
When overriding __new__, the method is expected to return
the object that should be initialized.

The common implementation is:

    return super().__new__(cls)
"""

class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        return super().__new__(cls)

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

print(person.name)


# ============================================================
# 9. __init__ DOES NOT CREATE THE OBJECT
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

print(person)

"""
The object already exists when __init__ starts.

__init__ is configuring that existing instance.
"""


# ============================================================
# 10. __init__ MUST RETURN None
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

print(person.name)

"""
The return value of __init__ must be None.

The object itself is not returned from __init__.
"""


# ============================================================
# 11. __new__ CAN PREVENT __init__ FROM RUNNING
# ============================================================

"""
If __new__ returns an object that is not an instance of
the class being constructed, Python does not call __init__
for that class.

This demonstrates why __new__ is involved in construction
while __init__ is involved in initialization.
"""

class Example:
    """Demonstrate construction control."""

    def __new__(cls) -> object:
        print("__new__() called")
        return object()

    def __init__(self) -> None:
        print("__init__() called")


example = Example()

print(type(example))


# ============================================================
# 12. __new__ CAN RETURN AN INSTANCE OF THE CLASS
# ============================================================

class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        instance = super().__new__(cls)

        print("Person instance created.")

        return instance

    def __init__(self) -> None:
        print("Person instance initialized.")
        self.name = "Alice"


person = Person()

print(person.name)


# ============================================================
# 13. OBJECT CREATION SEQUENCE
# ============================================================

class Employee:
    """Represent an employee."""

    def __new__(cls, name: str) -> "Employee":
        print(f"Creating Employee object for {name}")
        return super().__new__(cls)

    def __init__(self, name: str) -> None:
        print(f"Initializing Employee object for {name}")
        self.name = name


employee = Employee("Alice")

print(employee.name)


# ============================================================
# 14. WHY __init__ IS OFTEN CALLED A CONSTRUCTOR
# ============================================================

"""
In everyday Python terminology, developers frequently say:

    "__init__ is the constructor."

This is understandable because __init__ is normally where
we provide the initial values for an object.

Technically, however:

    __new__()
        → creates the object

    __init__()
        → initializes the object

Therefore, "__init__ is the initializer" is more precise.
"""


# ============================================================
# 15. SIMPLE EVERYDAY MODEL
# ============================================================

"""
Imagine buying a new laptop.

Construction:

    __new__()
        ↓
    A physical laptop object is created.

Initialization:

    __init__()
        ↓
    Configure its initial settings.

In Python terms:

    __new__()
        → create the object

    __init__()
        → prepare the object for use
"""


# ============================================================
# 16. __new__ IS RARELY OVERRIDDEN
# ============================================================

"""
Most Python classes only need __init__.

Typical class:

    class Person:

        def __init__(self, name):
            self.name = name


Most application-level code does not need to override
__new__.

__new__ becomes useful for advanced object creation
requirements such as:

    - immutable types
    - object caching
    - singleton-like patterns
    - controlling instance creation
    - metaclass-related behavior
"""


# ============================================================
# 17. NORMAL CLASS DESIGN USES __init__
# ============================================================

class Employee:
    """Represent an employee."""

    def __init__(self, name: str, department: str) -> None:
        self.name = name
        self.department = department


employee = Employee(
    "Alice",
    "Data Engineering",
)

print(employee.name)
print(employee.department)


# ============================================================
# 18. CONCEPTUAL CALL SEQUENCE
# ============================================================

"""
For:

    person = Person("Alice")


The conceptual sequence is:

    Person.__new__(Person, "Alice")
                ↓
        new Person instance
                ↓
    Person.__init__(instance, "Alice")
                ↓
        initialized instance
                ↓
        assigned to person


The exact internal machinery is more sophisticated,
but this model is useful for understanding the roles
of __new__ and __init__.
"""


# ============================================================
# 19. __new__ IS A CLASS-LEVEL CREATION STEP
# ============================================================

class Account:
    """Represent an account."""

    def __new__(cls) -> "Account":
        print(f"__new__ received: {cls.__name__}")
        return super().__new__(cls)

    def __init__(self) -> None:
        print("__init__ received the instance.")
        self.balance = 0.0


account = Account()

print(account.balance)


# ============================================================
# 20. __init__ IS AN INSTANCE INITIALIZATION STEP
# ============================================================

class Account:
    """Represent an account."""

    def __init__(self) -> None:
        self.balance = 0.0
        self.active = True


account = Account()

print(account.balance)
print(account.active)


# ============================================================
# 21. IMPORTANT DIFFERENCE
# ============================================================

"""
Remember:

    __new__(cls)
        ↓
    decides/creates which object is produced


    __init__(self)
        ↓
    initializes the produced object


Parameter difference:

    __new__()
        → cls

    __init__()
        → self


Conceptual relationship:

    cls
      ↓
    class
      ↓
    __new__()
      ↓
    object
      ↓
    __init__()
      ↓
    initialized object
"""


# ============================================================
# 22. KEY TAKEAWAY
# ============================================================

"""
The most important distinction is:

    __new__()
        → object creation

    __init__()
        → object initialization


When writing normal Python classes:

    class Person:

        def __init__(self, name):
            self.name = name


you generally only need __init__.

Python handles __new__ for you.

So:

    __new__()
        = "Create the object."

    __init__()
        = "Initialize the object."


This is why calling __init__ the "constructor" is common
in casual Python terminology, but technically:

    __new__       → constructor / object creation
    __init__      → initializer / object initialization
"""

