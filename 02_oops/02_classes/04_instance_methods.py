# type: ignore
"""
04_instance_methods.py

Introduces instance methods in Python.

This file focuses on:

    - What an instance method is
    - Defining instance methods
    - Calling instance methods
    - The role of self
    - Instance methods accessing instance attributes
    - Instance methods modifying instance state
    - Returning values from instance methods
    - Multiple instance methods
    - Methods operating independently on different objects
    - Method calls through instances

The following topics are covered separately:

    05_self_parameter.py
        -> Detailed behavior of the self parameter

    06_class_methods.py
        -> @classmethod

    07_static_methods.py
        -> @staticmethod

    08_method_binding.py
        -> Method binding and bound methods
"""


# ============================================================
# 1. WHAT IS AN INSTANCE METHOD?
# ============================================================

"""
An instance method is a function defined inside a class that
is intended to operate on an instance of that class.

The first parameter is conventionally named self.
"""


class Person:
    """Represent a person."""

    def greet(self) -> None:
        """Print a greeting."""
        print("Hello!")


person = Person()

person.greet()


# ============================================================
# 2. DEFINING A BASIC INSTANCE METHOD
# ============================================================

"""
The general structure is:

    class ClassName:

        def method_name(self):
            ...


The method becomes part of the class definition.
"""


class Calculator:
    """Provide calculator operations."""

    def add(self, first: int, second: int) -> int:
        """Return the sum of two numbers."""
        return first + second


calculator = Calculator()

result = calculator.add(10, 20)

print(result)


# ============================================================
# 3. CALLING AN INSTANCE METHOD
# ============================================================

"""
An instance method is normally called through an instance:

    instance.method()

For example:

    person.greet()
"""


class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


person = Person()

message = person.greet()

print(message)


# ============================================================
# 4. INSTANCE METHODS CAN ACCESS INSTANCE ATTRIBUTES
# ============================================================

"""
Instance methods commonly work with attributes stored on the
instance.

The instance is accessed through self.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a personalized greeting."""
        return f"Hello, {self.name}!"


person = Person("Shreyas")

print(person.greet())


# ============================================================
# 5. INSTANCE METHODS CAN READ INSTANCE STATE
# ============================================================

"""
An instance method can read values stored in the instance.
"""


class Account:
    """Represent a bank account."""

    def __init__(self, balance: float) -> None:
        self.balance = balance

    def get_balance(self) -> float:
        """Return the current balance."""
        return self.balance


account = Account(5000.0)

print(account.get_balance())


# ============================================================
# 6. INSTANCE METHODS CAN MODIFY INSTANCE STATE
# ============================================================

"""
Instance methods can also change attributes belonging to the
instance.
"""


class Counter:
    """Represent a counter."""

    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        """Increase the counter by one."""
        self.value += 1


counter = Counter()

print(counter.value)

counter.increment()

print(counter.value)

counter.increment()

print(counter.value)


# ============================================================
# 7. INSTANCE METHODS OPERATE ON THE PARTICULAR INSTANCE
# ============================================================

"""
When an instance method is called through an object, that
object is the instance the method operates on.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> str:
        """Return an introduction."""
        return f"My name is {self.name}."


first = Person("Shreyas")
second = Person("Rahul")

print(first.introduce())
print(second.introduce())


# ============================================================
# 8. DIFFERENT INSTANCES HAVE INDEPENDENT STATE
# ============================================================

"""
The same instance method can operate on different instances.

Each instance has its own state.
"""


class Counter:
    """Represent a counter."""

    def __init__(self, value: int = 0) -> None:
        self.value = value

    def increment(self) -> None:
        """Increase the counter."""
        self.value += 1


first = Counter()
second = Counter()

first.increment()
first.increment()

second.increment()

print(first.value)
print(second.value)


# ============================================================
# 9. INSTANCE METHODS CAN RETURN VALUES
# ============================================================

"""
An instance method behaves like a normal function in that it
can return a value.
"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        """Return the rectangle's area."""
        return self.length * self.width


