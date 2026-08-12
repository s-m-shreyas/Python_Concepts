# type: ignore
"""
05_self_parameter.py

Demonstrates the self parameter in Python classes.

The self parameter refers to the current instance of a class.

It allows instance methods to access:

    - instance attributes
    - other instance methods

The name "self" is a convention. Python does not require
that exact name, but using self is the standard practice.
"""


# ============================================================
# 1. BASIC USE OF self
# ============================================================

class Person:
    """Represent a person."""

    def introduce(self) -> None:
        """Print a basic introduction."""
        print("I am a person.")


person = Person()

person.introduce()


# ============================================================
# 2. self REFERS TO THE CURRENT OBJECT
# ============================================================

class Person:
    """Represent a person."""

    def show_identity(self) -> None:
        """Display the current object's identity."""
        print(self)


person = Person()

person.show_identity()


# ============================================================
# 3. self AND INSTANCE ATTRIBUTES
# ============================================================

class Person:
    """Represent a person with a name."""

    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> None:
        """Print the person's name."""
        print(f"My name is {self.name}.")


person = Person("Alice")

person.introduce()


# ============================================================
# 4. EACH OBJECT HAS ITS OWN INSTANCE DATA
# ============================================================

class Person:
    """Represent a person with a name and age."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def display(self) -> None:
        """Display the person's information."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


person_one = Person("Alice", 25)
person_two = Person("Bob", 30)

person_one.display()
person_two.display()


# ============================================================
# 5. self STORES DATA ON THE CURRENT INSTANCE
# ============================================================

class Counter:
    """Represent an independent counter."""

    def __init__(self) -> None:
        self.count = 0

    def increment(self) -> None:
        """Increase this object's counter."""
        self.count += 1

    def display(self) -> None:
        """Display this object's counter."""
        print(self.count)


counter_one = Counter()
counter_two = Counter()

counter_one.increment()
counter_one.increment()

counter_two.increment()

counter_one.display()
counter_two.display()


# ============================================================
# 6. self ALLOWS METHODS TO ACCESS OTHER METHODS
# ============================================================

class Calculator:
    """Perform simple calculations."""

    def add(self, first: int, second: int) -> int:
        """Return the sum of two numbers."""
        return first + second

    def display_sum(self, first: int, second: int) -> None:
        """Calculate and display the sum."""
        result = self.add(first, second)
        print(result)


calculator = Calculator()

calculator.display_sum(10, 20)


# ============================================================
# 7. self IS AUTOMATICALLY PROVIDED WHEN USING OBJECT.method()
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        """Print a greeting."""
        print("Hello!")


person = Person()

person.greet()

"""
Conceptually, Python performs something similar to:

    Person.greet(person)

The object before the dot becomes the self argument.
"""


# ============================================================
# 8. DIFFERENT OBJECTS PRODUCE DIFFERENT self VALUES
# ============================================================

class Person:
    """Represent a person."""

    def show_name(self, name: str) -> None:
        """Display the supplied name and current object."""
        print(f"Object: {self}")
        print(f"Name: {name}")


person_one = Person()
person_two = Person()

person_one.show_name("Alice")
person_two.show_name("Bob")


# ============================================================
# 9. self IS NOT THE SAME AS AN INSTANCE ATTRIBUTE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def display(self) -> None:
        """Display the instance attribute."""
        print(self)
        print(self.name)


person = Person("Alice")

person.display()

"""
Here:

    self
        -> refers to the current object

    self.name
        -> accesses the name attribute belonging to that object
"""


# ============================================================
# 10. self CAN ACCESS MULTIPLE INSTANCE ATTRIBUTES
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

    def display(self) -> None:
        """Display employee information."""
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Experience: {self.experience} years")


employee = Employee(
    "Alice",
    "Data Engineering",
    3,
)

employee.display()


# ============================================================
# 11. self ALLOWS INSTANCE DATA TO BE MODIFIED
# ============================================================

class BankAccount:
    """Represent a simple bank account."""

    def __init__(self, balance: float) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        self.balance += amount

    def display_balance(self) -> None:
        """Display the current balance."""
        print(f"Balance: {self.balance}")


