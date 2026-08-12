# type: ignore

"""
02_multilevel_inheritance.py

Demonstrates multilevel inheritance in Python.

Multilevel inheritance occurs when a class inherits from a
class that itself inherits from another class.

Structure:

    Grandparent
         ↑
       Parent
         ↑
       Child

The child can access inherited members from its direct parent
and from earlier classes in the inheritance chain.

This file focuses on:

    - Multilevel inheritance
    - Inheritance chains
    - Direct and indirect inheritance
    - Transitive inheritance
    - Instance methods across inheritance levels
    - Instance attributes across inheritance levels
    - issubclass()
    - isinstance()
"""


# ============================================================
# 1. BASIC MULTILEVEL INHERITANCE
# ============================================================

class Animal:
    """Represent a generic animal."""

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
Inheritance chain:

    Animal
       ↑
    Mammal
       ↑
      Dog

Dog directly inherits from Mammal.

Mammal directly inherits from Animal.

Therefore Dog can access behaviour from both classes.
"""


# ============================================================
# 2. DIRECT VS. INDIRECT INHERITANCE
# ============================================================

class Vehicle:
    """Represent a vehicle."""

    def start(self) -> None:
        print("Vehicle started.")


class Car(Vehicle):
    """Represent a car."""

    def drive(self) -> None:
        print("Car is driving.")


class ElectricCar(Car):
    """Represent an electric car."""

    def charge(self) -> None:
        print("Electric car is charging.")


electric_car = ElectricCar()

electric_car.start()
electric_car.drive()
electric_car.charge()

"""
ElectricCar directly inherits from Car.

ElectricCar indirectly inherits from Vehicle.

Therefore:

    Car
        → direct parent of ElectricCar

    Vehicle
        → indirect ancestor of ElectricCar
"""


# ============================================================
# 3. THREE LEVELS OF INSTANCE BEHAVIOUR
# ============================================================

class Person:
    """Represent a person."""

    def introduce(self) -> None:
        print("I am a person.")


class Employee(Person):
    """Represent an employee."""

    def work(self) -> None:
        print("Employee is working.")


class Developer(Employee):
    """Represent a developer."""

    def write_code(self) -> None:
        print("Developer is writing code.")


developer = Developer()

developer.introduce()
developer.work()
developer.write_code()

"""
Developer can use:

    introduce() → Person
    work()      → Employee
    write_code() → Developer
"""


# ============================================================
# 4. MULTILEVEL INHERITANCE WITH INSTANCE ATTRIBUTES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


class Employee(Person):
    """Represent an employee."""

    def set_employee_id(self, employee_id: int) -> None:
        self.employee_id = employee_id


class Developer(Employee):
    """Represent a developer."""

    def set_language(self, language: str) -> None:
        self.language = language


developer = Developer("Alice")

developer.set_employee_id(101)
developer.set_language("Python")

print(developer.name)
print(developer.employee_id)
print(developer.language)

"""
The instance contains state introduced at different levels:

    Person
        → name

    Employee
        → employee_id

    Developer
        → language
"""


# ============================================================
# 5. TRANSITIVE INHERITANCE
# ============================================================

class A:
    """Base class."""

    def method_a(self) -> None:
        print("Method from A.")


class B(A):
    """Intermediate class."""

    def method_b(self) -> None:
        print("Method from B.")


class C(B):
    """Derived class."""

    def method_c(self) -> None:
        print("Method from C.")


obj = C()

obj.method_a()
obj.method_b()
obj.method_c()

"""
C inherits directly from B.

B inherits directly from A.

Therefore C indirectly inherits from A.

This is called transitive inheritance.
"""


# ============================================================
# 6. CHECKING THE INHERITANCE CHAIN WITH issubclass()
# ============================================================

class Animal:
    """Represent an animal."""

    pass


class Mammal(Animal):
    """Represent a mammal."""

    pass


class Dog(Mammal):
    """Represent a dog."""

    pass


print(issubclass(Dog, Mammal))
print(issubclass(Dog, Animal))
print(issubclass(Mammal, Animal))

"""
Results:

    Dog → Mammal  : True
    Dog → Animal  : True
    Mammal → Animal : True

