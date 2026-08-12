# type: ignore

"""
07_method_resolution_order.py

Demonstrates Method Resolution Order (MRO) in Python.

MRO is the order in which Python searches classes when
looking for a method or attribute.

This file focuses on:

    - What MRO means
    - __mro__
    - mro()
    - Single inheritance MRO
    - Multilevel inheritance MRO
    - Multiple inheritance MRO
    - Method lookup using MRO
    - Attribute lookup using MRO
    - MRO and overriding
    - Diamond inheritance
    - C3 linearization
    - Why inheritance order matters
"""


# ============================================================
# 1. BASIC MRO
# ============================================================

class Animal:
    """Represent a generic animal."""

    pass


class Dog(Animal):
    """Represent a dog."""

    pass


print(Dog.__mro__)

"""
Typical result:

    (
        <class '__main__.Dog'>,
        <class '__main__.Animal'>,
        <class 'object'>
    )

The search order is:

    Dog
      ↓
    Animal
      ↓
    object
"""


# ============================================================
# 2. mro() METHOD
# ============================================================

class Animal:
    """Represent a generic animal."""

    pass


class Dog(Animal):
    """Represent a dog."""

    pass


print(Dog.mro())

"""
Dog.mro() returns the same MRO information as Dog.__mro__,
but as a list.
"""


# ============================================================
# 3. __mro__ VS mro()
# ============================================================

class Parent:
    """Parent class."""

    pass


class Child(Parent):
    """Child class."""

    pass


print(Child.__mro__)
print(Child.mro())

"""
__mro__:

    tuple

mro():

    list
"""


# ============================================================
# 4. MRO IN MULTILEVEL INHERITANCE
# ============================================================

class Animal:
    """Base class."""

    pass


class Mammal(Animal):
    """Intermediate class."""

    pass


class Dog(Mammal):
    """Derived class."""

    pass


print(Dog.__mro__)

"""
MRO:

    Dog
      ↓
    Mammal
      ↓
    Animal
      ↓
    object
"""


# ============================================================
# 5. MRO CONTROLS METHOD LOOKUP
# ============================================================

class Animal:
    """Base class."""

    def speak(self) -> None:
        print("Animal speaks.")


class Dog(Animal):
    """Child class."""

    pass


dog = Dog()

dog.speak()

"""
Python searches:

    Dog
      ↓
    Animal

speak() is found in Animal.

Therefore Animal.speak() executes.
"""


# ============================================================
# 6. CHILD METHOD IS FOUND BEFORE PARENT METHOD
# ============================================================

class Animal:
    """Base class."""

    def speak(self) -> None:
        print("Animal speaks.")


class Dog(Animal):
    """Child class."""

    def speak(self) -> None:
        print("Dog barks.")


dog = Dog()

dog.speak()

"""
MRO:

    Dog
      ↓
    Animal
      ↓
    object

speak() exists in Dog.

Python stops searching once it finds the attribute.
"""


# ============================================================
# 7. MRO ALSO CONTROLS ATTRIBUTE LOOKUP
# ============================================================

class Animal:
    """Base class."""

    species = "Animal"


class Dog(Animal):
    """Child class."""

    pass


print(Dog.species)

"""
Python searches:

    Dog
      ↓
    Animal

species is found in Animal.
"""


# ============================================================
# 8. MRO WITH MULTIPLE INHERITANCE
# ============================================================

class Flyer:
    """Provide flying behaviour."""

    pass


class Swimmer:
    """Provide swimming behaviour."""

    pass


class Duck(Flyer, Swimmer):
    """Represent a duck."""

    pass


print(Duck.__mro__)

"""
Typical MRO:

    Duck
      ↓
    Flyer
      ↓
    Swimmer
      ↓
    object
"""


# ============================================================
# 9. INHERITANCE ORDER MATTERS
# ============================================================

class ParentA:
    """First parent."""

    value = "A"


class ParentB:
    """Second parent."""

    value = "B"


class Child(ParentA, ParentB):
    """Child class."""

    pass


print(Child.value)

"""
Both parents contain value.

MRO:

    Child
      ↓
    ParentA
      ↓
    ParentB
      ↓
    object

Therefore:

    Child.value

returns:

    "A"
"""


# ============================================================
# 10. CHANGING PARENT ORDER CHANGES MRO
# ============================================================

class ParentA:
    """First parent."""

    value = "A"


class ParentB:
    """Second parent."""

    value = "B"


class Child(ParentB, ParentA):
    """Child class."""

    pass


print(Child.value)

"""
MRO:

    Child
      ↓
    ParentB
      ↓
    ParentA
      ↓
    object

Therefore:

    Child.value

returns:

    "B"
"""


# ============================================================
# 11. MRO WITH METHODS
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
    """Child class."""

    pass


child = Child()

child.show()

print(Child.__mro__)

"""
MRO determines which show() is selected.

ParentA appears before ParentB.

Therefore ParentA.show() executes.
"""


# ============================================================
# 12. CHILD OVERRIDE TAKES PRIORITY OVER BOTH PARENTS
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
    """Child class."""

    def show(self) -> None:
        print("Child")


