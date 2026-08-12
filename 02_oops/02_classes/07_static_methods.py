# type: ignore
"""
07_static_methods.py

Demonstrates static methods in Python.

A static method is a method that does not automatically
receive either:

    - the current instance (self), or
    - the current class (cls).

Static methods are created using the @staticmethod decorator.

They are useful when a function is logically related to a
class but does not need access to instance or class state.
"""


# ============================================================
# 1. BASIC STATIC METHOD
# ============================================================

class Calculator:
    """Provide calculation utilities."""

    @staticmethod
    def add(first: int, second: int) -> int:
        """Return the sum of two numbers."""
        return first + second


result = Calculator.add(10, 20)

print(result)


# ============================================================
# 2. STATIC METHOD DOES NOT RECEIVE self
# ============================================================

class Calculator:
    """Provide calculation utilities."""

    @staticmethod
    def multiply(first: int, second: int) -> int:
        """Return the product of two numbers."""
        return first * second


print(Calculator.multiply(5, 4))


# ============================================================
# 3. STATIC METHOD DOES NOT RECEIVE cls
# ============================================================

class Temperature:
    """Provide temperature conversion utilities."""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9 / 5) + 32


print(Temperature.celsius_to_fahrenheit(25))


# ============================================================
# 4. STATIC METHOD CAN BE CALLED WITHOUT AN INSTANCE
# ============================================================

class MathUtility:
    """Provide mathematical utilities."""

    @staticmethod
    def square(number: int) -> int:
        """Return the square of a number."""
        return number**2


print(MathUtility.square(6))


# ============================================================
# 5. STATIC METHOD CAN ALSO BE CALLED THROUGH AN INSTANCE
# ============================================================

class MathUtility:
    """Provide mathematical utilities."""

    @staticmethod
    def cube(number: int) -> int:
        """Return the cube of a number."""
        return number**3


utility = MathUtility()

print(utility.cube(4))


# ============================================================
# 6. STATIC METHOD DOES NOT DEPEND ON INSTANCE STATE
# ============================================================

class Rectangle:
    """Represent a rectangle."""

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    @staticmethod
    def calculate_area(length: float, width: float) -> float:
        """Calculate rectangle area."""
        return length * width


rectangle = Rectangle(10, 5)

print(rectangle.calculate_area(10, 5))
print(Rectangle.calculate_area(10, 5))


# ============================================================
# 7. INSTANCE METHOD VS STATIC METHOD
# ============================================================

class Circle:
    """Represent a circle."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        """Calculate area using instance state."""
        return 3.14159 * self.radius**2

    @staticmethod
    def calculate_area(radius: float) -> float:
        """Calculate area using supplied data."""
        return 3.14159 * radius**2


circle = Circle(5)

print(circle.area())
print(Circle.calculate_area(5))


# ============================================================
# 8. WHEN self IS REQUIRED
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> None:
        """Use instance-specific state."""
        print(f"My name is {self.name}.")


person = Person("Alice")

person.introduce()


# ============================================================
# 9. WHEN self IS NOT REQUIRED
# ============================================================

class Person:
    """Provide person-related utilities."""

    @staticmethod
    def is_adult(age: int) -> bool:
        """Return whether an age represents an adult."""
        return age >= 18


print(Person.is_adult(25))
print(Person.is_adult(15))


# ============================================================
# 10. STATIC METHOD DOES NOT ACCESS INSTANCE ATTRIBUTES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def create_greeting(name: str) -> str:
        """Create a greeting from supplied data."""
        return f"Hello, {name}!"


person = Person("Alice")

print(person.create_greeting("Bob"))


# ============================================================
# 11. STATIC METHOD DOES NOT ACCESS CLASS STATE
# ============================================================

class Employee:
    """Represent an employee."""

    company = "TechCorp"

    @staticmethod
    def format_name(name: str) -> str:
        """Format an employee name."""
        return name.strip().title()


print(Employee.format_name("  alice  "))


# ============================================================
# 12. STATIC METHOD AS A VALIDATION UTILITY
# ============================================================

class User:
    """Represent a user."""

    @staticmethod
    def is_valid_username(username: str) -> bool:
        """Validate a username."""
        return username.isalnum() and len(username) >= 4


print(User.is_valid_username("alice123"))
print(User.is_valid_username("ab"))


# ============================================================
# 13. STATIC METHOD AS A CONVERSION UTILITY
# ============================================================

class Measurement:
    """Provide measurement utilities."""

    @staticmethod
    def kilometers_to_miles(kilometers: float) -> float:
        """Convert kilometers to miles."""
        return kilometers * 0.621371


distance = Measurement.kilometers_to_miles(10)

print(distance)


# ============================================================
# 14. STATIC METHOD AS A FORMATTING UTILITY
# ============================================================

class Product:
    """Represent a product."""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    @staticmethod
    def format_price(price: float) -> str:
        """Format a numeric price."""
        return f"₹{price:,.2f}"


product = Product("Laptop", 75000)

print(product.format_price(product.price))
print(Product.format_price(125000))


# ============================================================
# 15. STATIC METHOD CAN ACCEPT ANY NORMAL PARAMETERS
# ============================================================

class StringUtility:
    """Provide string utilities."""

    @staticmethod
    def join_words(first: str, second: str) -> str:
        """Join two words."""
        return f"{first} {second}"


print(StringUtility.join_words("Hello", "Python"))


# ============================================================
# 16. STATIC METHOD CAN USE OTHER STATIC METHODS
# ============================================================

class NumberUtility:
    """Provide number-related utilities."""

    @staticmethod
    def square(number: int) -> int:
        """Return the square of a number."""
        return number**2

    @staticmethod
    def square_and_double(number: int) -> int:
        """Square a number and then double the result."""
        return NumberUtility.square(number) * 2


print(NumberUtility.square_and_double(5))


# ============================================================
# 17. STATIC METHOD CAN ALSO BE CALLED THROUGH self
# ============================================================

class Calculator:
    """Provide calculation utilities."""

    @staticmethod
    def add(first: int, second: int) -> int:
        """Return the sum."""
        return first + second

    def calculate(self, first: int, second: int) -> int:
        """Use the static method."""
        return self.add(first, second)


calculator = Calculator()

print(calculator.calculate(10, 20))


# ============================================================
# 18. STATIC METHOD VS CLASS METHOD
# ============================================================

class Employee:
    """Demonstrate class and static methods."""

    company = "TechCorp"

    @classmethod
    def get_company(cls) -> str:
        """Return class-level information."""
        return cls.company

    @staticmethod
    def format_name(name: str) -> str:
        """Format a name without using class state."""
        return name.strip().title()


print(Employee.get_company())
print(Employee.format_name("  alice  "))


# ============================================================
# 19. STATIC METHOD VS INSTANCE METHOD
# ============================================================

class Employee:
    """Demonstrate instance and static methods."""

    def __init__(self, name: str) -> None:
        self.name = name

    def display_name(self) -> None:
        """Display instance-specific information."""
        print(self.name)

    @staticmethod
    def format_name(name: str) -> str:
        """Format a supplied name."""
        return name.strip().title()


employee = Employee("Alice")

employee.display_name()
print(employee.format_name("  bob  "))


# ============================================================
# 20. THREE TYPES OF METHODS
# ============================================================

"""
Python classes commonly use three types of methods:

1. Instance method

    def method(self):
        ...

    self → current instance


2. Class method

    @classmethod
    def method(cls):
        ...

    cls → current class


3. Static method

    @staticmethod
    def method():
        ...

    No automatic self or cls.


Conceptually:

                    METHOD
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
    INSTANCE         CLASS          STATIC
      self             cls          nothing
        │              │              │
    object           class       independent
"""


# ============================================================
# 21. STATIC METHOD IS STILL A FUNCTION
# ============================================================

class Utility:
    """Provide utility operations."""

    @staticmethod
    def add(first: int, second: int) -> int:
        """Return the sum."""
        return first + second


print(Utility.add(10, 20))


# ============================================================
# 22. STATIC METHOD IS USEFUL FOR CLASS-RELATED LOGIC
# ============================================================

"""
A static method does not need to access the class or an
instance.

So why put it inside a class?

Because the operation is logically related to that class.

For example:

    User.is_valid_username()

is conceptually related to User.

It could exist as a standalone function, but placing it
inside User groups related behavior together.
"""


# ============================================================
# 23. STATIC METHOD WITH CONDITIONAL LOGIC
# ============================================================

class NumberUtility:
    """Provide number-related utilities."""

    @staticmethod
    def classify(number: int) -> str:
        """Classify a number."""
        if number > 0:
            return "Positive"

        if number < 0:
            return "Negative"

        return "Zero"


print(NumberUtility.classify(10))
print(NumberUtility.classify(-5))
print(NumberUtility.classify(0))


# ============================================================
# 24. STATIC METHOD DOES NOT NEED THE CLASS NAME INTERNALLY
# ============================================================

class Converter:
    """Provide conversion utilities."""

    @staticmethod
    def meters_to_centimeters(meters: float) -> float:
        """Convert meters to centimeters."""
        return meters * 100


print(Converter.meters_to_centimeters(2.5))


# ============================================================
# 25. KEY TAKEAWAY
# ============================================================

"""
A static method:

    - is created using @staticmethod
    - does not receive self automatically
    - does not receive cls automatically
    - does not depend on instance state
    - does not depend on class state
    - can be called through the class
    - can also be called through an instance
    - behaves essentially like a regular function grouped
      inside a class

Use a static method when:

    - the operation logically belongs to the class
    - but it does not need self
    - and it does not need cls


Compare:

    Instance method:

        def method(self):
            ...

        Needs instance.


    Class method:

        @classmethod
        def method(cls):
            ...

        Needs class.


    Static method:

        @staticmethod
        def method():
            ...

        Needs neither.


The key idea:

    self → instance
    cls  → class
    static method → neither
"""