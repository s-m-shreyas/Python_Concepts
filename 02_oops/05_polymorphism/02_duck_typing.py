# type: ignore

"""
02_duck_typing.py

Demonstrates duck typing in Python.

Duck typing is a form of polymorphism where the type or class
of an object is less important than the operations that the
object supports.

The idea is commonly summarized as:

    "If it walks like a duck and quacks like a duck,
     it is treated like a duck."

Python therefore focuses on an object's behaviour rather than
requiring a specific inheritance relationship.
"""


# ============================================================
# 1. BASIC DUCK TYPING
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


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# ============================================================
# 2. SAME METHOD, UNRELATED CLASSES
# ============================================================

"""
Dog and Cat do not inherit from a common Animal class.

They are completely unrelated classes.

However, both provide:

    speak()

That shared behaviour is enough for code that only needs
something capable of speaking.
"""

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


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# ============================================================
# 3. DUCK TYPING WITH A FUNCTION
# ============================================================

"""
The function does not care whether the object is a Dog,
Cat, or something else.

It only requires the object to provide speak().
"""

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


def make_it_speak(animal: Dog | Cat) -> None:
    """Call speak() on an object."""
    animal.speak()


dog = Dog()
cat = Cat()

make_it_speak(dog)
make_it_speak(cat)


# ============================================================
# 4. DUCK TYPING DOES NOT REQUIRE INHERITANCE
# ============================================================

class Bird:
    """Represent a bird."""

    def speak(self) -> None:
        """Make the bird speak."""
        print("Chirp!")


class Robot:
    """Represent a robot."""

    def speak(self) -> None:
        """Make the robot speak."""
        print("Robot speaking.")


def speak_object(obj: Bird | Robot) -> None:
    """Call speak() regardless of the object's class."""
    obj.speak()


bird = Bird()
robot = Robot()

speak_object(bird)
speak_object(robot)


# ============================================================
# 5. BEHAVIOUR MATTERS, NOT CLASS IDENTITY
# ============================================================

class Person:
    """Represent a person."""

    def speak(self) -> None:
        """Make the person speak."""
        print("Person speaks.")


class Computer:
    """Represent a computer."""

    def speak(self) -> None:
        """Make the computer speak."""
        print("Computer speaks.")


def communicate(obj: Person | Computer) -> None:
    """Communicate with an object that can speak."""
    obj.speak()


person = Person()
computer = Computer()

communicate(person)
communicate(computer)


# ============================================================
# 6. THREE UNRELATED CLASSES
# ============================================================

class Dog:
    """Represent a dog."""

    def move(self) -> None:
        """Move the dog."""
        print("Dog runs.")


class Fish:
    """Represent a fish."""

    def move(self) -> None:
        """Move the fish."""
        print("Fish swims.")


class Bird:
    """Represent a bird."""

    def move(self) -> None:
        """Move the bird."""
        print("Bird flies.")


def move_object(obj: Dog | Fish | Bird) -> None:
    """Move an object."""
    obj.move()


dog = Dog()
fish = Fish()
bird = Bird()

move_object(dog)
move_object(fish)
move_object(bird)


# ============================================================
# 7. DUCK TYPING WITH DIFFERENT IMPLEMENTATIONS
# ============================================================

class EmailSender:
    """Represent an email sender."""

    def send(self, message: str) -> None:
        """Send an email."""
        print(f"Email sent: {message}")


class SMSSender:
    """Represent an SMS sender."""

    def send(self, message: str) -> None:
        """Send an SMS."""
        print(f"SMS sent: {message}")


class NotificationSender:
    """Represent a notification sender."""

    def send(self, message: str) -> None:
        """Send a notification."""
        print(f"Notification sent: {message}")


def send_message(
    sender: EmailSender | SMSSender | NotificationSender,
    message: str,
) -> None:
    """Send a message using the supplied sender."""
    sender.send(message)


send_message(EmailSender(), "Hello")
send_message(SMSSender(), "Hello")
send_message(NotificationSender(), "Hello")


# ============================================================
# 8. THE FUNCTION DOES NOT CHECK THE CLASS
# ============================================================

class Printer:
    """Represent a printer."""

    def print_document(self, document: str) -> None:
        """Print a document."""
        print(f"Printing: {document}")


class PDFPrinter:
    """Represent a PDF printer."""

    def print_document(self, document: str) -> None:
        """Print a PDF document."""
        print(f"Printing PDF: {document}")


def print_document(
    printer: Printer | PDFPrinter,
    document: str,
) -> None:
    """Print a document using the supplied printer."""
    printer.print_document(document)


print_document(Printer(), "Report")
print_document(PDFPrinter(), "Report")


# ============================================================
# 9. DUCK TYPING BASED ON MULTIPLE METHODS
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
        print("Database connection opened.")

    def close(self) -> None:
        """Close the database connection."""
        print("Database connection closed.")


def use_resource(
    resource: File | DatabaseConnection,
) -> None:
    """Use any resource providing open() and close()."""
    resource.open()
    print("Using resource.")
    resource.close()


