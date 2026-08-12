# type: ignore

"""
01_single_inheritance.py

Demonstrates single inheritance in Python.

Single inheritance means a child class inherits from exactly
one parent class.

Structure:

    Parent
      ↑
    Child

The child class automatically receives accessible attributes
and methods defined by the parent class.

This file focuses on:

    - Parent and child classes
    - Inheriting from one parent class
    - Creating child objects
    - Accessing inherited methods
    - Adding child-specific methods
    - Checking the inheritance relationship
"""


# ============================================================
# 1. BASIC SINGLE INHERITANCE
# ============================================================

class Animal:
    """Represent a generic animal."""

    def speak(self) -> None:
        print("Animal makes a sound.")


class Dog(Animal):
    """Represent a dog."""

    def bark(self) -> None:
        print("Dog barks.")


dog = Dog()

dog.speak()
dog.bark()

"""
Dog inherits from Animal.

Therefore Dog objects can access:

    speak()

from Animal.

Dog also defines its own:

    bark()
"""


# ============================================================
# 2. PARENT CLASS AND CHILD CLASS
# ============================================================

class Vehicle:
    """Represent a generic vehicle."""

    def start(self) -> None:
        print("Vehicle started.")


class Car(Vehicle):
    """Represent a car."""

    def drive(self) -> None:
        print("Car is driving.")


car = Car()

car.start()
car.drive()

"""
Inheritance relationship:

    Vehicle
       ↑
      Car

Car inherits start() from Vehicle.
Car defines drive() itself.
"""


# ============================================================
# 3. INHERITED METHODS ARE AVAILABLE TO CHILD OBJECTS
# ============================================================

class Person:
    """Represent a person."""

    def introduce(self) -> None:
        print("I am a person.")


class Student(Person):
    """Represent a student."""

    pass


student = Student()

student.introduce()

"""
Student does not define introduce().

Python looks for the method in Student and then finds it
in the parent class Person.
"""


# ============================================================
# 4. CHILD CLASS CAN ADD ITS OWN BEHAVIOUR
# ============================================================

class Employee:
    """Represent an employee."""

    def work(self) -> None:
        print("Employee is working.")


class Developer(Employee):
    """Represent a developer."""

    def write_code(self) -> None:
        print("Developer is writing code.")


developer = Developer()

developer.work()
developer.write_code()

"""
Developer receives:

    work()

from Employee and adds:

    write_code()

of its own.
"""


# ============================================================
# 5. CHILD CLASS CAN HAVE ITS OWN ATTRIBUTES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Unknown"


class Student(Person):
    """Represent a student."""

    def __init__(self) -> None:
        self.name = "Alice"
        self.grade = 90


student = Student()

print(student.name)
print(student.grade)

"""
Student inherits from Person but defines its own
initialization here.

The inheritance relationship still exists even though
Student provides its own __init__().
"""


# ============================================================
# 6. INHERITANCE DOES NOT COPY THE PARENT CLASS
# ============================================================

class Animal:
    """Represent an animal."""

    def speak(self) -> None:
        print("Animal sound.")


class Dog(Animal):
    """Represent a dog."""

    pass


dog = Dog()

print(type(dog).__name__)
print(type(dog).__bases__[0].__name__)

"""
Dog is a separate class.

Inheritance establishes a relationship:

    Dog → Animal

It does not create a duplicate copy of Animal.
"""


# ============================================================
# 7. CHECKING THE INHERITANCE RELATIONSHIP
# ============================================================

class Person:
    """Represent a person."""

    pass


class Employee(Person):
    """Represent an employee."""

    pass


employee = Employee()

print(isinstance(employee, Employee))
print(isinstance(employee, Person))

print(issubclass(Employee, Person))
print(issubclass(Employee, object))

"""
An Employee object is also considered a Person object because
Employee inherits from Person.

All Python classes ultimately inherit from object.
"""


# ============================================================
# 8. INHERITED CLASS ATTRIBUTES
# ============================================================

class Animal:
    """Represent an animal."""

    species = "Animal"


class Dog(Animal):
    """Represent a dog."""

    pass


dog = Dog()

print(dog.species)
print(Dog.species)
print(Animal.species)

"""
Dog does not define species.

Python finds it in Animal.
"""


# ============================================================
# 9. CHILD CLASS CAN DEFINE ITS OWN CLASS ATTRIBUTES
# ============================================================

class Animal:
    """Represent an animal."""

    species = "Animal"


class Dog(Animal):
    """Represent a dog."""

    species = "Dog"


print(Animal.species)
print(Dog.species)

"""
Dog defines its own species attribute.

Therefore Dog.species resolves to the value defined by Dog.
"""


# ============================================================
# 10. CHILD CLASS CAN OVERRIDE AN INHERITED METHOD
# ============================================================

