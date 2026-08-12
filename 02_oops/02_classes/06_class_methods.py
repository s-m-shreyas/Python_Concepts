## `06_class_methods.py`

# type: ignore
"""
06_class_methods.py

Demonstrates class methods in Python.

A class method is a method that receives the class itself
as its first argument.

Class methods are created using the @classmethod decorator.

The conventional name for the first parameter is:

    cls

A class method can access and modify class-level state,
and it can be called using either the class or an instance.
"""


# ============================================================
# 1. BASIC CLASS METHOD
# ============================================================

class Person:
    """Represent a person."""

    @classmethod
    def describe_class(cls) -> None:
        """Display the class represented by cls."""
        print(cls)


Person.describe_class()


# ============================================================
# 2. THE cls PARAMETER
# ============================================================

"""
For a class method:

    cls

refers to the class itself.

This is similar to how:

    self

refers to the current instance in an instance method.
"""

class Person:
    """Represent a person."""

    @classmethod
    def show_class(cls) -> None:
        """Display the current class."""
        print(cls.__name__)


Person.show_class()


# ============================================================
# 3. CLASS METHOD CAN ACCESS CLASS ATTRIBUTES
# ============================================================

class Employee:
    """Represent an employee."""

    company = "TechCorp"

    @classmethod
    def show_company(cls) -> None:
        """Display the company name."""
        print(cls.company)


Employee.show_company()


# ============================================================
# 4. CLASS METHODS CAN BE CALLED THROUGH AN INSTANCE
# ============================================================

class Employee:
    """Represent an employee."""

    company = "TechCorp"

    @classmethod
    def show_company(cls) -> None:
        """Display the company name."""
        print(cls.company)


employee = Employee()

Employee.show_company()
employee.show_company()


# ============================================================
# 5. CLASS METHOD RECEIVES THE CLASS AUTOMATICALLY
# ============================================================

class Person:
    """Represent a person."""

    @classmethod
    def identify(cls) -> None:
        """Display the class name."""
        print(f"Class: {cls.__name__}")


Person.identify()

person = Person()
person.identify()


# ============================================================
# 6. CLASS METHOD VS INSTANCE METHOD
# ============================================================

class Person:
    """Represent a person."""

    species = "Human"

    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> None:
        """Display instance-specific information."""
        print(f"Name: {self.name}")

    @classmethod
    def show_species(cls) -> None:
        """Display class-level information."""
        print(f"Species: {cls.species}")


person = Person("Alice")

person.introduce()
person.show_species()


# ============================================================
# 7. CLASS METHODS ACCESS CLASS STATE
# ============================================================

class Counter:
    """Represent a counter shared by all instances."""

    count = 0

    @classmethod
    def increment(cls) -> None:
        """Increase the class-level counter."""
        cls.count += 1

    @classmethod
    def show_count(cls) -> None:
        """Display the class-level counter."""
        print(f"Count: {cls.count}")


Counter.increment()
Counter.increment()
Counter.increment()

Counter.show_count()


# ============================================================
# 8. CLASS METHOD MODIFIES CLASS STATE
# ============================================================

class Configuration:
    """Represent application configuration."""

    environment = "development"

    @classmethod
    def set_environment(cls, environment: str) -> None:
        """Change the class-level environment."""
        cls.environment = environment


print(Configuration.environment)

Configuration.set_environment("production")

print(Configuration.environment)


# ============================================================
# 9. CLASS METHODS DO NOT REQUIRE AN INSTANCE
# ============================================================

class Database:
    """Represent database configuration."""

    connection_count = 0

    @classmethod
    def connect(cls) -> None:
        """Register a database connection."""
        cls.connection_count += 1


Database.connect()
Database.connect()

print(Database.connection_count)


# ============================================================
# 10. CLASS METHOD CAN ACCEPT ADDITIONAL ARGUMENTS
# ============================================================

class Employee:
    """Represent an employee."""

    company = "TechCorp"

    @classmethod
    def create_label(cls, name: str) -> str:
        """Create a company-specific employee label."""
        return f"{name} - {cls.company}"


label = Employee.create_label("Alice")

print(label)


# ============================================================
# 11. CLASS METHODS AS ALTERNATIVE CONSTRUCTORS
# ============================================================

"""
One of the most useful applications of class methods is
creating alternative constructors.

An alternative constructor is another way to create an
instance of a class.
"""

class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data: str) -> "Person":
        """Create a Person from 'name,age' text."""
        name, age_text = data.split(",")

        return cls(name, int(age_text))

    def display(self) -> None:
        """Display person information."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


person = Person.from_string("Alice,30")

person.display()


# ============================================================
# 12. WHY USE cls INSTEAD OF THE CLASS NAME?
# ============================================================

"""
Using cls makes the class method work naturally with
inheritance.

Prefer:

    return cls(...)

instead of:

    return Person(...)

