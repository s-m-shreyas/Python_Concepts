# type: ignore

"""
04_hierarchical_inheritance.py

Demonstrates hierarchical inheritance in Python.

Hierarchical inheritance occurs when multiple child classes
inherit from the same parent class.

Structure:

                 Parent
                /      \
           Child A    Child B

This file focuses on:

    - Basic hierarchical inheritance
    - Multiple children sharing one parent
    - Inherited methods
    - Child-specific behaviour
    - Independent child classes
    - Shared parent behaviour
    - Instance attributes
    - isinstance()
    - issubclass()
"""


# ============================================================
# 1. BASIC HIERARCHICAL INHERITANCE
# ============================================================

class Animal:
    """Represent a generic animal."""

    def eat(self) -> None:
        print("Animal eats.")


class Dog(Animal):
    """Represent a dog."""

    def bark(self) -> None:
        print("Dog barks.")


class Cat(Animal):
    """Represent a cat."""

    def meow(self) -> None:
        print("Cat meows.")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()

"""
Structure:

            Animal
           /      \
        Dog        Cat

Both Dog and Cat inherit eat() from Animal.

Each child also provides its own behaviour.
"""


# ============================================================
# 2. MULTIPLE CHILDREN SHARE THE SAME PARENT
# ============================================================

class Vehicle:
    """Represent a generic vehicle."""

    def start(self) -> None:
        print("Vehicle started.")


class Car(Vehicle):
    """Represent a car."""

    def drive(self) -> None:
        print("Car is driving.")


class Bike(Vehicle):
    """Represent a bike."""

    def ride(self) -> None:
        print("Bike is being ridden.")


car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()


# ============================================================
# 3. CHILD CLASSES CAN HAVE DIFFERENT BEHAVIOUR
# ============================================================

class Employee:
    """Represent an employee."""

    def work(self) -> None:
        print("Employee is working.")


class Developer(Employee):
    """Represent a developer."""

    def write_code(self) -> None:
        print("Developer is writing code.")


class Tester(Employee):
    """Represent a tester."""

    def test_software(self) -> None:
        print("Tester is testing software.")


developer = Developer()
tester = Tester()

developer.work()
developer.write_code()

tester.work()
tester.test_software()

"""
Both children inherit:

    work()

But each child adds different behaviour.
"""


# ============================================================
# 4. SHARED PARENT METHOD
# ============================================================

class Person:
    """Represent a person."""

    def introduce(self) -> None:
        print("I am a person.")


class Student(Person):
    """Represent a student."""

    def study(self) -> None:
        print("Student is studying.")


class Employee(Person):
    """Represent an employee."""

    def work(self) -> None:
        print("Employee is working.")


student = Student()
employee = Employee()

student.introduce()
student.study()

employee.introduce()
employee.work()

"""
Structure:

             Person
             /    \
        Student   Employee

Both children inherit introduce() independently.
"""


# ============================================================
# 5. CHILD CLASSES CAN HAVE THEIR OWN CLASS ATTRIBUTES
# ============================================================

class Animal:
    """Represent a generic animal."""

    kingdom = "Animalia"


class Dog(Animal):
    """Represent a dog."""

    species = "Canis familiaris"


class Cat(Animal):
    """Represent a cat."""

    species = "Felis catus"


print(Dog.kingdom)
print(Dog.species)

print(Cat.kingdom)
print(Cat.species)

"""
Both children inherit:

    kingdom

from Animal.

Each child defines its own:

    species
"""


# ============================================================
# 6. CHILD CLASSES CAN HAVE THEIR OWN INSTANCE STATE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


class Student(Person):
    """Represent a student."""

    def __init__(self, name: str, grade: int) -> None:
        self.name = name
        self.grade = grade


class Employee(Person):
    """Represent an employee."""

    def __init__(self, name: str, employee_id: int) -> None:
        self.name = name
        self.employee_id = employee_id


student = Student("Alice", 90)
employee = Employee("Bob", 101)

print(student.__dict__)
print(employee.__dict__)

"""
The child classes maintain their own instance state.

Student:

    name
    grade

Employee:

    name
    employee_id
"""


# ============================================================
# 7. SHARED PARENT METHOD, DIFFERENT CHILD IMPLEMENTATIONS
# ============================================================

class Animal:
    """Represent a generic animal."""

    def move(self) -> None:
        print("Animal moves.")


