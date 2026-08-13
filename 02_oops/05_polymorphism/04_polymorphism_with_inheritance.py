# type: ignore

"""
04_polymorphism_with_inheritance.py

Demonstrates polymorphism through inheritance.

Inheritance-based polymorphism occurs when a parent class
defines a common interface and child classes provide their
own implementations of that interface.

The same parent-type reference or function can then work
with objects of different child classes.

This file combines:

    - inheritance
    - method overriding
    - polymorphic behaviour
    - runtime method dispatch
"""


# ============================================================
# 1. BASIC POLYMORPHISM THROUGH INHERITANCE
# ============================================================

class Animal:
    """Represent a generic animal."""

    def speak(self) -> None:
        """Make a generic animal sound."""
        print("Animal makes a sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> None:
        """Make the dog sound."""
        print("Dog barks.")


class Cat(Animal):
    """Represent a cat."""

    def speak(self) -> None:
        """Make the cat sound."""
        print("Cat meows.")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# ============================================================
# 2. CHILD CLASSES SHARE THE PARENT INTERFACE
# ============================================================

"""
Animal defines:

    speak()

Dog and Cat inherit from Animal and override speak().

Therefore, all three classes provide the same operation:

    speak()

but the child classes provide different implementations.
"""

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
dog.speak()
cat.speak()


# ============================================================
# 3. PARENT TYPE CAN REFER TO CHILD OBJECTS
# ============================================================

"""
A variable annotated as Animal can refer to an object of
a child class because Dog and Cat are Animals.
"""

animal: Animal = Dog()

animal.speak()

animal = Cat()

animal.speak()


# ============================================================
# 4. RUNTIME METHOD DISPATCH
# ============================================================

"""
The important point is that the method implementation is
selected according to the actual object at runtime.

The variable:

    animal

has the type:

    Animal

but the actual object may be:

    Dog
    Cat

Python therefore calls the implementation belonging to the
actual object.
"""

animal: Animal = Dog()

animal.speak()

animal = Cat()

animal.speak()


# ============================================================
# 5. POLYMORPHIC FUNCTION WITH A PARENT TYPE
# ============================================================

def make_sound(animal: Animal) -> None:
    """Make an animal produce its sound."""
    animal.speak()


make_sound(Dog())
make_sound(Cat())


# ============================================================
# 6. ONE FUNCTION, MULTIPLE CHILD TYPES
# ============================================================

class Animal:
    """Represent a generic animal."""

    def speak(self) -> None:
        """Make a generic sound."""
        print("Animal sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> None:
        """Make a dog sound."""
        print("Woof!")


class Cat(Animal):
    """Represent a cat."""

    def speak(self) -> None:
        """Make a cat sound."""
        print("Meow!")


class Bird(Animal):
    """Represent a bird."""

    def speak(self) -> None:
        """Make a bird sound."""
        print("Chirp!")


def make_sound(animal: Animal) -> None:
    """Make the supplied animal speak."""
    animal.speak()


make_sound(Dog())
make_sound(Cat())
make_sound(Bird())


# ============================================================
# 7. POLYMORPHISM WITH A COLLECTION
# ============================================================

animals: list[Animal] = [
    Dog(),
    Cat(),
    Bird(),
]


for animal in animals:
    animal.speak()


# ============================================================
# 8. EACH CHILD PROVIDES DIFFERENT BEHAVIOUR
# ============================================================

class Animal:
    """Represent a generic animal."""

    def move(self) -> None:
        """Describe generic movement."""
        print("Animal moves.")


class Dog(Animal):
    """Represent a dog."""

    def move(self) -> None:
        """Describe dog movement."""
        print("Dog runs.")


class Fish(Animal):
    """Represent a fish."""

    def move(self) -> None:
        """Describe fish movement."""
        print("Fish swims.")


class Bird(Animal):
    """Represent a bird."""

    def move(self) -> None:
        """Describe bird movement."""
        print("Bird flies.")


animals: list[Animal] = [
    Dog(),
    Fish(),
    Bird(),
]


for animal in animals:
    animal.move()


# ============================================================
# 9. POLYMORPHISM WITH BUSINESS OBJECTS
# ============================================================

class Employee:
    """Represent a generic employee."""

    def calculate_salary(self) -> float:
        """Return a generic salary."""
        return 30000.0


class Developer(Employee):
    """Represent a developer."""

    def calculate_salary(self) -> float:
        """Return a developer salary."""
        return 50000.0


class Manager(Employee):
    """Represent a manager."""

    def calculate_salary(self) -> float:
        """Return a manager salary."""
        return 70000.0


class Intern(Employee):
    """Represent an intern."""

    def calculate_salary(self) -> float:
        """Return an intern salary."""
        return 20000.0


employees: list[Employee] = [
    Developer(),
    Manager(),
    Intern(),
]


for employee in employees:
    print(employee.calculate_salary())


# ============================================================
# 10. POLYMORPHIC FUNCTION WITH EMPLOYEES
# ============================================================

def display_salary(employee: Employee) -> None:
    """Display an employee's salary."""
    print(f"Salary: {employee.calculate_salary()}")


display_salary(Developer())
display_salary(Manager())
display_salary(Intern())


# ============================================================
# 11. POLYMORPHISM WITH SHAPES
# ============================================================

class Shape:
    """Represent a generic shape."""

    def area(self) -> float:
        """Return a generic area."""
        return 0.0


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        """Calculate the circle area."""
        return 3.14159 * self.radius**2


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate the rectangle area."""
        return self.length * self.width


class Square(Shape):
    """Represent a square."""

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        """Calculate the square area."""
        return self.side**2


shapes: list[Shape] = [
    Circle(5),
    Rectangle(10, 5),
    Square(4),
]


for shape in shapes:
    print(shape.area())


# ============================================================
# 12. POLYMORPHISM HIDES IMPLEMENTATION DETAILS
# ============================================================

"""
The following function knows only that it receives a Shape.

It does not need to know:

    - whether it is a Circle
    - whether it is a Rectangle
    - whether it is a Square
    - how each shape calculates its area
"""

def display_area(shape: Shape) -> None:
    """Display the area of a shape."""
    print(f"Area: {shape.area()}")


display_area(Circle(5))
display_area(Rectangle(10, 5))
display_area(Square(4))


# ============================================================
# 13. ADDING A NEW CHILD CLASS
# ============================================================

class Triangle(Shape):
    """Represent a triangle."""

    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        """Calculate the triangle area."""
        return 0.5 * self.base * self.height


"""
The display_area() function does not need to change.

Triangle simply follows the Shape interface.
"""

display_area(Triangle(10, 6))


# ============================================================
# 14. POLYMORPHISM WITH PAYMENT METHODS
# ============================================================

class Payment:
    """Represent a generic payment."""

    def process(self, amount: float) -> None:
        """Process a generic payment."""
        print(f"Processing payment: {amount}")


class CreditCardPayment(Payment):
    """Represent a credit card payment."""

    def process(self, amount: float) -> None:
        """Process a credit card payment."""
        print(f"Processing credit card payment: {amount}")


class UPIPayment(Payment):
    """Represent a UPI payment."""

    def process(self, amount: float) -> None:
        """Process a UPI payment."""
        print(f"Processing UPI payment: {amount}")


class CashPayment(Payment):
    """Represent a cash payment."""

    def process(self, amount: float) -> None:
        """Process a cash payment."""
        print(f"Processing cash payment: {amount}")


def process_payment(payment: Payment, amount: float) -> None:
    """Process a payment using polymorphic behaviour."""
    payment.process(amount)


process_payment(CreditCardPayment(), 1000)
process_payment(UPIPayment(), 1000)
process_payment(CashPayment(), 1000)


# ============================================================
# 15. POLYMORPHISM WITH MEDIA PLAYERS
# ============================================================

class MediaPlayer:
    """Represent a generic media player."""

    def play(self) -> None:
        """Play media."""
        print("Playing media.")


class AudioPlayer(MediaPlayer):
    """Represent an audio player."""

    def play(self) -> None:
        """Play audio."""
        print("Playing audio.")


class VideoPlayer(MediaPlayer):
    """Represent a video player."""

    def play(self) -> None:
        """Play video."""
        print("Playing video.")


class PodcastPlayer(MediaPlayer):
    """Represent a podcast player."""

    def play(self) -> None:
        """Play a podcast."""
        print("Playing podcast.")


def start_player(player: MediaPlayer) -> None:
    """Start a media player."""
    player.play()


players: list[MediaPlayer] = [
    AudioPlayer(),
    VideoPlayer(),
    PodcastPlayer(),
]


for player in players:
    start_player(player)


# ============================================================
# 16. OVERRIDING + POLYMORPHISM
# ============================================================

"""
Method overriding provides the different implementations.

Polymorphism allows the same code to work with those
different implementations.
"""

class Animal:
    """Represent a generic animal."""

    def speak(self) -> None:
        """Make a generic sound."""
        print("Animal sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> None:
        """Make a dog sound."""
        print("Woof!")


class Cat(Animal):
    """Represent a cat."""

    def speak(self) -> None:
        """Make a cat sound."""
        print("Meow!")


def make_sound(animal: Animal) -> None:
    """Make an animal sound."""
    animal.speak()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)


# ============================================================
# 17. POLYMORPHISM DOES NOT MEAN SAME OUTPUT
# ============================================================

"""
Polymorphism does not mean every object performs the exact
same action.

It means the same interface can produce different behaviour.

For example:

    Dog.speak()
        -> Woof!

    Cat.speak()
        -> Meow!

Both respond to:

    speak()

but their implementations are different.
"""


# ============================================================
# 18. POLYMORPHISM WITH COMMON DATA
# ============================================================

class Employee:
    """Represent an employee."""

    def __init__(self, name: str) -> None:
        self.name = name

    def calculate_bonus(self) -> float:
        """Calculate a generic bonus."""
        return 1000.0


class Developer(Employee):
    """Represent a developer."""

    def calculate_bonus(self) -> float:
        """Calculate developer bonus."""
        return 5000.0


class Manager(Employee):
    """Represent a manager."""

    def calculate_bonus(self) -> float:
        """Calculate manager bonus."""
        return 10000.0


def display_bonus(employee: Employee) -> None:
    """Display an employee's bonus."""
    print(f"{employee.name}: {employee.calculate_bonus()}")


developer = Developer("Alice")
manager = Manager("Bob")

display_bonus(developer)
display_bonus(manager)


# ============================================================
# 19. POLYMORPHISM WITH MULTIPLE LEVELS OF INHERITANCE
# ============================================================

class Animal:
    """Represent an animal."""

    def speak(self) -> None:
        """Make a generic sound."""
        print("Animal sound.")


class Mammal(Animal):
    """Represent a mammal."""

    pass


class Dog(Mammal):
    """Represent a dog."""

    def speak(self) -> None:
        """Make a dog sound."""
        print("Dog barks.")


class Cat(Mammal):
    """Represent a cat."""

    def speak(self) -> None:
        """Make a cat sound."""
        print("Cat meows.")


animals: list[Animal] = [
    Dog(),
    Cat(),
]


for animal in animals:
    animal.speak()


# ============================================================
# 20. POLYMORPHISM AND super()
# ============================================================

class Animal:
    """Represent an animal."""

    def describe(self) -> None:
        """Describe an animal."""
        print("This is an animal.")


class Dog(Animal):
    """Represent a dog."""

    def describe(self) -> None:
        """Extend the animal description."""
        super().describe()
        print("This is a dog.")


class Cat(Animal):
    """Represent a cat."""

    def describe(self) -> None:
        """Extend the animal description."""
        super().describe()
        print("This is a cat.")


def describe_animal(animal: Animal) -> None:
    """Describe an animal."""
    animal.describe()


describe_animal(Dog())
describe_animal(Cat())


# ============================================================
# 21. POLYMORPHISM VS CONDITIONAL TYPE CHECKING
# ============================================================

class Dog:
    """Represent a dog."""

    def speak(self) -> None:
        """Make the dog speak."""
        print("Woof!")


class Cat:
    """Represent a cat."""

    def speak(self) -> None:
        """Make the cat speak."""
        print("Meow!")


class Bird:
    """Represent a bird."""

    def speak(self) -> None:
        """Make the bird speak."""
        print("Chirp!")


"""
A less polymorphic approach might look like:

    if isinstance(animal, Dog):
        ...
    elif isinstance(animal, Cat):
        ...
    elif isinstance(animal, Bird):
        ...

Inheritance-based polymorphism instead allows each class
to define speak(), while the calling code simply does:

    animal.speak()
"""


# ============================================================
# 22. POLYMORPHISM ENABLES EXTENSIBILITY
# ============================================================

class Report:
    """Represent a generic report."""

    def generate(self) -> None:
        """Generate a report."""
        print("Generating report.")


class SalesReport(Report):
    """Represent a sales report."""

    def generate(self) -> None:
        """Generate a sales report."""
        print("Generating sales report.")


class InventoryReport(Report):
    """Represent an inventory report."""

    def generate(self) -> None:
        """Generate an inventory report."""
        print("Generating inventory report.")


def generate_report(report: Report) -> None:
    """Generate any supported report."""
    report.generate()


reports: list[Report] = [
    SalesReport(),
    InventoryReport(),
]


for report in reports:
    generate_report(report)


# ============================================================
# 23. ADDING ANOTHER CHILD CLASS
# ============================================================

class FinancialReport(Report):
    """Represent a financial report."""

    def generate(self) -> None:
        """Generate a financial report."""
        print("Generating financial report.")


generate_report(FinancialReport())


"""
Notice that generate_report() did not change.

The new child class automatically works because it follows
the Report interface.

This is one of the major practical benefits of polymorphism.
"""


# ============================================================
# 24. COMPLETE POLYMORPHIC FLOW
# ============================================================

class Animal:
    """Represent a generic animal."""

    def speak(self) -> None:
        """Define the common animal interface."""
        print("Animal sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> None:
        """Provide dog-specific behaviour."""
        print("Woof!")


class Cat(Animal):
    """Represent a cat."""

    def speak(self) -> None:
        """Provide cat-specific behaviour."""
        print("Meow!")


class Bird(Animal):
    """Represent a bird."""

    def speak(self) -> None:
        """Provide bird-specific behaviour."""
        print("Chirp!")


def announce(animal: Animal) -> None:
    """Use the common Animal interface."""
    animal.speak()


animals: list[Animal] = [
    Dog(),
    Cat(),
    Bird(),
]


for animal in animals:
    announce(animal)


"""
The complete flow is:

    Animal
       │
       ├── Dog
       │     └── speak() -> "Woof!"
       │
       ├── Cat
       │     └── speak() -> "Meow!"
       │
       └── Bird
             └── speak() -> "Chirp!"


The function:

    announce(animal)

accepts the parent type:

    Animal

but receives different child objects.

At runtime, Python dispatches:

    Dog  -> Dog.speak()
    Cat  -> Cat.speak()
    Bird -> Bird.speak()
"""


# ============================================================
# 25. KEY TAKEAWAY
# ============================================================

"""
Inheritance-based polymorphism combines three ideas:

    1. Inheritance

        Dog inherits from Animal.

    2. Method overriding

        Dog provides its own speak() implementation.

    3. Polymorphism

        Code written for Animal can work with Dog, Cat,
        Bird, and other Animal subclasses.


The general structure is:

    class Parent:
        def method(self):
            ...


    class ChildA(Parent):
        def method(self):
            ...


    class ChildB(Parent):
        def method(self):
            ...


    def use_object(obj: Parent):
        obj.method()


Then:

    use_object(ChildA())
    use_object(ChildB())


The function works with both objects even though they have
different concrete classes.

The central idea is:

    Parent interface
          ↓
    different child implementations
          ↓
    same calling code
          ↓
    different runtime behaviour


This is inheritance-based polymorphism.
"""