Dog is considered a subclass of Animal even though Dog does
not directly inherit from Animal.
"""


# ============================================================
# 7. CHECKING INSTANCE RELATIONSHIPS WITH isinstance()
# ============================================================

class Animal:
    """Represent an animal."""

    pass


class Mammal(Animal):
    """Represent a mammal."""

    pass


class Dog(Mammal):
    """Represent a dog."""

    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Mammal))
print(isinstance(dog, Animal))
print(isinstance(dog, object))

"""
A Dog object is also considered:

    Dog
    Mammal
    Animal
    object

because of the inheritance chain.
"""


# ============================================================
# 8. INHERITED CLASS ATTRIBUTES THROUGH MULTIPLE LEVELS
# ============================================================

class Animal:
    """Represent an animal."""

    kingdom = "Animalia"


class Mammal(Animal):
    """Represent a mammal."""

    category = "Mammal"


class Dog(Mammal):
    """Represent a dog."""

    species = "Canis familiaris"


dog = Dog()

print(dog.kingdom)
print(dog.category)
print(dog.species)

"""
Dog can access attributes defined at every level:

    kingdom → Animal
    category → Mammal
    species → Dog
"""


# ============================================================
# 9. CLASS ATTRIBUTE LOOKUP THROUGH THE INHERITANCE CHAIN
# ============================================================

class A:
    """Base class."""

    value = "A"


class B(A):
    """Intermediate class."""

    pass


class C(B):
    """Derived class."""

    pass


print(C.value)

"""
C does not define value.

Python searches its inheritance chain and finds:

    A.value
"""


# ============================================================
# 10. CHILD CLASS CAN OVERRIDE AN INHERITED ATTRIBUTE
# ============================================================

class Animal:
    """Represent an animal."""

    category = "Animal"


class Mammal(Animal):
    """Represent a mammal."""

    category = "Mammal"


class Dog(Mammal):
    """Represent a dog."""

    category = "Dog"


print(Animal.category)
print(Mammal.category)
print(Dog.category)

"""
Each class defines the same attribute.

The value found first in the inheritance lookup is used.
"""


# ============================================================
# 11. METHOD OVERRIDING IN A MULTILEVEL CHAIN
# ============================================================

class Animal:
    """Represent an animal."""

    def speak(self) -> None:
        print("Animal sound.")


class Mammal(Animal):
    """Represent a mammal."""

    def speak(self) -> None:
        print("Mammal sound.")


class Dog(Mammal):
    """Represent a dog."""

    def speak(self) -> None:
        print("Dog bark.")


dog = Dog()

dog.speak()

"""
All three classes define speak().

The implementation in Dog is selected for a Dog instance.

Method resolution through inheritance chains is explored
more deeply in the MRO file.
"""


# ============================================================
# 12. CHILD DOES NOT HAVE TO OVERRIDE EVERY PARENT METHOD
# ============================================================

class Animal:
    """Represent an animal."""

    def eat(self) -> None:
        print("Animal eats.")

    def sleep(self) -> None:
        print("Animal sleeps.")


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
dog.sleep()
dog.breathe()
dog.bark()

"""
Dog defines only bark().

The other methods are inherited through the chain.
"""


# ============================================================
# 13. MULTILEVEL INHERITANCE WITH SPECIALIZATION
# ============================================================

class Employee:
    """Represent an employee."""

    def work(self) -> None:
        print("Employee is working.")


class SoftwareEngineer(Employee):
    """Represent a software engineer."""

    def develop(self) -> None:
        print("Software engineer is developing software.")


class DataEngineer(SoftwareEngineer):
    """Represent a data engineer."""

    def build_pipeline(self) -> None:
        print("Data engineer is building a data pipeline.")


data_engineer = DataEngineer()

data_engineer.work()
data_engineer.develop()
data_engineer.build_pipeline()

"""
Each level specializes the previous level:

    Employee
        ↓
    SoftwareEngineer
        ↓
    DataEngineer