rectangle = Rectangle(10.0, 5.0)

print(rectangle.area())


# ============================================================
# 10. INSTANCE METHODS CAN RECEIVE ADDITIONAL ARGUMENTS
# ============================================================

"""
self represents the instance.

Other parameters represent additional values supplied by the
caller.
"""


class Calculator:
    """Provide calculator operations."""

    def add(self, first: int, second: int) -> int:
        """Return the sum."""
        return first + second


calculator = Calculator()

print(calculator.add(10, 20))


# ============================================================
# 11. self IS NOT PASSED EXPLICITLY IN NORMAL METHOD CALLS
# ============================================================

"""
When calling:

    calculator.add(10, 20)

you normally provide only:

    10
    20

Python supplies the instance automatically as self.

So conceptually:

    calculator.add(10, 20)

is associated with:

    Calculator.add(calculator, 10, 20)

The mechanics of this binding are covered in detail in:

    08_method_binding.py
"""


class Calculator:
    """Provide calculator operations."""

    def add(self, first: int, second: int) -> int:
        """Return the sum."""
        return first + second


calculator = Calculator()

print(calculator.add(10, 20))


# ============================================================
# 12. INSTANCE METHODS CAN ACCESS MULTIPLE ATTRIBUTES
# ============================================================

"""
An instance method can work with multiple pieces of instance
state.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def describe(self) -> str:
        """Return a description."""
        return f"{self.name} is {self.age} years old."


person = Person("Shreyas", 29)

print(person.describe())


# ============================================================
# 13. INSTANCE METHODS CAN MODIFY MULTIPLE ATTRIBUTES
# ============================================================

"""
A method can update more than one instance attribute.
"""


class BankAccount:
    """Represent a bank account."""

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        self.balance += amount


account = BankAccount("Shreyas", 5000.0)

account.deposit(2000.0)

print(account.owner)
print(account.balance)


# ============================================================
# 14. INSTANCE METHODS CAN CALL OTHER INSTANCE METHODS
# ============================================================

"""
An instance method can call another instance method using self.
"""


class Calculator:
    """Provide calculator operations."""

    def add(self, first: int, second: int) -> int:
        """Return the sum."""
        return first + second

    def calculate_total(self, first: int, second: int) -> int:
        """Calculate a total using add()."""
        return self.add(first, second)


calculator = Calculator()

print(calculator.calculate_total(10, 20))


# ============================================================
# 15. MULTIPLE INSTANCE METHODS CAN SHARE STATE
# ============================================================

"""
Methods belonging to the same class can work with the same
instance state.
"""


class Counter:
    """Represent a counter."""

    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        """Increase the counter."""
        self.value += 1

    def decrement(self) -> None:
        """Decrease the counter."""
        self.value -= 1

    def current_value(self) -> int:
        """Return the current value."""
        return self.value


counter = Counter()

counter.increment()
counter.increment()
counter.decrement()

print(counter.current_value())


# ============================================================
# 16. INSTANCE METHODS CAN USE CONDITIONAL LOGIC
# ============================================================

"""
Instance methods can contain normal control-flow logic.
"""


class BankAccount:
    """Represent a bank account."""

    def __init__(self, balance: float) -> None:
        self.balance = balance

    def can_withdraw(self, amount: float) -> bool:
        """Return whether the requested amount can be withdrawn."""
        return amount <= self.balance


account = BankAccount(5000.0)

print(account.can_withdraw(2000.0))
print(account.can_withdraw(6000.0))


# ============================================================
# 17. INSTANCE METHODS CAN CONTAIN LOOPS
# ============================================================

"""
Instance methods are normal function bodies, so loops can be
used when appropriate.
"""


class NumberCollection:
    """Represent a collection of numbers."""

    def __init__(self, numbers: list[int]) -> None:
        self.numbers = numbers

    def total(self) -> int:
        """Return the sum of all numbers."""
        total = 0

        for number in self.numbers:
            total += number

        return total


collection = NumberCollection([10, 20, 30])

print(collection.total())


# ============================================================
# 18. INSTANCE METHODS CAN RETURN DIFFERENT DATA TYPES
# ============================================================

"""
An instance method can return any appropriate value according
to its purpose and annotation.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_name(self) -> str:
        """Return the person's name."""
        return self.name

    def get_age(self) -> int:
        """Return the person's age."""
        return self.age

    def get_details(self) -> dict[str, str | int]:
        """Return the person's details."""
        return {
            "name": self.name,
            "age": self.age,
        }


