# type: ignore

"""
03_polymorphic_functions.py

Demonstrates polymorphic functions in Python.

A polymorphic function is a function that can operate on
objects of different types through a common interface or
behaviour.

The function does not need to know the exact concrete type
of the object.

It only needs the object to support the operation required
by the function.
"""


# ============================================================
# 1. BASIC POLYMORPHIC FUNCTION
# ============================================================

class Dog:
    """Represent a dog."""

    def speak(self) -> None:
        """Make the dog speak."""
        print("Dog barks.")


class Cat:
    """Represent a cat."""

    def speak(self) -> None:
        """Make the cat speak."""
        print("Cat meows.")


def make_sound(animal: Dog | Cat) -> None:
    """Make an animal produce its sound."""
    animal.speak()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)


# ============================================================
# 2. SAME FUNCTION, DIFFERENT OBJECTS
# ============================================================

class Circle:
    """Represent a circle."""

    def draw(self) -> None:
        """Draw a circle."""
        print("Drawing a circle.")


class Square:
    """Represent a square."""

    def draw(self) -> None:
        """Draw a square."""
        print("Drawing a square.")


def draw_shape(shape: Circle | Square) -> None:
    """Draw the supplied shape."""
    shape.draw()


draw_shape(Circle())
draw_shape(Square())


# ============================================================
# 3. POLYMORPHIC FUNCTION DOES NOT NEED TYPE BRANCHING
# ============================================================

"""
A polymorphic function can simply call the common operation.

It does not need:

    if isinstance(...)
    elif isinstance(...)

The object's implementation determines the behaviour.
"""

class Email:
    """Represent an email."""

    def send(self) -> None:
        """Send an email."""
        print("Sending email.")


class SMS:
    """Represent an SMS."""

    def send(self) -> None:
        """Send an SMS."""
        print("Sending SMS.")


def send_notification(notification: Email | SMS) -> None:
    """Send a notification."""
    notification.send()


send_notification(Email())
send_notification(SMS())


# ============================================================
# 4. POLYMORPHIC FUNCTION WITH INHERITANCE
# ============================================================

class Animal:
    """Represent a generic animal."""

    def speak(self) -> None:
        """Make a generic animal sound."""
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


def make_animal_speak(animal: Animal) -> None:
    """Make an animal speak."""
    animal.speak()


make_animal_speak(Dog())
make_animal_speak(Cat())


# ============================================================
# 5. FUNCTION USES THE PARENT TYPE
# ============================================================

"""
The function accepts Animal.

Dog and Cat are both subclasses of Animal.

Therefore, both can be passed to the function.
"""

dog = Dog()
cat = Cat()

make_animal_speak(dog)
make_animal_speak(cat)


# ============================================================
# 6. POLYMORPHIC FUNCTION WITH MULTIPLE METHODS
# ============================================================

class File:
    """Represent a file."""

    def open(self) -> None:
        """Open the file."""
        print("File opened.")

    def close(self) -> None:
        """Close the file."""
        print("File closed.")


class DatabaseConnection:
    """Represent a database connection."""

    def open(self) -> None:
        """Open the database connection."""
        print("Database opened.")

    def close(self) -> None:
        """Close the database connection."""
        print("Database closed.")


def use_resource(
    resource: File | DatabaseConnection,
) -> None:
    """Open, use, and close a resource."""
    resource.open()
    print("Resource is being used.")
    resource.close()


use_resource(File())
use_resource(DatabaseConnection())


# ============================================================
# 7. POLYMORPHIC FUNCTION WITH DIFFERENT CALCULATIONS
# ============================================================

class Circle:
    """Represent a circle."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle."""
        return 3.14159 * self.radius**2


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.length * self.width


def display_area(shape: Circle | Rectangle) -> None:
    """Display the area of a shape."""
    print(f"Area: {shape.area()}")


display_area(Circle(5))
display_area(Rectangle(10, 5))


# ============================================================
# 8. POLYMORPHIC FUNCTION WITH DIFFERENT IMPLEMENTATIONS
# ============================================================

