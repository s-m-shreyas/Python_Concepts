# type: ignore

"""
05_method_inheritance.py

Demonstrates method inheritance in Python.

Method inheritance means a child class can use methods
defined by its parent class without redefining them.

This file focuses specifically on how methods behave across
an inheritance relationship.

Topics covered:

    - Inheriting methods
    - Calling inherited methods
    - Adding new methods in a child
    - Overriding inherited methods
    - Method lookup
    - Parent method access
    - Inherited instance methods
    - Inherited class methods
    - Inherited static methods
    - Method inheritance across multiple levels
"""


# ============================================================
# 1. BASIC METHOD INHERITANCE
# ============================================================

class Animal:
    """Represent a generic animal."""

    def eat(self) -> None:
        print("Animal is eating.")


class Dog(Animal):
    """Represent a dog."""

    pass


dog = Dog()

dog.eat()

"""
Dog does not define eat().

Python finds eat() in Animal and executes it.

This is the simplest example of method inheritance.
"""


# ============================================================
# 2. CHILD CAN ADD ITS OWN METHODS
# ============================================================

class Animal:
    """Represent a generic animal."""

    def eat(self) -> None:
        print("Animal is eating.")


class Dog(Animal):
    """Represent a dog."""

    def bark(self) -> None:
        print("Dog is barking.")


dog = Dog()

dog.eat()
dog.bark()

"""
Dog has access to:

    eat()   → inherited from Animal
    bark()  → defined by Dog
"""


# ============================================================
# 3. INHERITED METHOD CAN USE THE CHILD INSTANCE
# ============================================================

class Person:
    """Represent a person."""

    def introduce(self) -> None:
        print(f"My name is {self.name}.")


class Student(Person):
    """Represent a student."""

    def __init__(self, name: str) -> None:
        self.name = name


student = Student("Alice")

student.introduce()

"""
introduce() is defined in Person.

However, self refers to the Student instance when the
inherited method is called.

Therefore:

    self.name

is resolved against the Student object.
"""


# ============================================================
# 4. INHERITED METHOD CAN ACCESS CHILD ATTRIBUTES
# ============================================================

class Employee:
    """Represent an employee."""

    def describe(self) -> None:
        print(f"Employee ID: {self.employee_id}")


class Developer(Employee):
    """Represent a developer."""

    def __init__(self, employee_id: int) -> None:
        self.employee_id = employee_id


developer = Developer(101)

developer.describe()

"""
describe() belongs to Employee.

But self refers to developer.

Therefore the inherited method can access attributes stored
on the child object.
"""


# ============================================================
# 5. CHILD CLASS CAN OVERRIDE A METHOD
# ============================================================