because cls refers to the class that actually called
the class method.
"""

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def create(cls, name: str) -> "Person":
        """Create an instance of the calling class."""
        return cls(name)


person = Person.create("Alice")

print(person.name)


# ============================================================
# 13. CLASS METHOD AND INHERITANCE
# ============================================================

class Person:
    """Represent a person."""

    @classmethod
    def create(cls, name: str) -> "Person":
        """Create an instance of the calling class."""
        return cls(name)

    def __init__(self, name: str) -> None:
        self.name = name


class Employee(Person):
    """Represent an employee."""

    pass


employee = Employee.create("Alice")

print(type(employee))
print(employee.name)


# ============================================================
# 14. cls REPRESENTS THE CALLING CLASS
# ============================================================

class Person:
    """Represent a person."""

    @classmethod
    def show_class(cls) -> None:
        """Display the calling class."""
        print(cls.__name__)


class Employee(Person):
    """Represent an employee."""

    pass


Person.show_class()
Employee.show_class()


# ============================================================
# 15. CLASS METHOD CAN CALL ANOTHER CLASS METHOD
# ============================================================

class Calculator:
    """Provide class-level calculation utilities."""

    @classmethod
    def double(cls, number: int) -> int:
        """Return twice the supplied number."""
        return number * 2

    @classmethod
    def quadruple(cls, number: int) -> int:
        """Return four times the supplied number."""
        return cls.double(cls.double(number))


print(Calculator.quadruple(5))


# ============================================================
# 16. CLASS METHOD VS CLASS ATTRIBUTE
# ============================================================

class Company:
    """Represent company-level information."""

    name = "TechCorp"

    @classmethod
    def get_name(cls) -> str:
        """Return the company name."""
        return cls.name


print(Company.name)
print(Company.get_name())


# ============================================================
# 17. CLASS METHOD DOES NOT RECEIVE self
# ============================================================

"""
An instance method receives:

    self

A class method receives:

    cls

Example:

    def instance_method(self):
        ...


    @classmethod
    def class_method(cls):
        ...

The two parameters represent different objects:

    self
        -> current instance

    cls
        -> current class
"""


# ============================================================
# 18. CLASS METHOD CAN ACCESS CLASS ATTRIBUTES THROUGH cls
# ============================================================

class Product:
    """Represent a product."""

    category = "Electronics"

    @classmethod
    def display_category(cls) -> None:
        """Display the product category."""
        print(cls.category)


Product.display_category()


# ============================================================
# 19. CLASS METHOD CAN CHANGE CLASS-LEVEL CONFIGURATION
# ============================================================

class Application:
    """Represent application-level configuration."""

    debug = False

    @classmethod
    def enable_debug(cls) -> None:
        """Enable debug mode."""
        cls.debug = True

    @classmethod
    def disable_debug(cls) -> None:
        """Disable debug mode."""
        cls.debug = False


print(Application.debug)

Application.enable_debug()

print(Application.debug)

Application.disable_debug()

print(Application.debug)


# ============================================================
# 20. CLASS METHODS CAN BE USED AS FACTORIES
# ============================================================

"""
A factory method creates objects according to some input
or configuration.

This is another common use of class methods.
"""

class User:
    """Represent a user."""

    def __init__(self, username: str, role: str) -> None:
        self.username = username
        self.role = role

    @classmethod
    def create_admin(cls, username: str) -> "User":
        """Create a user with the administrator role."""
        return cls(username, "admin")

    @classmethod
    def create_guest(cls, username: str) -> "User":
        """Create a user with the guest role."""
        return cls(username, "guest")

    def display(self) -> None:
        """Display user information."""
        print(f"Username: {self.username}")
        print(f"Role: {self.role}")


admin = User.create_admin("alice")
guest = User.create_guest("bob")

admin.display()
guest.display()


# ============================================================
# 21. CLASS METHOD AND INSTANCE METHOD CAN COEXIST
# ============================================================

class BankAccount:
    """Represent a bank account."""

    bank_name = "Global Bank"

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Modify instance-specific balance."""
        self.balance += amount

    @classmethod
    def get_bank_name(cls) -> str:
        """Return the shared bank name."""
        return cls.bank_name


account = BankAccount("Alice", 1000)

account.deposit(500)

print(account.balance)
print(account.get_bank_name())


# ============================================================
# 22. CLASS METHOD SHOULD BE USED FOR CLASS-LEVEL LOGIC
# ============================================================

"""
Use a class method when the operation needs information
about the class itself.

Typical situations:

    - accessing class attributes
    - modifying class-level state
    - creating alternative constructors
    - creating factory methods
    - behavior that belongs to the class rather than
      an individual instance
"""


# ============================================================
# 23. CLASS METHOD DOES NOT NEED INSTANCE DATA
# ============================================================

class Temperature:
    """Represent temperature conversion utilities."""

    @classmethod
    def celsius_to_fahrenheit(cls, celsius: float) -> float:
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9 / 5) + 32


print(Temperature.celsius_to_fahrenheit(25))


# ============================================================
# 24. CLASS METHOD DECORATOR
# ============================================================

"""
The @classmethod decorator transforms the function into
a class method.

Without @classmethod:

    def show_class(cls):
        ...


With @classmethod:

    @classmethod
    def show_class(cls):
        ...

The decorator changes how Python binds the method.
"""


# ============================================================
# 25. KEY TAKEAWAY
# ============================================================

"""
A class method:

    - is defined using @classmethod
    - receives the class as its first argument
    - conventionally names that argument cls
    - can access class attributes through cls
    - can modify class-level state
    - can be called through the class
    - can also be called through an instance
    - does not require an instance to exist
    - is commonly used for alternative constructors
    - is commonly used for factory methods


Compare:

    Instance method:

        def method(self):
            ...


        self
            ↓
        current instance


    Class method:

        @classmethod
        def method(cls):
            ...


        cls
            ↓
        current class


The key distinction is:

    self → instance
    cls  → class


Class methods are about behavior associated with the
class itself rather than a particular instance.
"""