class CreditCardPayment:
    """Represent a credit card payment."""

    def process(self, amount: float) -> None:
        """Process a credit card payment."""
        print(f"Credit card payment: {amount}")


class UPIPayment:
    """Represent a UPI payment."""

    def process(self, amount: float) -> None:
        """Process a UPI payment."""
        print(f"UPI payment: {amount}")


class CashPayment:
    """Represent a cash payment."""

    def process(self, amount: float) -> None:
        """Process a cash payment."""
        print(f"Cash payment: {amount}")


def process_payment(
    payment: CreditCardPayment | UPIPayment | CashPayment,
    amount: float,
) -> None:
    """Process a payment using the supplied payment method."""
    payment.process(amount)


process_payment(CreditCardPayment(), 1000)
process_payment(UPIPayment(), 1000)
process_payment(CashPayment(), 1000)


# ============================================================
# 9. POLYMORPHIC FUNCTION WITH COLLECTIONS
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


animals: list[Dog | Cat] = [
    Dog(),
    Cat(),
    Dog(),
    Cat(),
]


def make_all_speak(animals: list[Dog | Cat]) -> None:
    """Make every animal in the collection speak."""
    for animal in animals:
        animal.speak()


make_all_speak(animals)


# ============================================================
# 10. POLYMORPHIC FUNCTION WITH INHERITANCE
# ============================================================

class Employee:
    """Represent an employee."""

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


def display_salary(employee: Employee) -> None:
    """Display an employee's salary."""
    print(f"Salary: {employee.calculate_salary()}")


display_salary(Developer())
display_salary(Manager())


# ============================================================
# 11. POLYMORPHIC FUNCTION WITH OVERRIDING
# ============================================================

"""
The function knows only that it received an Employee.

The actual method implementation is selected according to
the object's runtime type.
"""

employees: list[Employee] = [
    Developer(),
    Manager(),
    Employee(),
]


for employee in employees:
    display_salary(employee)


# ============================================================
# 12. POLYMORPHIC FUNCTION AND METHOD DISPATCH
# ============================================================

class Animal:
    """Represent an animal."""

    def sound(self) -> None:
        """Make a generic sound."""
        print("Animal sound.")


class Dog(Animal):
    """Represent a dog."""

    def sound(self) -> None:
        """Make a dog sound."""
        print("Dog bark.")


class Cat(Animal):
    """Represent a cat."""

    def sound(self) -> None:
        """Make a cat sound."""
        print("Cat meow.")


def play_sound(animal: Animal) -> None:
    """Play the sound produced by an animal."""
    animal.sound()


animals: list[Animal] = [
    Dog(),
    Cat(),
    Animal(),
]


for animal in animals:
    play_sound(animal)


# ============================================================
# 13. FUNCTION DOES NOT NEED TO KNOW THE CONCRETE CLASS
# ============================================================

class PDFReport:
    """Represent a PDF report."""

    def generate(self) -> None:
        """Generate a PDF report."""
        print("Generating PDF report.")


class ExcelReport:
    """Represent an Excel report."""

    def generate(self) -> None:
        """Generate an Excel report."""
        print("Generating Excel report.")


def generate_report(
    report: PDFReport | ExcelReport,
) -> None:
    """Generate the supplied report."""
    report.generate()


generate_report(PDFReport())
generate_report(ExcelReport())


# ============================================================
# 14. POLYMORPHIC FUNCTION VS TYPE CHECKING
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


def polymorphic_sound(animal: Dog | Cat) -> None:
    """Use polymorphic behaviour."""
    animal.speak()


def type_checked_sound(animal: Dog | Cat) -> None:
    """Use explicit type checking."""
    if isinstance(animal, Dog):
        animal.speak()
    elif isinstance(animal, Cat):
        animal.speak()


polymorphic_sound(Dog())
polymorphic_sound(Cat())

type_checked_sound(Dog())
type_checked_sound(Cat())


"""
The polymorphic version is simpler:

    animal.speak()

The function does not need to know which concrete class
provided the object.
"""


# ============================================================
# 15. POLYMORPHIC FUNCTIONS AND DUCK TYPING
# ============================================================