person = Person("Shreyas", 29)

print(person.get_name())
print(person.get_age())
print(person.get_details())


# ============================================================
# 19. INSTANCE METHODS CAN RETURN self
# ============================================================

"""
An instance method can return the current instance.

This pattern is sometimes used for method chaining.

The concept of self itself is covered in greater detail in:

    05_self_parameter.py
"""


class Counter:
    """Represent a counter."""

    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> "Counter":
        """Increment and return this instance."""
        self.value += 1
        return self


counter = Counter()

counter.increment().increment()

print(counter.value)


# ============================================================
# 20. INSTANCE METHODS CAN ACCEPT OBJECTS
# ============================================================

"""
An instance method can receive another object as an argument.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def introduce_to(self, other: "Person") -> str:
        """Return an introduction to another person."""
        return f"{self.name} meets {other.name}."


first = Person("Shreyas")
second = Person("Rahul")

print(first.introduce_to(second))


# ============================================================
# 21. INSTANCE METHODS CAN COMPARE INSTANCE STATE
# ============================================================

"""
Methods can compare the current object's state with another
object's state.
"""


class Product:
    """Represent a product."""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def is_more_expensive_than(self, other: "Product") -> bool:
        """Return whether this product costs more."""
        return self.price > other.price


laptop = Product("Laptop", 75000.0)
phone = Product("Phone", 50000.0)

print(laptop.is_more_expensive_than(phone))


# ============================================================
# 22. INSTANCE METHODS CAN UPDATE STATE BASED ON ARGUMENTS
# ============================================================

"""
An instance method can combine existing instance state with
values supplied by the caller.
"""


class BankAccount:
    """Represent a bank account."""

    def __init__(self, balance: float) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add money to the balance."""
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Subtract money from the balance."""
        self.balance -= amount


account = BankAccount(5000.0)

account.deposit(1000.0)
account.withdraw(500.0)

print(account.balance)


# ============================================================
# 23. INSTANCE METHODS OPERATE ON THE CALLING INSTANCE
# ============================================================

"""
Consider:

    first.greet()
    second.greet()

The same method definition is used in both cases.

The important difference is the instance supplied as self.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a personalized greeting."""
        return f"Hello, {self.name}!"


first = Person("Shreyas")
second = Person("Rahul")

print(first.greet())
print(second.greet())


# ============================================================
# 24. SAME METHOD, DIFFERENT INSTANCE STATE
# ============================================================

"""
The method definition belongs to the class.

The data it operates on belongs to each instance.
"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        """Return the area."""
        return self.length * self.width


small = Rectangle(5.0, 4.0)
large = Rectangle(10.0, 8.0)

print(small.area())
print(large.area())


# ============================================================
# 25. INSTANCE METHODS ARE DEFINED ON THE CLASS
# ============================================================

"""
The method definition is stored as part of the class.

It is not separately defined inside every instance.
"""


class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


print(Person.__dict__["greet"])


# ============================================================
# 26. INSTANCES ACCESS METHODS THROUGH THE CLASS
# ============================================================

"""
An instance can access methods defined by its class.
"""


class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


person = Person()

print(person.greet())


# ============================================================
# 27. INSTANCE METHOD DOES NOT NEED TO MODIFY STATE
# ============================================================

"""
An instance method can simply use instance state without
changing it.
"""


class Circle:
    """Represent a circle."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def diameter(self) -> float:
        """Return the diameter."""
        return self.radius * 2