child = Child()

child.show()

"""
MRO:

    Child
      ↓
    ParentA
      ↓
    ParentB
      ↓
    object

show() is found immediately in Child.
"""


# ============================================================
# 13. DIAMOND INHERITANCE
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
    """Bottom class."""

    pass


print(D.__mro__)

"""
The inheritance structure is:

             A
            / \
           B   C
            \ /
             D

This is called the diamond inheritance pattern.
"""


# ============================================================
# 14. DIAMOND MRO
# ============================================================

class A:
    """Top-level base class."""

    pass


class B(A):
    """First branch."""

    pass


class C(A):
    """Second branch."""

    pass


class D(B, C):
    """Bottom class."""

    pass


print(D.__mro__)

"""
The MRO is:

    D
    B
    C
    A
    object

Notice that A appears only once.

Python does not simply perform:

    D → B → A → C → A

because that would duplicate A and violate the inheritance
ordering rules.
"""


# ============================================================
# 15. DIAMOND INHERITANCE WITH A SHARED METHOD
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
    """Bottom class."""

    pass


d = D()

d.show()

"""
MRO:

    D
    B
    C
    A
    object

Neither D, B, nor C defines show().

Therefore Python eventually finds A.show().
"""


# ============================================================
# 16. MRO IS NOT SIMPLY DEPTH-FIRST SEARCH
# ============================================================

class A:
    """Top-level base class."""

    pass


class B(A):
    """First branch."""

    pass


class C(A):
    """Second branch."""

    pass


class D(B, C):
    """Bottom class."""

    pass


print(D.__mro__)

"""
A simple depth-first search might suggest:

    D → B → A → C

But Python's MRO is:

    D → B → C → A → object

Python must preserve important ordering constraints.

This is why Python uses C3 linearization.
"""


# ============================================================
# 17. C3 LINEARIZATION — THE BASIC IDEA
# ============================================================

"""
Python uses C3 linearization to calculate MRO.

The algorithm ensures that the resulting MRO preserves:

    1. Local precedence order
    2. Monotonicity
    3. Consistent inheritance ordering

You normally do not need to calculate the algorithm manually.

Python calculates it for you.

You can inspect the result using:

    Class.__mro__

or:

    Class.mro()
"""


# ============================================================
# 18. LOCAL PRECEDENCE ORDER
# ============================================================

class A:
    """First parent."""

    pass


class B:
    """Second parent."""

    pass


class C(A, B):
    """Child class."""

    pass


print(C.__mro__)

"""
Because C explicitly declares:

    class C(A, B):

A must appear before B in C's MRO.

This is called local precedence order.
"""


# ============================================================
# 19. MRO AND super()
# ============================================================

class Parent:
    """Parent class."""

    def show(self) -> None:
        print("Parent")


class Child(Parent):
    """Child class."""

    def show(self) -> None:
        print("Child")
        super().show()


child = Child()

child.show()

"""
Output:

    Child
    Parent

super() does not simply mean:

    "call my direct parent"

More accurately, it means:

    "continue method lookup from the next class in the MRO."

This becomes especially important with multiple inheritance.

A detailed treatment of super() comes in:

    08_super_function.py
"""


# ============================================================
# 20. super() FOLLOWS MRO
# ============================================================

class A:
    """Top-level class."""

    def show(self) -> None:
        print("A")


class B(A):
    """First class."""

    def show(self) -> None:
        print("B")
        super().show()


class C(B):
    """Second class."""

    def show(self) -> None:
        print("C")
        super().show()


c = C()

c.show()

"""
MRO:

    C
    B
    A
    object

Calling:

    C.show()

then:

    super().show()

continues to B.show()

which then continues to A.show().
"""


# ============================================================
# 21. MULTIPLE INHERITANCE AND super()
# ============================================================

class A:
    """First base class."""

    def show(self) -> None:
        print("A")


class B(A):
    """Second class."""

    def show(self) -> None:
        print("B")
        super().show()


class C(A):
    """Third class."""

    def show(self) -> None:
        print("C")
        super().show()


class D(B, C):
    """Bottom class."""

    def show(self) -> None:
        print("D")
        super().show()


print(D.__mro__)

d = D()

d.show()

"""
Typical MRO:

    D
    B
    C
    A
    object

Output:

    D
    B
    C
    A

This demonstrates why super() is more powerful than simply
calling a named parent class.
"""


# ============================================================
# 22. NAMED PARENT CALL VS super()
# ============================================================

class A:
    """Base class."""

    def show(self) -> None:
        print("A")


class B(A):
    """Intermediate class."""

    def show(self) -> None:
        print("B")
        A.show(self)


class C(B):
    """Child class."""

    def show(self) -> None:
        print("C")
        super().show()


c = C()

c.show()

"""
A.show(self) explicitly targets A.

super().show() follows the MRO.

These are not always equivalent.

This distinction becomes critical in cooperative multiple
inheritance.
"""


# ============================================================
# 23. INSPECTING MRO AS CLASS OBJECTS
# ============================================================

class Animal:
    """Base class."""

    pass


class Mammal(Animal):
    """Intermediate class."""

    pass