class Printer:
    """Represent a printer."""

    def print_document(self, document: str) -> None:
        """Print a document."""
        print(f"Printer: {document}")


class PDFPrinter:
    """Represent a PDF printer."""

    def print_document(self, document: str) -> None:
        """Print a PDF document."""
        print(f"PDF printer: {document}")


def print_document(
    printer: Printer | PDFPrinter,
    document: str,
) -> None:
    """Print a document using the supplied printer."""
    printer.print_document(document)


print_document(Printer(), "Report")
print_document(PDFPrinter(), "Report")


# ============================================================
# 16. POLYMORPHIC FUNCTION CAN RETURN DIFFERENT RESULTS
# ============================================================

class Circle:
    """Represent a circle."""

    def calculate(self) -> float:
        """Return a calculation."""
        return 78.54


class Rectangle:
    """Represent a rectangle."""

    def calculate(self) -> float:
        """Return a calculation."""
        return 50.0


def calculate(shape: Circle | Rectangle) -> float:
    """Perform the object's calculation."""
    return shape.calculate()


circle_result = calculate(Circle())
rectangle_result = calculate(Rectangle())

print(circle_result)
print(rectangle_result)


# ============================================================
# 17. POLYMORPHIC FUNCTIONS REDUCE CONDITIONAL LOGIC
# ============================================================

"""
Without polymorphism, code might become:

    if type == "dog":
        ...
    elif type == "cat":
        ...
    elif type == "bird":
        ...

With polymorphism:

    animal.speak()

Each class owns its own implementation.

This keeps the function focused on what it needs to do.
"""


# ============================================================
# 18. POLYMORPHIC FUNCTIONS SUPPORT EXTENSIBILITY
# ============================================================

class Animal:
    """Represent an animal."""

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


def announce(animal: Animal) -> None:
    """Announce an animal's sound."""
    animal.speak()


class Bird(Animal):
    """Represent a bird."""

    def speak(self) -> None:
        """Make a bird sound."""
        print("Chirp!")


announce(Dog())
announce(Cat())
announce(Bird())


"""
The announce() function did not need to be modified when
Bird was introduced.

Bird simply followed the same interface:

    speak()

This is one of the practical benefits of polymorphism.
"""


# ============================================================
# 19. POLYMORPHIC FUNCTION WITH A COMMON BASE CLASS
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
        """Return the circle area."""
        return 3.14159 * self.radius**2


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        """Return the rectangle area."""
        return self.length * self.width


def total_area(shapes: list[Shape]) -> float:
    """Return the combined area of all shapes."""
    total = 0.0

    for shape in shapes:
        total += shape.area()

    return total


shapes: list[Shape] = [
    Circle(5),
    Rectangle(10, 5),
]

print(total_area(shapes))


# ============================================================
# 20. POLYMORPHIC FUNCTION: CORE IDEA
# ============================================================

"""
A polymorphic function separates:

    WHAT the function needs

from:

    HOW each object performs that operation.

For example:

    def make_sound(animal):
        animal.speak()


The function only requires:

    speak()

Dog decides HOW:
    "Woof!"

Cat decides HOW:
    "Meow!"

Bird decides HOW:
    "Chirp!"

The function remains unchanged.
"""


# ============================================================
# 21. KEY TAKEAWAY
# ============================================================

"""
A polymorphic function is designed to work with multiple
object types through a shared interface or behaviour.

The function:

    - does not need to know the exact concrete class
    - calls a common method or operation
    - allows each object to provide its own implementation
    - can work with inheritance-based polymorphism
    - can also work with duck typing

Example:

    def make_sound(animal):
        animal.speak()


Different objects:

    Dog()
    Cat()
    Bird()

can all work with the same function if they provide:

    speak()


The important separation is:

    Polymorphic function
            ↓
       calls common operation
            ↓
       object decides behaviour


This allows code to be:

    - simpler
    - more flexible
    - easier to extend
    - less dependent on concrete classes
    - less dependent on conditional type checks

The core idea:

    One function
        +
    Different compatible objects
        =
    Polymorphic behaviour
"""