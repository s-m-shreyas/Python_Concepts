# type: ignore

"""
01_method_overriding.py

Demonstrates method overriding in Python.

Method overriding occurs when a child class provides its own
implementation of a method that already exists in its parent
class.

The child implementation replaces the inherited implementation
when the method is called on a child-class object.
"""


# ============================================================
# 1. BASIC METHOD OVERRIDING
# ============================================================

class Animal:
    """Represent a generic animal."""

    def make_sound(self) -> None:
        """Make a generic animal sound."""
        print("Animal makes a sound.")


class Dog(Animal):
    """Represent a dog."""

    def make_sound(self) -> None:
        """Make a dog sound."""
        print("Dog barks.")


animal = Animal()
dog = Dog()

animal.make_sound()
dog.make_sound()


# ============================================================
# 2. CHILD METHOD REPLACES INHERITED IMPLEMENTATION
# ============================================================

class Vehicle:
    """Represent a generic vehicle."""

    def start(self) -> None:
        """Start the vehicle."""
        print("Vehicle starts.")


class Car(Vehicle):
    """Represent a car."""

    def start(self) -> None:
        """Start the car."""
        print("Car starts with a key.")


car = Car()

car.start()

"""
The Car object inherits from Vehicle, but Car provides its
own implementation of start().

Therefore:

    car.start()

uses:

    Car.start()

instead of:

    Vehicle.start()
"""


# ============================================================
# 3. SAME METHOD NAME, DIFFERENT BEHAVIOUR
# ============================================================

class Animal:
    """Represent an animal."""

    def move(self) -> None:
        """Describe animal movement."""
        print("Animal moves.")


class Bird(Animal):
    """Represent a bird."""

    def move(self) -> None:
        """Describe bird movement."""
        print("Bird flies.")


class Fish(Animal):
    """Represent a fish."""

    def move(self) -> None:
        """Describe fish movement."""
        print("Fish swims.")


bird = Bird()
fish = Fish()

bird.move()
fish.move()


# ============================================================
# 4. OVERRIDING WITH DIFFERENT IMPLEMENTATION
# ============================================================

class Employee:
    """Represent an employee."""

    def calculate_salary(self) -> float:
        """Calculate a generic salary."""
        return 30000.0


class Manager(Employee):
    """Represent a manager."""

    def calculate_salary(self) -> float:
        """Calculate manager salary."""
        return 60000.0


class Developer(Employee):
    """Represent a developer."""

    def calculate_salary(self) -> float:
        """Calculate developer salary."""
        return 50000.0


manager = Manager()
developer = Developer()

print(manager.calculate_salary())
print(developer.calculate_salary())


# ============================================================
# 5. OVERRIDING CAN USE INSTANCE DATA
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> None:
        """Introduce the person."""
        print(f"I am {self.name}.")


class Student(Person):
    """Represent a student."""

    def introduce(self) -> None:
        """Introduce the student."""
        print(f"I am {self.name}, and I am a student.")


person = Person("Alice")
student = Student("Bob")

person.introduce()
student.introduce()


# ============================================================
# 6. OVERRIDING CAN EXTEND PARENT BEHAVIOUR
# ============================================================

"""
A child class does not always have to completely replace
the parent's behaviour.

It can also call the parent implementation using super()
and then add its own behaviour.
"""

class Person:
    """Represent a person."""

    def introduce(self) -> None:
        """Introduce a generic person."""
        print("I am a person.")


class Student(Person):
    """Represent a student."""

    def introduce(self) -> None:
        """Extend the parent introduction."""
        super().introduce()
        print("I am also a student.")


student = Student()

student.introduce()


# ============================================================
# 7. OVERRIDING WITH super()
# ============================================================

class Animal:
    """Represent an animal."""

    def make_sound(self) -> None:
        """Make a generic sound."""
        print("Animal makes a sound.")


class Dog(Animal):
    """Represent a dog."""

    def make_sound(self) -> None:
        """Extend the animal sound."""
        super().make_sound()
        print("Dog barks.")


dog = Dog()

dog.make_sound()


# ============================================================
# 8. OVERRIDING WITH INSTANCE ATTRIBUTES
# ============================================================

class Shape:
    """Represent a generic shape."""

    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> None:
        """Describe the shape."""
        print(f"Shape: {self.name}")


class Circle(Shape):
    """Represent a circle."""

    def describe(self) -> None:
        """Describe the circle."""
        print(f"{self.name} is a circle.")


circle = Circle("My Shape")

circle.describe()


# ============================================================
# 9. OVERRIDING WITH ADDITIONAL PARAMETERS
# ============================================================

class Notification:
    """Represent a notification."""

    def send(self, message: str) -> None:
        """Send a generic notification."""
        print(f"Notification: {message}")


class EmailNotification(Notification):
    """Represent an email notification."""

    def send(self, message: str) -> None:
        """Send an email notification."""
        print(f"Email: {message}")


notification = Notification()
email = EmailNotification()

