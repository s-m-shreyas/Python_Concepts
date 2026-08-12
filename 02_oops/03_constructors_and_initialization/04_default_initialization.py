# type: ignore
"""
04_default_initialization.py

Demonstrates default initialization of instance attributes.

Default initialization means assigning predefined values to
instance attributes when an object is created.

Key idea:

    object creation
        ↓
    __init__()
        ↓
    default values assigned
        ↓
    initialized object

This file focuses on:

    - Default values for instance attributes
    - Why default initialization is useful
    - Independent defaults for each instance
    - Default values with mutable objects
    - Explicit values overriding defaults
    - None as a default value
    - Avoiding shared mutable class attributes
"""


# ============================================================
# 1. BASIC DEFAULT INITIALIZATION
# ============================================================

class Person:
    """Represent a person with default values."""

    def __init__(self) -> None:
        self.name = "Unknown"
        self.age = 0


person = Person()

print(person.name)
print(person.age)


# ============================================================
# 2. DEFAULT INITIALIZATION CREATES INITIAL INSTANCE STATE
# ============================================================

class Employee:
    """Represent an employee."""

    def __init__(self) -> None:
        self.name = "Unknown"
        self.department = "Unassigned"
        self.experience = 0


employee = Employee()

print(employee.__dict__)


# ============================================================
# 3. EVERY INSTANCE RECEIVES ITS OWN DEFAULT VALUES
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
Both objects initially received:

    balance = 0.0
    active = True

Changing account_1 does not affect account_2.
"""


# ============================================================
# 4. DEFAULT INITIALIZATION PROVIDES A PREDICTABLE STATE
# ============================================================

class Product:
    """Represent a product."""

    def __init__(self) -> None:
        self.name = "Unknown"
        self.price = 0.0
        self.available = False


product = Product()

print(product.name)
print(product.price)
print(product.available)

"""
The object starts in a predictable state instead of having
missing attributes.
"""


# ============================================================
# 5. DEFAULT VALUE OF NONE
# ============================================================

class Employee:
    """Represent an employee whose manager may be unknown."""

    def __init__(self) -> None:
        self.name = "Unknown"
        self.manager = None


employee = Employee()

print(employee.name)
print(employee.manager)

"""
None is commonly used when a value is currently unavailable
or intentionally not assigned.
"""


# ============================================================
# 6. DEFAULT INITIALIZATION DOES NOT MEAN IMMUTABLE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Unknown"
        self.age = 0


person = Person()

person.name = "Alice"
person.age = 30

print(person.name)
print(person.age)

"""
Default initialization only defines the object's initial
state.

It does not prevent later modification.
"""


# ============================================================
# 7. DEFAULT VALUES CAN BE REPLACED AFTER CREATION
# ============================================================

class Product:
    """Represent a product."""

    def __init__(self) -> None:
        self.name = "Unknown"
        self.price = 0.0


product = Product()

print(product.__dict__)

product.name = "Laptop"
product.price = 75000.0

print(product.__dict__)


# ============================================================
# 8. DEFAULT INITIALIZATION WITH MUTABLE INSTANCE ATTRIBUTES
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
Because the list is created inside __init__:

    self.subjects = []

each Student receives a separate list.

Therefore:

    student_1.subjects is student_2.subjects

is False.
"""

print(student_1.subjects is student_2.subjects)


# ============================================================
# 9. SHARED MUTABLE CLASS ATTRIBUTE — AVOID THIS
# ============================================================

class Student:
    """Demonstrate an unwanted shared mutable attribute."""

    subjects = []

    def __init__(self) -> None:
        self.name = "Unknown"


student_1 = Student()
student_2 = Student()

student_1.subjects.append("Python")

print(student_1.subjects)
print(student_2.subjects)

"""
Both objects see the same list because subjects belongs to
the class rather than being initialized separately for each
instance.

This is usually NOT what we want for per-object state.
"""


# ============================================================
# 10. CORRECT WAY TO INITIALIZE A MUTABLE DEFAULT
# ============================================================

class Student:
    """Represent a student."""

    def __init__(self) -> None:
        self.name = "Unknown"
        self.subjects = []


student_1 = Student()
student_2 = Student()

student_1.subjects.append("Python")

print(student_1.subjects)
print(student_2.subjects)

"""
The list is created during each __init__ call.

Therefore each object receives a separate list.
"""


# ============================================================
# 11. DEFAULT INITIALIZATION WITH MULTIPLE DATA TYPES
# ============================================================

class Configuration:
    """Represent application configuration."""

    def __init__(self) -> None:
        self.debug = False
        self.timeout = 30
        self.host = "localhost"
        self.tags = []
        self.metadata = {}


configuration = Configuration()

print(configuration.__dict__)


# ============================================================
# 12. DEFAULT INITIALIZATION CAN ESTABLISH OBJECT INVARIANTS
# ============================================================

class Counter:
    """Represent a counter."""

    def __init__(self) -> None:
        self.value = 0


counter = Counter()

print(counter.value)

"""
The class guarantees that every newly created Counter
starts with:

    value = 0

This is an example of establishing an initial invariant.
"""