use_resource(File())
use_resource(DatabaseConnection())


# ============================================================
# 10. DUCK TYPING WITH A THIRD-PARTY-STYLE OBJECT
# ============================================================

"""
The important idea is that the function only cares about the
required behaviour.

The class does not need to inherit from anything specific.
"""

class CustomLogger:
    """Represent a custom logger."""

    def write(self, message: str) -> None:
        """Write a log message."""
        print(f"LOG: {message}")


def log_message(logger: CustomLogger, message: str) -> None:
    """Write a message using a logger."""
    logger.write(message)


logger = CustomLogger()

log_message(logger, "Application started.")


# ============================================================
# 11. DUCK TYPING AND BUILT-IN TYPES
# ============================================================

"""
Python's built-in functions frequently work according to
behaviour rather than requiring a specific class.

For example, len() works with objects that provide the
required length behaviour.
"""

numbers = [10, 20, 30]
text = "Python"

print(len(numbers))
print(len(text))


# ============================================================
# 12. DIFFERENT OBJECTS CAN SUPPORT THE SAME OPERATION
# ============================================================

"""
These objects have different types, but both support the
addition operation.
"""

first_number = 10
second_number = 20

first_text = "Hello "
second_text = "Python"

print(first_number + second_number)
print(first_text + second_text)


# ============================================================
# 13. DUCK TYPING WITH A CUSTOM OBJECT
# ============================================================

class Score:
    """Represent a score."""

    def __init__(self, value: int) -> None:
        self.value = value

    def __int__(self) -> int:
        """Return the score as an integer."""
        return self.value


score = Score(95)

print(int(score))


# ============================================================
# 14. WHAT DUCK TYPING DOES NOT REQUIRE
# ============================================================

"""
Duck typing does NOT require:

    - a common parent class
    - inheritance
    - the same concrete class
    - explicit type checking

It primarily requires that the object support the operations
the code attempts to perform.
"""


# ============================================================
# 15. DUCK TYPING VS INHERITANCE
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


class Robot:
    """Represent a robot."""

    def speak(self) -> None:
        """Make the robot speak."""
        print("Beep!")


def make_sound(obj: Dog | Robot) -> None:
    """Call speak() on any compatible object."""
    obj.speak()


dog = Dog()
robot = Robot()

make_sound(dog)
make_sound(robot)

"""
Dog uses inheritance:

    Dog → Animal

Robot does not:

    Robot → no Animal

Yet both can be passed to make_sound() because both provide
the required speak() behaviour.

That is the key idea behind duck typing.
"""


# ============================================================
# 16. EXPLICIT TYPE CHECKING IS NOT DUCK TYPING
# ============================================================

class Dog:
    """Represent a dog."""

    def speak(self) -> None:
        """Make the dog speak."""
        print("Woof!")


def check_type(obj: object) -> None:
    """Demonstrate explicit type checking."""
    if isinstance(obj, Dog):
        obj.speak()


dog = Dog()

check_type(dog)

"""
This approach checks the object's type explicitly.

Duck typing generally focuses on:

    "Can this object perform the required operation?"

rather than:

    "Is this object an instance of this particular class?"
"""


# ============================================================
# 17. DUCK TYPING AND EAFP
# ============================================================

"""
Duck typing is closely related to Python's EAFP style:

    Easier to Ask Forgiveness than Permission.

Instead of checking whether an object supports an operation,
code can attempt the operation and handle failure when
appropriate.

Example:
"""

class Document:
    """Represent a document."""

    def read(self) -> str:
        """Read the document."""
        return "Document contents."


def read_document(document: Document) -> None:
    """Read an object that provides read()."""
    print(document.read())


document = Document()

read_document(document)


# ============================================================
# 18. A SIMPLE DUCK-TYPING MENTAL MODEL
# ============================================================

"""
Suppose a function needs:

    obj.speak()

The function does not necessarily care whether obj is:

    Dog
    Cat
    Robot
    Person

It only cares that:

    obj.speak()

works.

Therefore:

    Type
      ↓
    less important

    Behaviour
      ↓
    more important


This is the core idea of duck typing.
"""


# ============================================================
# 19. KEY TAKEAWAY
# ============================================================

"""
Duck typing is a Python approach to polymorphism where
objects are used according to the behaviour they provide
rather than their explicit class relationship.

Key points:

    - Inheritance is not required.
    - A common parent class is not required.
    - The same method or operation can be provided by
      unrelated classes.
    - Code focuses on what an object can do.
    - This supports flexible and polymorphic code.
    - It is closely related to Python's dynamic nature and
      EAFP programming style.

Example:

    class Dog:
        def speak(self):
            print("Woof!")


    class Cat:
        def speak(self):
            print("Meow!")


    def make_sound(obj):
        obj.speak()


Both Dog and Cat can work with make_sound() because both
provide the required speak() behaviour.

The central idea is:

    "Don't ask what type the object is.
     Ask what the object can do."

More precisely in Python:

    If the required operation works, the object's concrete
    inheritance relationship may not matter.
"""