notification.send("Hello")
email.send("Hello")


# ============================================================
# 10. OVERRIDING DOES NOT REQUIRE THE SAME INTERNAL LOGIC
# ============================================================

class Payment:
    """Represent a generic payment."""

    def process(self, amount: float) -> None:
        """Process a generic payment."""
        print(f"Processing payment of {amount}.")


class CreditCardPayment(Payment):
    """Represent a credit card payment."""

    def process(self, amount: float) -> None:
        """Process a credit card payment."""
        print(f"Processing credit card payment of {amount}.")


class UPIPayment(Payment):
    """Represent a UPI payment."""

    def process(self, amount: float) -> None:
        """Process a UPI payment."""
        print(f"Processing UPI payment of {amount}.")


card_payment = CreditCardPayment()
upi_payment = UPIPayment()

card_payment.process(1000)
upi_payment.process(1000)


# ============================================================
# 11. OVERRIDING AND INHERITANCE
# ============================================================

class Animal:
    """Represent an animal."""

    def move(self) -> None:
        """Describe generic movement."""
        print("Animal moves.")


class Mammal(Animal):
    """Represent a mammal."""

    pass


class Dog(Mammal):
    """Represent a dog."""

    def move(self) -> None:
        """Describe dog movement."""
        print("Dog runs.")


dog = Dog()

dog.move()


# ============================================================
# 12. MULTIPLE LEVELS OF OVERRIDING
# ============================================================

class Animal:
    """Represent an animal."""

    def sound(self) -> None:
        """Make a generic sound."""
        print("Animal sound.")


class Mammal(Animal):
    """Represent a mammal."""

    def sound(self) -> None:
        """Make a mammal sound."""
        print("Mammal sound.")


class Dog(Mammal):
    """Represent a dog."""

    def sound(self) -> None:
        """Make a dog sound."""
        print("Dog bark.")


animal = Animal()
mammal = Mammal()
dog = Dog()

animal.sound()
mammal.sound()
dog.sound()


# ============================================================
# 13. OVERRIDING AND super() AT MULTIPLE LEVELS
# ============================================================

class Animal:
    """Represent an animal."""

    def describe(self) -> None:
        """Describe an animal."""
        print("This is an animal.")


class Mammal(Animal):
    """Represent a mammal."""

    def describe(self) -> None:
        """Extend the animal description."""
        super().describe()
        print("It is a mammal.")


class Dog(Mammal):
    """Represent a dog."""

    def describe(self) -> None:
        """Extend the mammal description."""
        super().describe()
        print("It is a dog.")


dog = Dog()

dog.describe()


# ============================================================
# 14. OVERRIDING IS RESOLVED AT RUNTIME
# ============================================================

class Animal:
    """Represent an animal."""

    def sound(self) -> None:
        """Make an animal sound."""
        print("Animal sound.")


class Cat(Animal):
    """Represent a cat."""

    def sound(self) -> None:
        """Make a cat sound."""
        print("Cat meows.")


class Dog(Animal):
    """Represent a dog."""

    def sound(self) -> None:
        """Make a dog sound."""
        print("Dog barks.")


animals = [Cat(), Dog()]

for animal in animals:
    animal.sound()


# ============================================================
# 15. OVERRIDING IS A FOUNDATION OF POLYMORPHISM
# ============================================================

"""
Different child classes can provide different implementations
of the same inherited method.

For example:

    Cat.sound()
        -> "Cat meows."

    Dog.sound()
        -> "Dog barks."

The calling code can use the same method name:

    animal.sound()

while the actual behaviour depends on the object's type.

This idea becomes the foundation for polymorphic behaviour.
"""


# ============================================================
# 16. METHOD OVERRIDING VS METHOD INHERITANCE
# ============================================================

class Parent:
    """Represent a parent class."""

    def show(self) -> None:
        """Display parent behaviour."""
        print("Parent implementation.")


class Child(Parent):
    """Represent a child class."""

    pass


class OverridingChild(Parent):
    """Represent a child that overrides show()."""

    def show(self) -> None:
        """Display child behaviour."""
        print("Child implementation.")


child = Child()
overriding_child = OverridingChild()

child.show()
overriding_child.show()

"""
Child:

    does not override show()
    -> inherits Parent.show()

OverridingChild:

    overrides show()
    -> uses OverridingChild.show()
"""


# ============================================================
# 17. KEY TAKEAWAY
# ============================================================

"""
Method overriding occurs when a child class defines a method
with the same name as a method inherited from its parent.

Example:

    class Parent:

        def show(self):
            print("Parent")


    class Child(Parent):

        def show(self):
            print("Child")


When:

    Child().show()

the child implementation is used.

Key points:

    - The child inherits from the parent.
    - The parent already defines the method.
    - The child defines a method with the same name.
    - The child's implementation takes precedence.
    - super() can be used to access the parent implementation.
    - Different child classes can provide different behaviour.

This is one of the fundamental mechanisms behind
polymorphism in object-oriented programming.
"""