circle = Circle(10.0)

print(circle.diameter())


# ============================================================
# 28. INSTANCE METHOD CAN BE PURELY BEHAVIORAL
# ============================================================

"""
A method may use instance state to perform an operation and
return the result without changing the object.
"""


class Temperature:
    """Represent a temperature."""

    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    def fahrenheit(self) -> float:
        """Convert Celsius to Fahrenheit."""
        return (self.celsius * 9 / 5) + 32


temperature = Temperature(25.0)

print(temperature.fahrenheit())


# ============================================================
# 29. INSTANCE METHOD CAN MODIFY THE SAME INSTANCE REPEATEDLY
# ============================================================

"""
Calling the same method multiple times operates on the same
instance when the calls are made through the same variable.
"""


class Counter:
    """Represent a counter."""

    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        """Increase the counter."""
        self.value += 1


counter = Counter()

counter.increment()
counter.increment()
counter.increment()

print(counter.value)


# ============================================================
# 30. INSTANCE METHODS AND INSTANCE ATTRIBUTES WORK TOGETHER
# ============================================================

"""
A common class design pattern is:

    __init__()
        -> establish initial instance state

    instance methods
        -> operate on that state
"""


class BankAccount:
    """Represent a bank account."""

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Deposit money."""
        self.balance += amount

    def get_balance(self) -> float:
        """Return the current balance."""
        return self.balance


account = BankAccount("Shreyas", 5000.0)

account.deposit(1500.0)

print(account.get_balance())


# ============================================================
# 31. INSTANCE METHODS CAN USE CLASS ATTRIBUTES
# ============================================================

"""
An instance method can also access class-level attributes.

The lookup rules involved here become more important when
learning namespaces and inheritance.
"""


class Employee:
    """Represent an employee."""

    company = "ABC Technologies"

    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        """Return employee information."""
        return f"{self.name} works at {self.company}."


employee = Employee("Shreyas")

print(employee.describe())


# ============================================================
# 32. INSTANCE METHODS CAN ACCESS OTHER INSTANCE ATTRIBUTES
# ============================================================

"""
An instance method can access any appropriate attribute
available through self.
"""


class Student:
    """Represent a student."""

    def __init__(self, name: str, marks: int) -> None:
        self.name = name
        self.marks = marks

    def passed(self) -> bool:
        """Return whether the student passed."""
        return self.marks >= 40


student = Student("Shreyas", 75)

print(student.passed())


# ============================================================
# 33. INSTANCE METHOD CALL WITH EXPLICIT CLASS SYNTAX
# ============================================================

"""
An instance method can also be accessed through the class.

When doing so, the instance must be supplied explicitly.

For example:

    Person.greet(person)

This is valid Python, but normal code generally uses:

    person.greet()

The difference becomes important when studying method
binding.
"""


class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


person = Person()

print(person.greet())
print(Person.greet(person))


# ============================================================
# 34. INSTANCE METHODS ARE REUSABLE
# ============================================================

"""
One method definition can operate on many instances.
"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        """Return the area."""
        return self.length * self.width


rectangles = [
    Rectangle(5.0, 4.0),
    Rectangle(10.0, 2.0),
    Rectangle(7.0, 3.0),
]

for rectangle in rectangles:
    print(rectangle.area())


# ============================================================
# 35. INSTANCE METHODS DEFINE OBJECT BEHAVIOR
# ============================================================

"""
A useful mental model is:

    Attributes
        -> represent object state

    Instance methods
        -> define behavior that operates on that state