"""


# ============================================================
# 14. MULTILEVEL INHERITANCE DOES NOT COPY ATTRIBUTES
# ============================================================

class A:
    """Base class."""

    value = 10


class B(A):
    """Intermediate class."""

    pass


class C(B):
    """Derived class."""

    pass


print(C.value)

"""
C does not receive an independent copy of value simply
because it inherits from A.

Attribute lookup follows the inheritance relationship.
"""


# ============================================================
# 15. INHERITANCE CHAIN USING __bases__
# ============================================================

class Animal:
    """Represent an animal."""

    pass


class Mammal(Animal):
    """Represent a mammal."""

    pass


class Dog(Mammal):
    """Represent a dog."""

    pass


print(Dog.__bases__)
print(Mammal.__bases__)
print(Animal.__bases__)

"""
__bases__ shows the direct base classes of a class.

Therefore:

    Dog.__bases__
        → Mammal

    Mammal.__bases__
        → Animal

    Animal.__bases__
        → object
"""


# ============================================================
# 16. INHERITANCE CHAIN USING __mro__
# ============================================================

class Animal:
    """Represent an animal."""

    pass


class Mammal(Animal):
    """Represent a mammal."""

    pass


class Dog(Mammal):
    """Represent a dog."""

    pass


print(Dog.__mro__)

"""
__mro__ displays the method resolution order.

Conceptually:

    Dog
      ↓
    Mammal
      ↓
    Animal
      ↓
    object
"""


# ============================================================
# 17. MULTILEVEL INHERITANCE WITH A THREE-LEVEL CHAIN
# ============================================================

class LevelOne:
    """First level."""

    def first(self) -> None:
        print("Level one.")


class LevelTwo(LevelOne):
    """Second level."""

    def second(self) -> None:
        print("Level two.")


class LevelThree(LevelTwo):
    """Third level."""

    def third(self) -> None:
        print("Level three.")


instance = LevelThree()

instance.first()
instance.second()
instance.third()


# ============================================================
# 18. MULTILEVEL INHERITANCE WITH A FOUR-LEVEL CHAIN
# ============================================================

class Organization:
    """Represent an organization."""

    def organization_info(self) -> None:
        print("Organization")


class Department(Organization):
    """Represent a department."""

    def department_info(self) -> None:
        print("Department")


class Team(Department):
    """Represent a team."""

    def team_info(self) -> None:
        print("Team")


class Developer(Team):
    """Represent a developer."""

    def developer_info(self) -> None:
        print("Developer")


developer = Developer()

developer.organization_info()
developer.department_info()
developer.team_info()
developer.developer_info()

"""
Inheritance chain:

    Organization
         ↑
    Department
         ↑
       Team
         ↑
     Developer
"""


# ============================================================
# 19. MULTILEVEL INHERITANCE IS NOT THE SAME AS MULTIPLE
# ============================================================

class Animal:
    """Represent an animal."""

    pass


class Mammal(Animal):
    """Represent a mammal."""

    pass


class Dog(Mammal):
    """Represent a dog."""

    pass


"""
This is multilevel inheritance:

    Animal
       ↑
    Mammal
       ↑
      Dog

Multiple inheritance would have multiple direct parents:

    class Child(ParentA, ParentB):
        ...

These are different inheritance patterns.
"""


# ============================================================
# 20. KEY TAKEAWAY
# ============================================================

"""
Multilevel inheritance means:

    Grandparent
         ↑
       Parent
         ↑
       Child

Example:

    class Animal:
        def eat(self):
            ...


    class Mammal(Animal):
        def breathe(self):
            ...


    class Dog(Mammal):
        def bark(self):
            ...


    dog = Dog()

    dog.eat()
    dog.breathe()
    dog.bark()


The important idea is:

    Dog
     ↓
    Mammal
     ↓
    Animal
     ↓
    object

Dog directly inherits from Mammal.

Dog indirectly inherits from Animal.

Because inheritance is transitive, Dog can access
appropriate inherited members from both ancestors.

Multilevel inheritance therefore builds a chain of
specialization:

    general
      ↓
    more specific
      ↓
    even more specific
"""