class Dog(Animal):
    """Represent a dog."""

    def bark(self) -> None:
        print("Dog barks.")


class Bird(Animal):
    """Represent a bird."""

    def fly(self) -> None:
        print("Bird flies.")


dog = Dog()
bird = Bird()

dog.move()
dog.bark()

bird.move()
bird.fly()


# ============================================================
# 8. HIERARCHICAL INHERITANCE WITH THREE CHILDREN
# ============================================================

class Shape:
    """Represent a generic shape."""

    def describe(self) -> None:
        print("This is a shape.")


class Circle(Shape):
    """Represent a circle."""

    def draw_circle(self) -> None:
        print("Drawing circle.")


class Rectangle(Shape):
    """Represent a rectangle."""

    def draw_rectangle(self) -> None:
        print("Drawing rectangle.")


class Triangle(Shape):
    """Represent a triangle."""

    def draw_triangle(self) -> None:
        print("Drawing triangle.")


circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

circle.describe()
circle.draw_circle()

rectangle.describe()
rectangle.draw_rectangle()

triangle.describe()
triangle.draw_triangle()

"""
Structure:

                 Shape
             /     |      \
        Circle  Rectangle  Triangle
"""


# ============================================================
# 9. CHILD CLASSES ARE INDEPENDENT OF EACH OTHER
# ============================================================

class Animal:
    """Represent a generic animal."""

    def eat(self) -> None:
        print("Animal eats.")


class Dog(Animal):
    """Represent a dog."""

    def bark(self) -> None:
        print("Dog barks.")


class Cat(Animal):
    """Represent a cat."""

    def meow(self) -> None:
        print("Cat meows.")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()

"""
Dog does not inherit from Cat.

Cat does not inherit from Dog.

Both independently inherit from Animal.
"""


# ============================================================
# 10. CHILD CLASSES DO NOT INHERIT FROM EACH OTHER
# ============================================================

class Animal:
    """Represent an animal."""

    def eat(self) -> None:
        print("Animal eats.")


class Dog(Animal):
    """Represent a dog."""

    def bark(self) -> None:
        print("Dog barks.")


class Cat(Animal):
    """Represent a cat."""

    def meow(self) -> None:
        print("Cat meows.")


dog = Dog()

dog.eat()
dog.bark()

"""
Dog cannot use meow() simply because Cat also inherits from
Animal.

The relationship is:

    Animal
      ↓
    Dog

and separately:

    Animal
      ↓
    Cat
"""


# ============================================================
# 11. CHECKING HIERARCHICAL RELATIONSHIPS WITH issubclass()
# ============================================================

class Animal:
    """Represent an animal."""

    pass


class Dog(Animal):
    """Represent a dog."""

    pass


class Cat(Animal):
    """Represent a cat."""

    pass


print(issubclass(Dog, Animal))
print(issubclass(Cat, Animal))

print(issubclass(Dog, Cat))
print(issubclass(Cat, Dog))

"""
Results:

    Dog → Animal : True
    Cat → Animal : True

But:

    Dog → Cat : False
    Cat → Dog : False
"""


# ============================================================
# 12. CHECKING INSTANCES
# ============================================================

class Animal:
    """Represent an animal."""

    pass


class Dog(Animal):
    """Represent a dog."""

    pass


class Cat(Animal):
    """Represent a cat."""

    pass


dog = Dog()
cat = Cat()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(isinstance(cat, Cat))
print(isinstance(cat, Animal))

print(isinstance(dog, Cat))
print(isinstance(cat, Dog))

"""
Each child instance is also an instance of the common parent.

But sibling classes are unrelated through inheritance.
"""


# ============================================================
# 13. SHARED CLASS ATTRIBUTE
# ============================================================

class Employee:
    """Represent an employee."""

    company = "TechCorp"


class Developer(Employee):
    """Represent a developer."""

    pass


class Tester(Employee):
    """Represent a tester."""

    pass


print(Developer.company)
print(Tester.company)

"""
Both children inherit company from Employee.
"""


# ============================================================
# 14. CHILD CAN OVERRIDE THE SHARED ATTRIBUTE
# ============================================================

class Employee:
    """Represent an employee."""

    company = "TechCorp"


class Developer(Employee):
    """Represent a developer."""

    company = "DevCorp"


class Tester(Employee):
    """Represent a tester."""

    pass


