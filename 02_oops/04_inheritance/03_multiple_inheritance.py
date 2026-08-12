# type: ignore

"""
03_multiple_inheritance.py

Demonstrates multiple inheritance in Python.

Multiple inheritance occurs when a class directly inherits
from more than one parent class.

Structure:

    Parent A      Parent B
        \          /
         \        /
          Child

This file focuses on:

    - Basic multiple inheritance
    - Inheriting from multiple parent classes
    - Combining behaviour from multiple parents
    - Multiple inherited attributes
    - Method lookup
    - Method Resolution Order (basic introduction)
    - Attribute conflicts
    - Method conflicts
    - isinstance()
    - issubclass()
"""


# ============================================================
# 1. BASIC MULTIPLE INHERITANCE
# ============================================================

class Flyer:
    """Represent something that can fly."""

    def fly(self) -> None:
        print("Flying.")


class Swimmer:
    """Represent something that can swim."""

    def swim(self) -> None:
        print("Swimming.")


class Duck(Flyer, Swimmer):
    """Represent a duck."""

    pass


duck = Duck()

duck.fly()
duck.swim()

"""
Duck inherits directly from two classes:

    Flyer
       \
        Duck
       /
    Swimmer

Therefore Duck receives behaviour from both parents.
"""


# ============================================================
# 2. MULTIPLE PARENTS CAN PROVIDE DIFFERENT BEHAVIOUR
# ============================================================

class Printer:
    """Provide printing behaviour."""

    def print_document(self) -> None:
        print("Printing document.")


class Scanner:
    """Provide scanning behaviour."""

    def scan_document(self) -> None:
        print("Scanning document.")


class MultiFunctionPrinter(Printer, Scanner):
    """Provide printing and scanning behaviour."""

    pass


printer = MultiFunctionPrinter()

printer.print_document()
printer.scan_document()


# ============================================================
# 3. CHILD CAN ADD ITS OWN BEHAVIOUR
# ============================================================

class Flyer:
    """Provide flying behaviour."""

    def fly(self) -> None:
        print("Flying.")


class Swimmer:
    """Provide swimming behaviour."""

    def swim(self) -> None:
        print("Swimming.")


class Duck(Flyer, Swimmer):
    """Represent a duck."""

    def walk(self) -> None:
        print("Walking.")


duck = Duck()

duck.fly()
duck.swim()
duck.walk()

"""
Duck combines:

    Flyer behaviour
    Swimmer behaviour
    Duck-specific behaviour
"""


# ============================================================
# 4. MULTIPLE INHERITED CLASS ATTRIBUTES
# ============================================================

class Animal:
    """Provide a general category."""

    kingdom = "Animalia"


class Bird:
    """Provide a movement category."""

    movement = "Flight"


class Eagle(Animal, Bird):
    """Represent an eagle."""

    species = "Eagle"


eagle = Eagle()

print(eagle.kingdom)
print(eagle.movement)
print(eagle.species)

"""
Eagle receives attributes from both parent classes.
"""


# ============================================================
# 5. MULTIPLE INHERITANCE WITH INSTANCE METHODS
# ============================================================

class Logger:
    """Provide logging behaviour."""

    def log(self, message: str) -> None:
        print(f"LOG: {message}")


class Validator:
    """Provide validation behaviour."""

    def validate(self, value: int) -> bool:
        return value >= 0


class DataProcessor(Logger, Validator):
    """Combine logging and validation behaviour."""

    def process(self, value: int) -> None:
        if self.validate(value):
            self.log(f"Processing {value}.")


processor = DataProcessor()

processor.process(10)
processor.process(-5)

"""
DataProcessor inherits:

    log()       → Logger
    validate()  → Validator

and defines:

    process()   → DataProcessor
"""


# ============================================================
# 6. CHECKING MULTIPLE INHERITANCE WITH issubclass()
# ============================================================

class Flyer:
    """Represent something that can fly."""

    pass


class Swimmer:
    """Represent something that can swim."""

    pass


class Duck(Flyer, Swimmer):
    """Represent a duck."""

    pass


print(issubclass(Duck, Flyer))
print(issubclass(Duck, Swimmer))
print(issubclass(Duck, object))


# ============================================================
# 7. CHECKING MULTIPLE INHERITANCE WITH isinstance()
# ============================================================

class Flyer:
    """Represent something that can fly."""

    pass


class Swimmer:
    """Represent something that can swim."""

    pass


class Duck(Flyer, Swimmer):
    """Represent a duck."""

    pass


duck = Duck()

print(isinstance(duck, Duck))
print(isinstance(duck, Flyer))
print(isinstance(duck, Swimmer))
print(isinstance(duck, object))

"""
A Duck instance is considered an instance of:

    Duck
    Flyer
    Swimmer
    object
"""


# ============================================================
# 8. METHOD NAME CONFLICT
# ============================================================

class ParentA:
    """First parent."""

    def show(self) -> None:
        print("Parent A")