class Dog(Mammal):
    """Derived class."""

    pass


for class_object in Dog.__mro__:
    print(class_object)

"""
Each element of __mro__ is a class object.

The order represents Python's attribute and method lookup
sequence.
"""


# ============================================================
# 24. MRO CAN BE USED TO UNDERSTAND ATTRIBUTE CONFLICTS
# ============================================================

class A:
    """First parent."""

    value = "A"


class B(A):
    """Second class."""

    value = "B"


class C(A):
    """Third class."""

    value = "C"


class D(B, C):
    """Bottom class."""

    pass


print(D.__mro__)
print(D.value)

"""
MRO:

    D
    B
    C
    A
    object

D.value therefore resolves to:

    B.value
"""


# ============================================================
# 25. MRO AND INSTANCE ATTRIBUTES
# ============================================================

class Parent:
    """Parent class."""

    value = "Parent"


class Child(Parent):
    """Child class."""

    pass


child = Child()

child.value = "Instance"

print(child.value)
print(Child.__mro__)

"""
The MRO still exists, but the instance attribute is found
before class-level lookup.

Conceptually:

    child.value
        ↓
    child.__dict__
        ↓
    Child
        ↓
    Parent
        ↓
    object
"""


# ============================================================
# 26. MRO DOES NOT CHANGE INSTANCE ATTRIBUTE PRIORITY
# ============================================================

class A:
    """First parent."""

    value = "A"


class B(A):
    """Child class."""

    value = "B"


b = B()

b.value = "Instance"

print(b.value)

"""
Even though:

    B.value = "B"

the instance attribute wins:

    b.value = "Instance"
"""


# ============================================================
# 27. INVALID MRO EXAMPLE
# ============================================================

"""
Python can reject an inheritance structure if no consistent
MRO can be created.

For example, conceptually:

    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

is valid.

But certain combinations that create contradictory ordering
requirements can result in:

    TypeError: Cannot create a consistent method resolution
    order (MRO)

The important point is:

Python refuses to create a class when the inheritance
constraints cannot be satisfied consistently.
"""


# ============================================================
# 28. MRO AND object
# ============================================================

class Person:
    """Represent a person."""

    pass


print(Person.__mro__)

"""
A normal Python class ultimately inherits from object.

Therefore:

    Person
       ↓
    object
"""


# ============================================================
# 29. MRO IS CLASS-SPECIFIC
# ============================================================

class A:
    """Base class."""

    pass


class B(A):
    """Child."""

    pass


class C(A):
    """Child."""

    pass


class D(B, C):
    """Bottom class."""

    pass


print(B.__mro__)
print(C.__mro__)
print(D.__mro__)

"""
Each class has its own MRO.

B's MRO is different from C's.

D's MRO incorporates the inheritance structure of both.
"""


# ============================================================
# 30. PRACTICAL MRO DEBUGGING
# ============================================================

class Animal:
    """Base class."""

    def speak(self) -> None:
        print("Animal")


class Dog(Animal):
    """Child class."""

    def speak(self) -> None:
        print("Dog")


dog = Dog()

print(type(dog).__mro__)
dog.speak()

"""
When you are unsure why Python selected a particular method,
inspect:

    type(object).__mro__

Then look for the first class in the MRO that defines the
requested attribute.
"""


# ============================================================
# 31. FINDING WHERE AN ATTRIBUTE IS DEFINED
# ============================================================

class Animal:
    """Base class."""

    species = "Animal"


class Dog(Animal):
    """Child class."""

    pass


for class_object in Dog.__mro__:
    if "species" in class_object.__dict__:
        print(f"Found species in {class_object.__name__}")
        break

"""
This demonstrates the basic idea behind attribute lookup:

    Search each class in MRO order.

The first class containing the attribute wins.
"""


# ============================================================
# 32. METHOD LOOKUP CAN BE VISUALIZED
# ============================================================

class A:
    """Base class."""

    def show(self) -> None:
        print("A")


class B(A):
    """Intermediate class."""

    pass


class C(B):
    """Derived class."""

    pass


print("MRO:")

for class_object in C.__mro__:
    print(" ->", class_object.__name__)

"""
The lookup path is:

    C
     ↓
    B
     ↓
    A
     ↓
    object
"""


# ============================================================
# 33. KEY TAKEAWAY
# ============================================================

"""
Method Resolution Order (MRO) is the order Python uses to
search classes for attributes and methods.

For:

    class Dog(Animal):
        ...


the MRO is:

    Dog
    Animal
    object


For:

    class D(B, C):
        ...


Python calculates a consistent MRO, commonly:

    D
    B
    C
    A
    object

in a diamond inheritance structure.

You can inspect MRO using:

    Class.__mro__

or:

    Class.mro()


Most important rule:

    Python searches the MRO from left to right
    and uses the first matching attribute/method.

For multiple inheritance:

    class Child(ParentA, ParentB):
        ...

ParentA has precedence over ParentB when both provide
the same attribute and no more-specific class overrides it.

Also remember:

    super()

follows the MRO.

It does not simply mean "call my parent".

This distinction becomes extremely important when working
with multiple inheritance.
"""