print(Developer.company)
print(Tester.company)

"""
Developer overrides company.

Tester continues to inherit company from Employee.
"""


# ============================================================
# 15. CHILD CAN OVERRIDE A SHARED METHOD
# ============================================================

class Animal:
    """Represent a generic animal."""

    def speak(self) -> None:
        print("Generic animal sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> None:
        print("Dog barks.")


class Cat(Animal):
    """Represent a cat."""

    def speak(self) -> None:
        print("Cat meows.")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

"""
The parent provides a common interface.

Each child provides its own implementation.

The deeper topic of polymorphism is covered separately.
"""


# ============================================================
# 16. HIERARCHICAL INHERITANCE WITH A COMMON BASE METHOD
# ============================================================

class Database:
    """Represent a database."""

    def connect(self) -> None:
        print("Connected to database.")


class PostgreSQL(Database):
    """Represent PostgreSQL."""

    def query(self) -> None:
        print("Executing PostgreSQL query.")


class MySQL(Database):
    """Represent MySQL."""

    def query(self) -> None:
        print("Executing MySQL query.")


postgresql = PostgreSQL()
mysql = MySQL()

postgresql.connect()
postgresql.query()

mysql.connect()
mysql.query()

"""
Both database classes share the common connection behaviour
from Database but provide their own query behaviour.
"""


# ============================================================
# 17. HIERARCHICAL INHERITANCE AND SPECIALIZATION
# ============================================================

class Vehicle:
    """Represent a generic vehicle."""

    def start(self) -> None:
        print("Vehicle started.")


class Car(Vehicle):
    """Represent a car."""

    def drive(self) -> None:
        print("Car is driving.")


class Bike(Vehicle):
    """Represent a bike."""

    def ride(self) -> None:
        print("Bike is riding.")


class Truck(Vehicle):
    """Represent a truck."""

    def load(self) -> None:
        print("Truck is loading cargo.")


car = Car()
bike = Bike()
truck = Truck()

car.start()
car.drive()

bike.start()
bike.ride()

truck.start()
truck.load()

"""
A common parent defines shared behaviour.

Each child specializes it for a particular type.
"""


# ============================================================
# 18. HIERARCHICAL INHERITANCE DOES NOT MEAN MULTIPLE
#     INHERITANCE
# ============================================================

class Animal:
    """Base class."""

    pass


class Dog(Animal):
    """Child class."""

    pass


class Cat(Animal):
    """Child class."""

    pass

"""
This is hierarchical inheritance:

             Animal
             /   \
           Dog   Cat

Each child has ONE direct parent.

Multiple inheritance would instead look like:

    class Child(ParentA, ParentB):
        ...

"""


# ============================================================
# 19. HIERARCHICAL INHERITANCE CAN BE COMBINED WITH
#     MULTILEVEL INHERITANCE
# ============================================================

class Animal:
    """Represent an animal."""

    def eat(self) -> None:
        print("Animal eats.")


class Mammal(Animal):
    """Represent a mammal."""

    def breathe(self) -> None:
        print("Mammal breathes.")


class Bird(Animal):
    """Represent a bird."""

    def fly(self) -> None:
        print("Bird flies.")


class Dog(Mammal):
    """Represent a dog."""

    def bark(self) -> None:
        print("Dog barks.")


dog = Dog()
bird = Bird()

dog.eat()
dog.breathe()
dog.bark()

bird.eat()
bird.fly()

"""
The structure now contains both patterns:

             Animal
             /    \
        Mammal    Bird
          |
         Dog

Animal → Mammal → Dog

and:

Animal → Bird

This shows that inheritance structures can be combined.
"""


# ============================================================
# 20. KEY TAKEAWAY
# ============================================================

"""
Hierarchical inheritance means:

                 Parent
                /      \
           Child A    Child B


Example:

    class Animal:
        def eat(self):
            ...


    class Dog(Animal):
        def bark(self):
            ...


    class Cat(Animal):
        def meow(self):
            ...


Here:

    Dog  → Animal
    Cat  → Animal

Both children share the behaviour provided by Animal.

However:

    Dog does not inherit from Cat.
    Cat does not inherit from Dog.

The important idea is:

    one common parent
          ↓
    multiple specialized children


Hierarchical inheritance is useful when several related
classes share common behaviour but also need their own
specialized behaviour.
"""