class ParentB:
    """Second parent."""

    def show(self) -> None:
        print("Parent B")


class Child(ParentA, ParentB):
    """Inherit from both parents."""

    pass


child = Child()

child.show()

"""
Both parents define show().

Child does not define show().

Python must determine which implementation to use.

Because ParentA appears first:

    class Child(ParentA, ParentB)

ParentA.show() is selected.

The mechanism responsible for this lookup is the
Method Resolution Order (MRO).
"""


# ============================================================
# 9. REVERSING THE PARENT ORDER
# ============================================================

class ParentA:
    """First parent."""

    def show(self) -> None:
        print("Parent A")


class ParentB:
    """Second parent."""

    def show(self) -> None:
        print("Parent B")


class Child(ParentB, ParentA):
    """Inherit from both parents."""

    pass


child = Child()

child.show()

"""
Changing the parent order changes the lookup order.

Here:

    ParentB

appears before:

    ParentA

Therefore ParentB.show() is selected.
"""


# ============================================================
# 10. VIEWING THE MRO
# ============================================================

class ParentA:
    """First parent."""

    pass


class ParentB:
    """Second parent."""

    pass


class Child(ParentA, ParentB):
    """Inherit from two parents."""

    pass


print(Child.__mro__)

"""
The MRO shows the order Python follows when looking up
attributes and methods.

Conceptually:

    Child
      ↓
    ParentA
      ↓
    ParentB
      ↓
    object
"""


# ============================================================
# 11. __bases__ VS __mro__
# ============================================================

class ParentA:
    """First parent."""

    pass


class ParentB:
    """Second parent."""

    pass


class Child(ParentA, ParentB):
    """Inherit from two parents."""

    pass


print(Child.__bases__)
print(Child.__mro__)

"""
__bases__:

    Shows direct parent classes.

__mro__:

    Shows the complete method resolution order.

For Child:

    __bases__
        → ParentA, ParentB

    __mro__
        → Child, ParentA, ParentB, object
"""


# ============================================================
# 12. CHILD CAN OVERRIDE A CONFLICTING METHOD
# ============================================================

class ParentA:
    """First parent."""

    def show(self) -> None:
        print("Parent A")


class ParentB:
    """Second parent."""

    def show(self) -> None:
        print("Parent B")


class Child(ParentA, ParentB):
    """Override the conflicting method."""

    def show(self) -> None:
        print("Child")


child = Child()

child.show()

"""
The child implementation takes precedence over both parents.
"""


# ============================================================
# 13. ACCESSING A SPECIFIC PARENT IMPLEMENTATION
# ============================================================

class ParentA:
    """First parent."""

    def show(self) -> None:
        print("Parent A")


class ParentB:
    """Second parent."""

    def show(self) -> None:
        print("Parent B")


class Child(ParentA, ParentB):
    """Inherit from both parents."""

    def show_both(self) -> None:
        ParentA.show(self)
        ParentB.show(self)


child = Child()

child.show_both()

"""
A specific parent implementation can be called explicitly
using the parent class name.

This bypasses normal method lookup for that call.
"""


# ============================================================
# 14. MULTIPLE INHERITANCE WITH INSTANCE STATE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


class Employee:
    """Represent an employee."""

    def set_employee_id(self, employee_id: int) -> None:
        self.employee_id = employee_id


class Developer(Person, Employee):
    """Represent a developer."""

    def introduce(self) -> None:
        print(f"{self.name} is a developer.")


developer = Developer("Alice")

developer.set_employee_id(101)
developer.introduce()

print(developer.name)
print(developer.employee_id)

"""
Developer inherits behaviour from both:

    Person
    Employee

However, initialization becomes more important when multiple
parents define their own __init__() methods.

Cooperative initialization with super() is covered later.
"""


# ============================================================
# 15. PARENT ORDER IS PART OF THE CLASS DEFINITION
# ============================================================

class A:
    """Parent A."""

    def identify(self) -> None:
        print("A")


class B:
    """Parent B."""

    def identify(self) -> None:
        print("B")


class C(A, B):
    """First inheritance order."""

    pass


class D(B, A):
    """Reversed inheritance order."""

    pass


C().identify()
D().identify()

"""
C and D contain the same two parent classes but in different
orders.

The order affects method lookup.
"""


# ============================================================
# 16. MULTIPLE INHERITANCE WITH THREE PARENTS
# ============================================================

class Reader:
    """Provide reading behaviour."""

    def read(self) -> None:
        print("Reading.")


class Writer:
    """Provide writing behaviour."""

    def write(self) -> None:
        print("Writing.")


class Editor:
    """Provide editing behaviour."""

    def edit(self) -> None:
        print("Editing.")


class DocumentManager(Reader, Writer, Editor):
    """Combine document management behaviour."""

    pass


manager = DocumentManager()

manager.read()
manager.write()
manager.edit()

"""
Python allows a class to have more than two direct parents.

The same MRO rules determine the lookup order.
"""