account = BankAccount(1000)

account.deposit(500)
account.display_balance()


# ============================================================
# 12. self REFERS TO THE OBJECT THAT CALLED THE METHOD
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def identify(self) -> None:
        """Display the current object's name."""
        print(f"Current object belongs to {self.name}.")


alice = Person("Alice")
bob = Person("Bob")

alice.identify()
bob.identify()


# ============================================================
# 13. self IS REQUIRED IN INSTANCE METHOD DEFINITIONS
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> None:
        """Greet the person."""
        print(f"Hello, {self.name}.")


person = Person("Alice")

person.greet()

"""
The instance method receives the current object through
its first parameter.

By convention, that parameter is named self.
"""


# ============================================================
# 14. self IS NOT A KEYWORD
# ============================================================

"""
"self" is a naming convention, not a Python keyword.

However, using another name is strongly discouraged because
it makes code less readable and violates normal Python
conventions.

Preferred:

    def display(self):

Not recommended:

    def display(current_object):
"""


# ============================================================
# 15. THE NAME self CAN TECHNICALLY BE CHANGED
# ============================================================

class Example:
    """Demonstrate that self is a convention."""

    def display(current_object) -> None:
        """Display the current object."""
        print(current_object)


example = Example()

example.display()

"""
This works because Python cares about the position of the
parameter, not its name.

However, always use "self" in normal Python code.
"""


# ============================================================
# 16. self AND ATTRIBUTE CREATION
# ============================================================

class Product:
    """Represent a product."""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


product = Product("Laptop", 75000)

print(product.name)
print(product.price)


# ============================================================
# 17. INSTANCE ATTRIBUTES BELONG TO THE INSTANCE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person_one = Person("Alice")
person_two = Person("Bob")

print(person_one.name)
print(person_two.name)


# ============================================================
# 18. self CAN BE USED TO CREATE STATE
# ============================================================

class Light:
    """Represent a simple light."""

    def __init__(self) -> None:
        self.is_on = False

    def turn_on(self) -> None:
        """Turn the light on."""
        self.is_on = True

    def turn_off(self) -> None:
        """Turn the light off."""
        self.is_on = False

    def display_status(self) -> None:
        """Display the current light status."""
        print(f"Light on: {self.is_on}")


light = Light()

light.display_status()

light.turn_on()

light.display_status()

light.turn_off()

light.display_status()


# ============================================================
# 19. self AND MULTIPLE INSTANCE METHODS
# ============================================================

class Temperature:
    """Represent a temperature."""

    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        """Convert Celsius to Fahrenheit."""
        return (self.celsius * 9 / 5) + 32

    def display(self) -> None:
        """Display the temperature."""
        fahrenheit = self.to_fahrenheit()
        print(f"Celsius: {self.celsius}")
        print(f"Fahrenheit: {fahrenheit}")


temperature = Temperature(25)

temperature.display()


# ============================================================
# 20. CONCEPTUAL MODEL OF self
# ============================================================

"""
Consider:

    person = Person("Alice")

    person.introduce()


Conceptually:

    person.introduce()

becomes approximately:

    Person.introduce(person)


Therefore inside introduce():

    self
        ↓
    person


And:

    self.name
        ↓
    person.name
        ↓
    "Alice"


This is the core purpose of self:
it gives an instance method access to the instance on which
the method was called.
"""


# ============================================================
# 21. KEY TAKEAWAY
# ============================================================

"""
self:

    - refers to the current instance
    - is the first parameter of an instance method
    - is automatically supplied when calling instance methods
    - allows access to instance attributes
    - allows one instance method to call another
    - allows an object to maintain its own state

Example:

    class Person:

        def __init__(self, name):
            self.name = name

        def greet(self):
            print(self.name)


    person = Person("Alice")
    person.greet()


Conceptually:

    person.greet()

is similar to:

    Person.greet(person)


Remember:

    self
        -> current object

    self.attribute
        -> attribute belonging to current object

    self.method()
        -> method called on current object


The word "self" is a convention, but it should always be
used for the first parameter of an instance method.
"""