# ============================================================
# 13. DEFAULT INITIALIZATION WITH A BOOLEAN STATE
# ============================================================

class User:
    """Represent a user."""

    def __init__(self) -> None:
        self.name = "Guest"
        self.is_active = False


user = User()

print(user.name)
print(user.is_active)


# ============================================================
# 14. DEFAULT INITIALIZATION WITH EMPTY COLLECTIONS
# ============================================================

class ShoppingCart:
    """Represent an empty shopping cart."""

    def __init__(self) -> None:
        self.items = []
        self.quantities = {}


cart = ShoppingCart()

print(cart.items)
print(cart.quantities)


# ============================================================
# 15. EACH EMPTY COLLECTION IS CREATED SEPARATELY
# ============================================================

class ShoppingCart:
    """Represent a shopping cart."""

    def __init__(self) -> None:
        self.items = []


cart_1 = ShoppingCart()
cart_2 = ShoppingCart()

print(cart_1.items is cart_2.items)

"""
Output:

    False

Each call to ShoppingCart() executes:

    self.items = []

and therefore creates a new list.
"""


# ============================================================
# 16. DEFAULT INITIALIZATION VS CLASS ATTRIBUTES
# ============================================================

class Employee:
    """Demonstrate instance and class state."""

    company = "Example Corp"

    def __init__(self) -> None:
        self.name = "Unknown"
        self.department = "Unassigned"


employee = Employee()

print(employee.__dict__)
print(Employee.company)

"""
name and department:

    instance attributes

company:

    class attribute
"""


# ============================================================
# 17. DEFAULT INSTANCE STATE CAN BE INSPECTED
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Unknown"
        self.age = 0
        self.city = "Unknown"


person = Person()

print(person.__dict__)

"""
The instance dictionary provides a view of the initialized
instance state.
"""


# ============================================================
# 18. DEFAULT INITIALIZATION DOES NOT REQUIRE PARAMETERS
# ============================================================

class Server:
    """Represent a server with default configuration."""

    def __init__(self) -> None:
        self.host = "localhost"
        self.port = 8000
        self.running = False


server = Server()

print(server.__dict__)


# ============================================================
# 19. DEFAULT INITIALIZATION CAN BE COMBINED WITH METHODS
# ============================================================

class Counter:
    """Represent a counter."""

    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        self.value += 1


counter = Counter()

print(counter.value)

counter.increment()
counter.increment()

print(counter.value)

"""
__init__ establishes the initial state.

Methods can then operate on that state.
"""


# ============================================================
# 20. DEFAULT INITIALIZATION IS PER INSTANCE
# ============================================================

class Player:
    """Represent a player."""

    def __init__(self) -> None:
        self.score = 0
        self.level = 1


player_1 = Player()
player_2 = Player()

player_1.score = 100
player_1.level = 5

print(player_1.__dict__)
print(player_2.__dict__)

"""
Each Player begins with:

    score = 0
    level = 1

but each object maintains independent state.
"""


# ============================================================
# 21. DEFAULT INITIALIZATION WITH AN EXPLICIT STATE FLAG
# ============================================================

class Task:
    """Represent a task."""

    def __init__(self) -> None:
        self.title = "Untitled"
        self.completed = False


task = Task()

print(task.__dict__)

task.completed = True

print(task.__dict__)


# ============================================================
# 22. DEFAULT INITIALIZATION VS MISSING ATTRIBUTES
# ============================================================

class Person:
    """Compare initialized and missing attributes."""

    def __init__(self) -> None:
        self.name = "Unknown"


person = Person()

print(hasattr(person, "name"))
print(hasattr(person, "age"))

"""
name exists because it was explicitly initialized.

age does not exist because it was never created.

Default initialization can therefore be used to ensure
required attributes always exist.
"""


# ============================================================
# 23. GOOD DEFAULT INITIALIZATION
# ============================================================

class Order:
    """Represent an order."""

    def __init__(self) -> None:
        self.items = []
        self.total = 0.0
        self.is_paid = False
        self.status = "Pending"


order = Order()

print(order.__dict__)

"""
The object starts with a complete, predictable state:

    items   → empty list
    total   → 0.0
    is_paid → False
    status  → "Pending"
"""


# ============================================================
# 24. KEY TAKEAWAY
# ============================================================

"""
Default initialization means giving an instance predefined
initial values when it is created.

Example:

    class Person:

        def __init__(self):
            self.name = "Unknown"
            self.age = 0


Every new Person receives its own initial state.

Important principles:

    1. Default values are assigned during initialization.

    2. Instance defaults should normally be assigned through
       self inside __init__.

    3. Mutable defaults such as lists and dictionaries should
       be created separately for every instance.

    4. Class-level mutable attributes are shared between
       instances and can cause unintended behavior.

    5. Default initialization creates the initial state;
       it does not make the object immutable.

Conceptual model:

    Person()
       ↓
    new instance
       ↓
    __init__()
       ↓
    self.name = "Unknown"
    self.age = 0
       ↓
    initialized instance
"""