# ============================================================
# 17. MULTIPLE INHERITANCE REPRESENTS MULTIPLE CAPABILITIES
# ============================================================

class Serializable:
    """Provide serialization behaviour."""

    def serialize(self) -> str:
        return "serialized data"


class Compressible:
    """Provide compression behaviour."""

    def compress(self) -> str:
        return "compressed data"


class Cacheable:
    """Provide caching behaviour."""

    def cache(self) -> str:
        return "cached data"


class DataObject(Serializable, Compressible, Cacheable):
    """Combine several capabilities."""

    pass


data = DataObject()

print(data.serialize())
print(data.compress())
print(data.cache())

"""
This is a common conceptual use of multiple inheritance:

    DataObject
       ├── Serializable
       ├── Compressible
       └── Cacheable
"""


# ============================================================
# 18. MRO IS USED FOR ATTRIBUTE LOOKUP TOO
# ============================================================

class A:
    """Parent A."""

    value = "A"


class B:
    """Parent B."""

    value = "B"


class C(A, B):
    """Child."""

    pass


print(C.value)

"""
Both A and B define value.

MRO determines which value is found first.

Because A comes before B:

    C.value → A.value
"""


# ============================================================
# 19. INSTANCE ATTRIBUTE STILL TAKES PRECEDENCE
# ============================================================

class A:
    """Parent A."""

    value = "A"


class B:
    """Parent B."""

    value = "B"


class C(A, B):
    """Child."""

    pass


obj = C()

obj.value = "Instance"

print(obj.value)
print(C.value)

"""
The instance attribute:

    obj.value

takes precedence over class-level lookup.

The class still resolves:

    C.value → A.value
"""


# ============================================================
# 20. MULTIPLE INHERITANCE AND OBJECT
# ============================================================

class A:
    """Parent A."""

    pass


class B:
    """Parent B."""

    pass


class C(A, B):
    """Child."""

    pass


print(issubclass(C, A))
print(issubclass(C, B))
print(issubclass(C, object))

"""
Even with multiple parents, the class ultimately inherits
from object.
"""


# ============================================================
# 21. DIAMOND-SHAPED INHERITANCE PREVIEW
# ============================================================

class A:
    """Top-level base class."""

    def show(self) -> None:
        print("A")


class B(A):
    """First branch."""

    pass


class C(A):
    """Second branch."""

    pass


class D(B, C):
    """Join the two branches."""

    pass


d = D()

d.show()

print(D.__mro__)

"""
The inheritance graph is:

        A
       / \
      B   C
       \ /
        D

This is called the Diamond Inheritance pattern.

Python's MRO handles this situation.

The detailed mechanics of MRO are covered in:

    07_method_resolution_order.py
"""


# ============================================================
# 22. MULTIPLE INHERITANCE DOES NOT MEAN RANDOM METHOD
#     SELECTION
# ============================================================

class A:
    """Parent A."""

    def action(self) -> None:
        print("A action")


class B:
    """Parent B."""

    def action(self) -> None:
        print("B action")


class C(A, B):
    """Child."""

    pass


c = C()

c.action()

"""
Python does not randomly choose between A.action() and
B.action().

It follows a deterministic Method Resolution Order.

The MRO for C begins with:

    C → A → B → object
"""


# ============================================================
# 23. MULTIPLE INHERITANCE WITH SPECIALIZED BEHAVIOUR
# ============================================================

class DatabaseReader:
    """Provide database reading behaviour."""

    def read_data(self) -> None:
        print("Reading data from database.")


class DataValidator:
    """Provide validation behaviour."""

    def validate_data(self) -> None:
        print("Validating data.")


class ETLPipeline(DatabaseReader, DataValidator):
    """Combine database reading and validation."""

    def run(self) -> None:
        self.read_data()
        self.validate_data()
        print("Pipeline completed.")


pipeline = ETLPipeline()

pipeline.run()

"""
ETLPipeline combines capabilities from two independent
parent classes.
"""


# ============================================================
# 24. KEY TAKEAWAY
# ============================================================

"""
Multiple inheritance means:

    One child
       ↓
    inherits directly from
       ↓
    two or more parent classes


Basic syntax:

    class Child(ParentA, ParentB):
        ...


Example:

    class Flyer:
        def fly(self):
            ...


    class Swimmer:
        def swim(self):
            ...


    class Duck(Flyer, Swimmer):
        pass


    duck = Duck()

    duck.fly()
    duck.swim()


The important difference is:

    Single inheritance:

        Parent
           ↑
         Child


    Multilevel inheritance:

        Grandparent
             ↑
           Parent
             ↑
           Child


    Multiple inheritance:

        Parent A      Parent B
             \          /
              \        /
               Child


When multiple parents provide the same attribute or method,
Python uses the Method Resolution Order (MRO) to determine
which implementation is found first.

The next files explore other inheritance structures and
then examine MRO and super() in greater detail.
"""