class Animal:
    """Represent a generic animal."""

    def speak(self) -> None:
        print("Animal makes a sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> None:
        print("Dog barks.")


dog = Dog()

dog.speak()

"""
Dog defines its own speak().

Therefore the inherited Animal.speak() is not selected when
speak() is called through a Dog object.

This is called method overriding.
"""


# ============================================================
# 6. OVERRIDING DOES NOT DELETE THE PARENT METHOD
# ============================================================

class Animal:
    """Represent a generic animal."""

    def speak(self) -> None:
        print("Animal sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> None:
        print("Dog bark.")


animal = Animal()
dog = Dog()

animal.speak()
dog.speak()

"""
Animal.speak() still exists.

Dog simply provides another implementation that is selected
for Dog instances.
"""


# ============================================================
# 7. EXPLICITLY CALLING THE PARENT METHOD
# ============================================================

class Animal:
    """Represent a generic animal."""

    def speak(self) -> None:
        print("Animal sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> None:
        Animal.speak(self)
        print("Dog bark.")


dog = Dog()

dog.speak()

"""
The parent implementation can be called explicitly using:

    Animal.speak(self)

The super() mechanism provides a cleaner approach for this
purpose and is covered in 08_super_function.py.
"""


# ============================================================
# 8. METHOD LOOKUP
# ============================================================

class Parent:
    """Represent a parent class."""

    def show(self) -> None:
        print("Parent.show()")


class Child(Parent):
    """Represent a child class."""

    pass


child = Child()

child.show()

"""
Python searches for show() starting from the class of child:

    Child
      ↓
    Parent
      ↓
    object

Child does not contain show(), so Python finds it in Parent.
"""


# ============================================================
# 9. METHOD LOOKUP WHEN BOTH CLASSES DEFINE THE METHOD
# ============================================================

class Parent:
    """Represent a parent class."""

    def show(self) -> None:
        print("Parent.show()")


class Child(Parent):
    """Represent a child class."""

    def show(self) -> None:
        print("Child.show()")


child = Child()

child.show()

"""
Python finds show() in Child first.

Therefore Child.show() is executed.
"""


# ============================================================
# 10. METHOD INHERITANCE ACROSS MULTIPLE LEVELS
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
Dog receives methods from different levels:

    eat()      → Animal
    breathe()  → Mammal
    bark()     → Dog
"""


# ============================================================
# 11. METHOD INHERITANCE IN HIERARCHICAL INHERITANCE
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
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()

"""
Both children independently inherit eat() from Animal.
"""


# ============================================================
# 12. METHOD INHERITANCE IN MULTIPLE INHERITANCE
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

    pass


duck = Duck()

duck.fly()
duck.swim()

"""
Duck inherits methods from both parent classes.
"""


# ============================================================
# 13. INHERITED METHODS CAN CALL OTHER METHODS
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        print("Hello.")

    def introduce(self) -> None:
        self.greet()
        print("I am a person.")


class Student(Person):
    """Represent a student."""

    pass


student = Student()

student.introduce()

"""
introduce() is inherited from Person.

Inside introduce():

    self.greet()

is also resolved through the Student object's method lookup.
"""


# ============================================================
# 14. CHILD OVERRIDE CAN CHANGE INTERNAL METHOD CALLS
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        print("Hello.")


    def introduce(self) -> None:
        self.greet()
        print("I am a person.")


class Student(Person):
    """Represent a student."""

    def greet(self) -> None:
        print("Hello from student.")


student = Student()

student.introduce()

"""
introduce() is inherited from Person.

But introduce() contains:

    self.greet()

Because self is a Student instance, Python resolves greet()
to Student.greet().

This is an important property of method lookup.
"""


# ============================================================
# 15. INHERITED METHOD WITH PARAMETERS
# ============================================================

class Calculator:
    """Provide calculator operations."""

    def add(self, first: int, second: int) -> int:
        return first + second


class ScientificCalculator(Calculator):
    """Represent a scientific calculator."""

    pass


calculator = ScientificCalculator()

result = calculator.add(10, 20)

print(result)

"""
The child inherits the complete method interface:

    add(first, second)

without redefining it.
"""


# ============================================================
# 16. CHILD CAN ADD METHODS WITHOUT AFFECTING THE PARENT
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
dog = Dog()

animal.eat()
dog.eat()
dog.bark()

"""
Adding bark() to Dog does not add bark() to Animal.

The inheritance relationship flows from parent to child.
"""


# ============================================================
# 17. INHERITED CLASS METHOD
# ============================================================

class Person:
    """Represent a person."""

    @classmethod
    def create_default(cls) -> "Person":
        return cls()


class Student(Person):
    """Represent a student."""

    pass


student = Student.create_default()

print(type(student).__name__)

"""
The class method is inherited by Student.

Because cls refers to the class through which the method
was called:

    Student.create_default()

cls becomes Student.

Therefore:

    cls()

creates a Student instance.

This is one important difference between cls and self.
"""


# ============================================================
# 18. INHERITED STATIC METHOD
# ============================================================

class MathTools:
    """Provide mathematical utilities."""

    @staticmethod
    def square(value: int) -> int:
        return value * value


class AdvancedMathTools(MathTools):
    """Extend mathematical utilities."""

    pass


print(AdvancedMathTools.square(5))

"""
Static methods can also be inherited.

Because static methods do not receive self or cls automatically,
there is no instance or class binding involved.
"""


# ============================================================
# 19. INHERITED METHOD CAN BE USED THROUGH THE CLASS
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        print("Hello.")


class Student(Person):
    """Represent a student."""

    pass


student = Student()

Person.greet(student)
Student.greet(student)

"""
Both expressions access the same inherited function.

When called explicitly through the class, the instance must
be supplied manually.
"""


# ============================================================
# 20. FUNCTION OBJECT VS. BOUND METHOD
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        print("Hello.")


class Student(Person):
    """Represent a student."""

    pass


student = Student()

print(Person.greet)
print(student.greet)

"""
Person.greet is the function stored on the class.

student.greet is a bound method associated with student.

Method binding is explored more deeply in:

    02_classes/
        08_method_binding.py
"""


# ============================================================
# 21. INHERITED METHODS ARE NOT COPIED INTO THE CHILD CLASS
# ============================================================

class Parent:
    """Parent class."""

    def show(self) -> None:
        print("Parent method.")


class Child(Parent):
    """Child class."""

    pass


print("show" in Child.__dict__)
print("show" in Parent.__dict__)

"""
The result is:

    False
    True

Child can use show(), but show() is not copied into
Child.__dict__.

Python finds it through inheritance.
"""


# ============================================================
# 22. METHOD INHERITANCE AND __dict__
# ============================================================

class Parent:
    """Parent class."""

    def parent_method(self) -> None:
        print("Parent method.")


class Child(Parent):
    """Child class."""

    def child_method(self) -> None:
        print("Child method.")


print(Parent.__dict__.keys())
print(Child.__dict__.keys())

"""
parent_method exists in Parent.__dict__.

child_method exists in Child.__dict__.

The child can still access parent_method because Python
searches the inheritance chain.
"""


# ============================================================
# 23. INHERITED METHODS CAN BE OVERRIDDEN SELECTIVELY
# ============================================================

class Animal:
    """Represent an animal."""

    def eat(self) -> None:
        print("Animal eats.")

    def sleep(self) -> None:
        print("Animal sleeps.")


class Dog(Animal):
    """Represent a dog."""

    def bark(self) -> None:
        print("Dog barks.")


dog = Dog()

dog.eat()
dog.sleep()
dog.bark()

"""
Dog inherits both eat() and sleep().

It adds bark().

There is no need to redefine methods whose behaviour is
already appropriate.
"""


# ============================================================
# 24. METHOD INHERITANCE VS. METHOD OVERRIDING
# ============================================================

class Parent:
    """Parent class."""

    def show(self) -> None:
        print("Parent implementation.")


class ChildWithoutOverride(Parent):
    """Child that inherits the method unchanged."""

    pass


class ChildWithOverride(Parent):
    """Child that replaces the method implementation."""

    def show(self) -> None:
        print("Child implementation.")


first = ChildWithoutOverride()
second = ChildWithOverride()

first.show()
second.show()

"""
ChildWithoutOverride:

    inherits show()

ChildWithOverride:

    overrides show()
"""


# ============================================================
# 25. KEY TAKEAWAY
# ============================================================

"""
Method inheritance means a child class can use methods
defined by its parent without redefining them.

Example:

    class Animal:
        def eat(self):
            print("Eating")


    class Dog(Animal):
        pass


    dog = Dog()
    dog.eat()


The method is not copied into Dog.

Python performs method lookup through the inheritance chain.

Conceptually:

    dog.eat()
        ↓
    Dog
        ↓
    Animal
        ↓
    object


If the child defines the same method:

    class Dog(Animal):
        def eat(self):
            print("Dog eating")


then the child implementation is found first.

So remember:

    Inheritance
        ↓
    Reuse existing methods


    Override
        ↓
    Replace inherited behaviour


    Add method
        ↓
    Extend child-specific behaviour


The next topic, attribute inheritance, applies the same
general inheritance idea to attributes.
"""