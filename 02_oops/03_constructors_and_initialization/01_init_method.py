# type: ignore


"""
01_init_method.py

Demonstrates the __init__ method in Python.

The __init__ method is a special instance method that Python
automatically calls after a new object has been created.

It is commonly used to initialize instance attributes.

Syntax:

    class ClassName:

        def __init__(self):
            ...


The first parameter is conventionally named self.
"""


# ============================================================
# 1. BASIC __init__ METHOD
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        print("The __init__ method was called.")


person = Person()


# ============================================================
# 2. __init__ IS CALLED AUTOMATICALLY
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        print("Person object initialized.")


person = Person()

"""
We did not explicitly write:

    person.__init__()

Python automatically called __init__ when the object was
created.
"""


# ============================================================
# 3. __init__ CAN INITIALIZE INSTANCE ATTRIBUTES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

print(person.name)


# ============================================================
# 4. MULTIPLE INSTANCE ATTRIBUTES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"
        self.age = 30
        self.city = "Bengaluru"


person = Person()

print(person.name)
print(person.age)
print(person.city)


# ============================================================
# 5. EACH OBJECT GETS ITS OWN INITIALIZED STATE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"


person_one = Person()
person_two = Person()

person_one.name = "Bob"

print(person_one.name)
print(person_two.name)


# ============================================================
# 6. __init__ RUNS FOR EACH NEW INSTANCE
# ============================================================

class Counter:
    """Represent a simple counter."""

    def __init__(self) -> None:
        print("Initializing a Counter object.")


counter_one = Counter()
counter_two = Counter()
counter_three = Counter()


# ============================================================
# 7. __init__ CAN PERFORM INITIAL SETUP
# ============================================================

class BankAccount:
    """Represent a bank account."""

    def __init__(self) -> None:
        self.balance = 0.0


account = BankAccount()

print(account.balance)


# ============================================================
# 8. __init__ WITH INSTANCE METHODS
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"

    def greet(self) -> None:
        """Greet the person."""
        print(f"Hello, {self.name}.")


person = Person()

person.greet()


# ============================================================
# 9. __init__ CAN INITIALIZE COLLECTIONS
# ============================================================

class ShoppingCart:
    """Represent a shopping cart."""

    def __init__(self) -> None:
        self.items: list[str] = []


cart = ShoppingCart()

cart.items.append("Laptop")
cart.items.append("Mouse")

print(cart.items)


# ============================================================
# 10. __init__ CAN INITIALIZE DIFFERENT DATA TYPES
# ============================================================

class Profile:
    """Represent a user profile."""

    def __init__(self) -> None:
        self.name: str = "Alice"
        self.age: int = 30
        self.active: bool = True
        self.skills: list[str] = ["Python", "SQL"]
        self.experience: dict[str, int] = {
            "Python": 3,
            "SQL": 2,
        }


profile = Profile()

print(profile.name)
print(profile.age)
print(profile.active)
print(profile.skills)
print(profile.experience)


# ============================================================
# 11. __init__ CAN INITIALIZE OBJECT STATE
# ============================================================

class Light:
    """Represent a light."""

    def __init__(self) -> None:
        self.is_on = False


light = Light()

print(light.is_on)


# ============================================================
# 12. INSTANCE STATE CAN CHANGE AFTER INITIALIZATION
# ============================================================

class Light:
    """Represent a light."""

    def __init__(self) -> None:
        self.is_on = False

    def turn_on(self) -> None:
        """Turn the light on."""
        self.is_on = True


light = Light()

print(light.is_on)

light.turn_on()

print(light.is_on)


# ============================================================
# 13. __init__ CAN CALL INSTANCE METHODS
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"
        self._display_initial_state()

    def _display_initial_state(self) -> None:
        """Display the initial state."""
        print(f"Initialized person: {self.name}")


person = Person()


# ============================================================
# 14. __init__ RETURNS None
# ============================================================

class Example:
    """Demonstrate the return requirement of __init__."""

    def __init__(self) -> None:
        self.value = 100


example = Example()

print(example.value)

"""
The __init__ method must return None.

This is why its annotation is:

    -> None
"""


# ============================================================
# 15. __init__ SHOULD NOT EXPLICITLY RETURN AN OBJECT
# ============================================================

class Product:
    """Represent a product."""

    def __init__(self) -> None:
        self.name = "Laptop"


product = Product()

print(product.name)

"""
Do not write:

    def __init__(self):
        return some_object

__init__ is responsible for initialization and must return
None.
"""


# ============================================================
# 16. __init__ CAN USE EXPRESSIONS TO INITIALIZE VALUES
# ============================================================

class Rectangle:
    """Represent a rectangle."""

    def __init__(self) -> None:
        self.length = 10
        self.width = 5
        self.area = self.length * self.width


rectangle = Rectangle()

print(rectangle.area)


# ============================================================
# 17. __init__ CAN INITIALIZE DEPENDENT ATTRIBUTES
# ============================================================

class Circle:
    """Represent a circle."""

    def __init__(self) -> None:
        self.radius = 5
        self.diameter = self.radius * 2


circle = Circle()

print(circle.radius)
print(circle.diameter)


# ============================================================
# 18. __init__ CAN INITIALIZE OBJECTS WITH A DEFAULT STATE
# ============================================================

class Employee:
    """Represent an employee."""

    def __init__(self) -> None:
        self.name = "Unknown"
        self.department = "Unassigned"
        self.active = False


employee = Employee()

print(employee.name)
print(employee.department)
print(employee.active)


# ============================================================
# 19. __init__ AND INSTANCE IDENTITY
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"

    def display(self) -> None:
        """Display information about this instance."""
        print(f"Object: {self}")
        print(f"Name: {self.name}")


person = Person()

person.display()


# ============================================================
# 20. __init__ IS AN INSTANCE METHOD
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Alice"


person = Person()

"""
Because __init__ is an instance method, it receives the
newly created object through self.

Conceptually:

    Person()

causes Python to eventually invoke something equivalent to:

    person.__init__()

where self refers to person.
"""


# ============================================================
# 21. __init__ CAN INITIALIZE DIFFERENT OBJECT STATES
# ============================================================

class Account:
    """Represent an account with default state."""

    def __init__(self) -> None:
        self.balance = 0.0
        self.is_active = False


account_one = Account()
account_two = Account()

account_one.balance = 1000.0
account_one.is_active = True

print(account_one.balance)
print(account_one.is_active)

print(account_two.balance)
print(account_two.is_active)


# ============================================================
# 22. COMMON PURPOSES OF __init__
# ============================================================

"""
The __init__ method is commonly used to:

    - initialize instance attributes
    - establish default object state
    - initialize collections
    - prepare an object for use
    - perform basic instance setup

For example:

    class Employee:

        def __init__(self):
            self.name = "Unknown"
            self.department = "Unassigned"
            self.active = True
"""


# ============================================================
# 23. KEY TAKEAWAY
# ============================================================

"""
The __init__ method:

    - is a special method
    - is automatically called during object creation
    - receives the instance as self
    - initializes the instance's state
    - commonly creates instance attributes
    - is called once for each newly created instance
    - must return None

Basic structure:

    class Person:

        def __init__(self):
            self.name = "Alice"


    person = Person()


Conceptually:

    Person()
        ↓
    object is created
        ↓
    __init__ is called
        ↓
    instance state is initialized
        ↓
    ready-to-use object


The next file will distinguish the roles of
object creation, the constructor mechanism, and
the __init__ initializer.
"""