"""


class Light:
    """Represent a light."""

    def __init__(self) -> None:
        self.is_on = False

    def turn_on(self) -> None:
        """Turn the light on."""
        self.is_on = True

    def turn_off(self) -> None:
        """Turn the light off."""
        self.is_on = False


light = Light()

print(light.is_on)

light.turn_on()

print(light.is_on)

light.turn_off()

print(light.is_on)


# ============================================================
# 36. CONCEPTUAL MODEL
# ============================================================

"""
Think of an instance method like this:

    Class
      |
      +---- method definition
                 |
                 | called through
                 v
              Instance
                 |
                 v
             self refers
             to that instance


For:

    person.greet()

the method operates on person.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a greeting."""
        return f"Hello, {self.name}!"


person = Person("Shreyas")

print(person.greet())


# ============================================================
# 37. KEY DISTINCTION: METHOD VS FUNCTION
# ============================================================

"""
A function can exist independently:

    def greet():
        ...


An instance method is defined inside a class:

    class Person:
        def greet(self):
            ...


The same underlying function/method mechanics become clearer
when studying method binding.
"""


def standalone_greet() -> str:
    """Return a standalone greeting."""
    return "Hello from function!"


class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a method greeting."""
        return "Hello from method!"


person = Person()

print(standalone_greet())
print(person.greet())


# ============================================================
# 38. INSTANCE METHODS AND self
# ============================================================

"""
The self parameter represents the current instance.

For example:

    person.greet()

means that the greet method operates on person.

A detailed treatment of self is intentionally kept in:

    05_self_parameter.py
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a greeting."""
        return f"Hello, {self.name}!"


person = Person("Shreyas")

print(person.greet())


# ============================================================
# 39. INSTANCE METHODS AND OBJECT STATE
# ============================================================

"""
The relationship can be summarized as:

    Object
      |
      +-- state
      |     |
      |     +-- instance attributes
      |
      +-- behavior
            |
            +-- instance methods
"""


class Car:
    """Represent a car."""

    def __init__(self, brand: str, speed: int) -> None:
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount: int) -> None:
        """Increase the car's speed."""
        self.speed += amount

    def current_speed(self) -> int:
        """Return the current speed."""
        return self.speed


car = Car("Toyota", 40)

car.accelerate(20)

print(car.current_speed())


# ============================================================
# 40. FINAL EXAMPLE
# ============================================================

"""
A complete but simple class using instance methods.
"""


class BankAccount:
    """Represent a bank account."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account."""
        self.balance -= amount

    def get_balance(self) -> float:
        """Return the current balance."""
        return self.balance

    def describe(self) -> str:
        """Return account information."""
        return f"{self.owner}: ₹{self.balance:.2f}"


account = BankAccount("Shreyas", 5000.0)

account.deposit(2000.0)
account.withdraw(500.0)

print(account.get_balance())
print(account.describe())


# ============================================================
# 41. KEY TAKEAWAYS
# ============================================================

"""
Key concepts:

1. An instance method is a function defined inside a class
   that operates on an instance.

2. Instance methods normally have self as their first
   parameter.

3. Instance methods are normally called through an instance:

       instance.method()

4. Python supplies the instance as self during a normal
   instance-method call.

5. Instance methods can read instance attributes.

6. Instance methods can modify instance attributes.

7. Instance methods can return values.

8. Instance methods can accept additional arguments.

9. The same method definition can operate on many instances.

10. Different instances maintain independent instance state.

11. An instance method can call another instance method using
    self.

12. An instance method can access class-level attributes.

13. The method definition belongs to the class, while the
    state it operates on commonly belongs to the instance.

14. An instance method can technically be called through the
    class by explicitly supplying the instance:

        Class.method(instance)

15. The normal form is:

        instance.method()

16. self represents the current instance.

17. The detailed mechanics of self are covered in:

        05_self_parameter.py

18. The detailed mechanics of automatic method binding are
    covered in:

        08_method_binding.py

The next file:

    05_self_parameter.py

will focus specifically on the self parameter, including what
it represents, why it is explicitly written in the method
definition, and how Python supplies it during method calls.
"""