class Animal:
    """Represent an animal."""

    def speak(self) -> None:
        print("Animal makes a sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> None:
        print("Dog barks.")


dog = Dog()

dog.speak()

"""
The method exists in both classes.

The child implementation is selected when called through
a Dog object.

Detailed method overriding and polymorphism are covered
in later OOP topics.
"""


# ============================================================
# 11. SINGLE INHERITANCE WITH MULTIPLE LEVELS OF BEHAVIOUR
# ============================================================

class Vehicle:
    """Represent a vehicle."""

    def start(self) -> None:
        print("Vehicle started.")


class Car(Vehicle):
    """Represent a car."""

    def drive(self) -> None:
        print("Car is driving.")


car = Car()

car.start()
car.drive()

"""
Car receives behaviour from Vehicle and combines it with
its own behaviour.
"""


# ============================================================
# 12. ONE PARENT, ONE CHILD
# ============================================================

class Parent:
    """Represent a parent class."""

    def parent_method(self) -> None:
        print("Parent method.")


class Child(Parent):
    """Represent a child class."""

    def child_method(self) -> None:
        print("Child method.")


child = Child()

child.parent_method()
child.child_method()

"""
This is the simplest form of single inheritance:

    Parent
       ↑
    Child
"""


# ============================================================
# 13. CHILD IS-A PARENT
# ============================================================

class Vehicle:
    """Represent a vehicle."""

    pass


class Car(Vehicle):
    """Represent a car."""

    pass


car = Car()

print(isinstance(car, Car))
print(isinstance(car, Vehicle))

"""
The inheritance relationship represents an IS-A relationship:

    Car IS-A Vehicle
"""


# ============================================================
# 14. PARENT DOES NOT INHERIT FROM CHILD
# ============================================================

class Animal:
    """Represent an animal."""

    def eat(self) -> None:
        print("Animal eats.")


class Dog(Animal):
    """Represent a dog."""

    def bark(self) -> None:
        print("Dog barks.")


animal = Animal()

animal.eat()

"""
Animal does not receive bark() from Dog.

Inheritance flows from parent to child:

    Animal
       ↓
      Dog

not the other way around.
"""


# ============================================================
# 15. SINGLE INHERITANCE WITH INSTANCE STATE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> None:
        print(f"My name is {self.name}.")


class Student(Person):
    """Represent a student."""

    def study(self) -> None:
        print(f"{self.name} is studying.")


student = Student("Alice")

student.introduce()
student.study()

"""
Student can use:

    name
    introduce()

from Person.

It also provides:

    study()

of its own.
"""


# ============================================================
# 16. SINGLE INHERITANCE WITH A SPECIALIZED CHILD
# ============================================================

class Employee:
    """Represent an employee."""

    def work(self) -> None:
        print("Employee is working.")


class DataEngineer(Employee):
    """Represent a data engineer."""

    def build_pipeline(self) -> None:
        print("Data engineer is building a data pipeline.")


data_engineer = DataEngineer()

data_engineer.work()
data_engineer.build_pipeline()

"""
The child specializes the behaviour of the parent.

Conceptually:

    Employee
       ↑
    DataEngineer
"""


# ============================================================
# 17. INHERITANCE IS TRANSITIVE
# ============================================================

class Animal:
    """Represent an animal."""

    def eat(self) -> None:
        print("Animal eats.")


class Mammal(Animal):
    """Represent a mammal."""

    def breathe(self) -> None:
        print("Mammal breathes.")


class Dog(Mammal):
    """Represent a dog."""

    def bark(self) -> None:
        print("Dog barks.")


dog = Dog()

dog.eat()
dog.breathe()
dog.bark()

"""
Dog directly inherits from Mammal.

Mammal directly inherits from Animal.

Therefore Dog also receives the accessible behaviour
inherited by Mammal from Animal.

The detailed multilevel inheritance structure is covered
in the next file.
"""


# ============================================================
# 18. SINGLE INHERITANCE VS. MULTIPLE INHERITANCE
# ============================================================

class Animal:
    """Represent an animal."""

    pass


class Dog(Animal):
    """Represent a dog."""

    pass


"""
This is single inheritance:

    class Dog(Animal)

Dog has exactly one direct parent.

Multiple inheritance would look like:

    class Child(ParentA, ParentB)

That is a separate inheritance pattern covered later.
"""


# ============================================================
# 19. OBJECT IS THE ULTIMATE BASE CLASS
# ============================================================

class Person:
    """Represent a person."""

    pass


class Student(Person):
    """Represent a student."""

    pass


student = Student()

print(issubclass(Student, Person))
print(issubclass(Student, object))

"""
The inheritance chain is conceptually:

    object
      ↑
    Person
      ↑
    Student

Every normal Python class ultimately inherits from object.
"""


# ============================================================
# 20. KEY TAKEAWAY
# ============================================================

"""
Single inheritance means:

    One child class
          ↓
    inherits from
          ↓
    One parent class


Basic syntax:

    class Parent:
        ...


    class Child(Parent):
        ...


The child can:

    - use inherited methods
    - access inherited attributes
    - define new methods
    - define new attributes
    - override inherited behaviour

Conceptual structure:

    Parent
      ↑
    Child

Example:

    class Animal:
        def speak(self):
            print("Animal sound.")


    class Dog(Animal):
        def bark(self):
            print("Dog barks.")


    dog = Dog()

    dog.speak()   # inherited
    dog.bark()    # defined by Dog

The essential idea is:

    inheritance
        ↓
    existing parent behaviour
        +
    child-specific behaviour
        ↓
    specialized child class
"""