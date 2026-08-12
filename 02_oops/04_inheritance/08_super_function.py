# type: ignore

"""
08_super_function.py

Demonstrates the super() function in Python.

super() provides access to the next class in the Method
Resolution Order (MRO).

This file focuses on:

    - Basic super()
    - Calling inherited methods
    - Calling parent __init__()
    - Extending parent behaviour
    - super() vs explicit parent calls
    - super() without arguments
    - super() with arguments
    - super() and multiple inheritance
    - Cooperative multiple inheritance
    - super() following MRO
"""


# ============================================================
# 1. BASIC super()
# ============================================================

class Parent:
    """Represent a parent class."""

    def show(self) -> None:
        print("Parent.show()")


class Child(Parent):
    """Represent a child class."""

    def show(self) -> None:
        print("Child.show()")
        super().show()


child = Child()

child.show()

"""
Output:

    Child.show()
    Parent.show()

super().show() accesses the next implementation of show()
according to the MRO.
"""


# ============================================================
# 2. super() DOES NOT CREATE A NEW OBJECT
# ============================================================

class Parent:
    """Represent a parent class."""

    def show(self) -> None:
        print("Parent.show()")


class Child(Parent):
    """Represent a child class."""

    def show(self) -> None:
        print("Child.show()")
        super().show()


child = Child()

print(child)

child.show()

"""
super() does not create another Child or Parent object.

It provides a proxy for accessing the next class in the
current MRO.
"""


# ============================================================
# 3. super() WITH __init__()
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


class Student(Person):
    """Represent a student."""

    def __init__(self, name: str, grade: int) -> None:
        super().__init__(name)
        self.grade = grade


student = Student("Alice", 90)

print(student.__dict__)

"""
Student.__init__() delegates the name initialization to
Person.__init__().

Student then performs its own initialization for grade.

Result:

    {
        "name": "Alice",
        "grade": 90
    }
"""


# ============================================================
# 4. WHY super() IS USEFUL WITH __init__()
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


class Employee(Person):
    """Represent an employee."""

    def __init__(self, name: str, employee_id: int) -> None:
        super().__init__(name)
        self.employee_id = employee_id


employee = Employee("Bob", 101)

print(employee.name)
print(employee.employee_id)

"""
Without super(), Employee would need to duplicate the logic
for initializing name.

super() allows Employee to reuse Person's initialization.
"""


# ============================================================
# 5. super() CAN EXTEND PARENT BEHAVIOUR
# ============================================================

class Animal:
    """Represent an animal."""

    def speak(self) -> None:
        print("Animal makes a sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> None:
        super().speak()
        print("Dog barks.")


dog = Dog()

dog.speak()

"""
The child does not completely replace the parent behaviour.

It extends it:

    1. Parent behaviour
    2. Child behaviour
"""


# ============================================================
# 6. super() CAN BE USED WITH OTHER METHODS
# ============================================================

class Parent:
    """Parent class."""

    def describe(self) -> None:
        print("Parent description.")


class Child(Parent):
    """Child class."""

    def describe(self) -> None:
        super().describe()
        print("Child description.")


child = Child()

child.describe()

"""
super() can be used with any inherited method, not only
__init__().
"""


# ============================================================
# 7. super() VS EXPLICIT PARENT CLASS CALL
# ============================================================

class Parent:
    """Parent class."""

    def show(self) -> None:
        print("Parent")


class Child(Parent):
    """Child class."""

    def show(self) -> None:
        Parent.show(self)


child = Child()

child.show()

"""
This explicitly calls Parent.show().

It works, but it directly names the parent class.
"""


# ============================================================
# 8. THE super() VERSION
# ============================================================

class Parent:
    """Parent class."""

    def show(self) -> None:
        print("Parent")


class Child(Parent):
    """Child class."""

    def show(self) -> None:
        super().show()


child = Child()

child.show()

"""
This uses super() instead of explicitly naming Parent.

The important difference becomes visible with multiple
inheritance.
"""


# ============================================================
# 9. super() FOLLOWS THE MRO
# ============================================================

class A:
    """Base class."""

    def show(self) -> None:
        print("A")


class B(A):
    """Intermediate class."""

    def show(self) -> None:
        print("B")
        super().show()


class C(B):
    """Derived class."""

    def show(self) -> None:
        print("C")
        super().show()


print(C.__mro__)

c = C()

c.show()

"""
MRO:

    C
    B
    A
    object

Execution:

    C.show()
        ↓
    B.show()
        ↓
    A.show()
"""


# ============================================================
# 10. super() IS NOT SIMPLY "PARENT"
# ============================================================

class A:
    """Base class."""

    def show(self) -> None:
        print("A")


class B(A):
    """Intermediate class."""

    def show(self) -> None:
        print("B")
        super().show()


class C(B):
    """Derived class."""

    def show(self) -> None:
        print("C")
        super().show()


c = C()

c.show()

"""
A common beginner explanation is:

    super() means parent.

A more accurate explanation is:

    super() continues attribute lookup from the next class
    in the MRO.

This distinction is especially important in multiple
inheritance.
"""


# ============================================================
# 11. MULTIPLE INHERITANCE
# ============================================================

class A:
    """First base class."""

    def show(self) -> None:
        print("A")


class B:
    """Second base class."""

    def show(self) -> None:
        print("B")


class C(A, B):
    """Child class."""

    def show(self) -> None:
        print("C")
        super().show()


print(C.__mro__)

c = C()

c.show()

"""
MRO:

    C
    A
    B
    object

super() from C reaches A.show().
"""


# ============================================================
# 12. super() CAN CONTINUE THROUGH MULTIPLE PARENTS
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

Execution:

    D
    B
    C
    A

This is one of the most important use cases for super().
"""


# ============================================================
# 13. EXPLICIT PARENT CALL CAN BREAK THE CHAIN
# ============================================================

class A:
    """Base class."""

    def show(self) -> None:
        print("A")


class B(A):
    """First branch."""

    def show(self) -> None:
        print("B")
        A.show(self)


class C(A):
    """Second branch."""

    def show(self) -> None:
        print("C")
        A.show(self)


class D(B, C):
    """Bottom class."""

    def show(self) -> None:
        print("D")
        super().show()


print(D.__mro__)

d = D()

d.show()

"""
Output:

    D
    B
    A

C is skipped.

Why?

B explicitly says:

    A.show(self)

It jumps directly to A instead of continuing through
the MRO.

This is one reason cooperative multiple inheritance
uses super().
"""


# ============================================================
# 14. COOPERATIVE MULTIPLE INHERITANCE
# ============================================================

class A:
    """Base class."""

    def show(self) -> None:
        print("A")


class B(A):
    """First branch."""

    def show(self) -> None:
        print("B")
        super().show()


class C(A):
    """Second branch."""

    def show(self) -> None:
        print("C")
        super().show()


class D(B, C):
    """Bottom class."""

    def show(self) -> None:
        print("D")
        super().show()


d = D()

d.show()

"""
Every class cooperates by calling super().

MRO:

    D
    B
    C
    A
    object

Result:

    D
    B
    C
    A
"""


# ============================================================
# 15. super() WITH MULTIPLE INHERITANCE AND __init__()
# ============================================================

class Person:
    """Base class."""

    def __init__(self, name: str) -> None:
        self.name = name


class Employee(Person):
    """Employee class."""

    def __init__(self, name: str, employee_id: int) -> None:
        super().__init__(name)
        self.employee_id = employee_id


employee = Employee("Alice", 101)

print(employee.__dict__)

"""
Employee.__init__() uses super() to delegate name
initialization to Person.__init__().
"""


# ============================================================
# 16. super() WITH NO ARGUMENTS
# ============================================================

class Parent:
    """Parent class."""

    def show(self) -> None:
        print("Parent")


class Child(Parent):
    """Child class."""

    def show(self) -> None:
        super().show()


child = Child()

child.show()

"""
Inside an instance method, Python automatically determines
the current class and instance for:

    super()

So:

    super().show()

is the modern and preferred form.
"""


# ============================================================
# 17. THE LONG FORM OF super()
# ============================================================

class Parent:
    """Parent class."""

    def show(self) -> None:
        print("Parent")


class Child(Parent):
    """Child class."""

    def show(self) -> None:
        super(Child, self).show()


child = Child()

child.show()

"""
The explicit form is:

    super(Child, self)

The modern form:

    super()

is preferred inside normal class methods.

The two forms perform the same basic operation here.
"""


# ============================================================
# 18. super() WITH A DIFFERENT STARTING CLASS
# ============================================================

class A:
    """Base class."""

    def show(self) -> None:
        print("A")


class B(A):
    """Intermediate class."""

    def show(self) -> None:
        print("B")


class C(B):
    """Derived class."""

    def show(self) -> None:
        super().show()


c = C()

c.show()

"""
Inside C.show():

    super()

starts lookup after C in the MRO.

MRO:

    C
    B
    A
    object

Therefore B.show() executes.
"""


# ============================================================
# 19. super() IS A PROXY OBJECT
# ============================================================

class Parent:
    """Parent class."""

    def show(self) -> None:
        print("Parent")


class Child(Parent):
    """Child class."""

    def show(self) -> None:
        parent_proxy = super()
        parent_proxy.show()


child = Child()

child.show()

"""
super() produces a proxy object that provides access to
attributes found after the current class in the MRO.

Normally you simply write:

    super().show()

instead of storing the proxy.
"""


# ============================================================
# 20. super() CAN ACCESS ATTRIBUTES
# ============================================================

class Parent:
    """Parent class."""

    value = "Parent"


class Child(Parent):
    """Child class."""

    value = "Child"

    def show_parent_value(self) -> None:
        print(super().value)


child = Child()

print(child.value)
child.show_parent_value()

"""
child.value:

    "Child"

super().value:

    "Parent"

super() allows access to the next matching attribute in
the MRO.
"""


# ============================================================
# 21. super() DOES NOT MEAN "USE THE PARENT'S ATTRIBUTE"
#     IN GENERAL
# ============================================================

class A:
    """Base class."""

    value = "A"


class B(A):
    """Intermediate class."""

    value = "B"


class C(B):
    """Derived class."""

    value = "C"

    def show(self) -> None:
        print(super().value)


c = C()

c.show()

"""
C.show() uses:

    super().value

The lookup starts after C.

Therefore it finds B.value.

If B did not contain value, lookup would continue to A.
"""


# ============================================================
# 22. super() CAN CALL A CLASS METHOD
# ============================================================

class Parent:
    """Parent class."""

    @classmethod
    def describe(cls) -> None:
        print(cls.__name__)


class Child(Parent):
    """Child class."""

    @classmethod
    def describe(cls) -> None:
        super().describe()


Child.describe()

"""
super() can also be used inside class methods.

Here the inherited class method receives the appropriate
class according to normal class-method binding.
"""


# ============================================================
# 23. super() CAN CALL A STATIC METHOD
# ============================================================

class Parent:
    """Parent class."""

    @staticmethod
    def utility() -> None:
        print("Parent utility")


class Child(Parent):
    """Child class."""

    @staticmethod
    def utility() -> None:
        super(Child, Child).utility()


Child.utility()

"""
Static methods do not automatically receive self or cls.

Therefore the explicit super() form is used here.

In normal code, simply inheriting the static method is often
more appropriate if no extension is required.
"""


# ============================================================
# 24. super() AND METHOD OVERRIDING
# ============================================================

class Animal:
    """Base class."""

    def speak(self) -> None:
        print("Generic sound")


class Dog(Animal):
    """Child class."""

    def speak(self) -> None:
        super().speak()
        print("Bark")


dog = Dog()

dog.speak()

"""
Overriding does not prevent the child from reusing the parent
implementation.

The child can combine:

    inherited behaviour
    +
    specialized behaviour
"""


# ============================================================
# 25. super() AND ATTRIBUTE INITIALIZATION
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


class Employee(Person):
    """Represent an employee."""

    def __init__(self, name: str, employee_id: int) -> None:
        super().__init__(name)
        self.employee_id = employee_id


employee = Employee("Bob", 101)

print(employee.__dict__)

"""
Parent:

    name

Child:

    employee_id

super() allows both initialization responsibilities to
participate in constructing the same object.
"""


# ============================================================
# 26. MULTIPLE INHERITANCE WITH COOPERATIVE __init__()
# ============================================================

class A:
    """First class."""

    def __init__(self) -> None:
        print("A.__init__")


class B(A):
    """Second class."""

    def __init__(self) -> None:
        print("B.__init__")
        super().__init__()


class C(A):
    """Third class."""

    def __init__(self) -> None:
        print("C.__init__")
        super().__init__()


class D(B, C):
    """Bottom class."""

    def __init__(self) -> None:
        print("D.__init__")
        super().__init__()


print(D.__mro__)

D()

"""
MRO:

    D
    B
    C
    A
    object

Output:

    D.__init__
    B.__init__
    C.__init__
    A.__init__

Each class calls super(), allowing the entire MRO to
participate.
"""


# ============================================================
# 27. WHY super() IS IMPORTANT IN MULTIPLE INHERITANCE
# ============================================================

"""
Consider:

    class D(B, C):
        ...

If B explicitly calls:

    A.method(self)

then C may never get a chance to participate.

If B instead calls:

    super().method()

Python continues according to the MRO.

This allows classes to cooperate rather than hard-code
specific parent classes.
"""


# ============================================================
# 28. super() AND MRO SHOULD BE UNDERSTOOD TOGETHER
# ============================================================

class A:
    """Base class."""

    def show(self) -> None:
        print("A")


class B(A):
    """First branch."""

    def show(self) -> None:
        print("B")
        super().show()


class C(A):
    """Second branch."""

    def show(self) -> None:
        print("C")
        super().show()


class D(B, C):
    """Bottom class."""

    def show(self) -> None:
        print("D")
        super().show()


print("MRO:")

for class_object in D.__mro__:
    print(class_object.__name__)

print("\nExecution:")

D().show()

"""
The MRO determines where super() goes next.

MRO:

    D
    B
    C
    A
    object

Execution:

    D
    B
    C
    A
"""


# ============================================================
# 29. COMMON MISTAKE — THINKING super() RETURNS THE PARENT
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

    def show(self) -> None:
        print("C")
        super().show()


c = C()

c.show()

"""
super() from C starts after C in C's MRO.

MRO:

    C
    B
    A
    object

Therefore super().show() finds B.show().

B does not define show(), so lookup continues to A.show().

Therefore A.show() executes.

This is why "super() = parent" is an incomplete explanation.
"""


# ============================================================
# 30. KEY TAKEAWAY
# ============================================================

"""
The most important concept:

    super()
        ↓
    continues attribute lookup
        ↓
    from the next class in the MRO


It is commonly used to:

    1. Reuse parent initialization

        super().__init__(...)


    2. Extend inherited methods

        super().method()


    3. Support cooperative multiple inheritance


Example:

    class Parent:
        def show(self):
            print("Parent")


    class Child(Parent):
        def show(self):
            print("Child")
            super().show()


The result is:

    Child
    Parent


But with multiple inheritance:

    class A:
        def show(self):
            print("A")


    class B(A):
        def show(self):
            print("B")
            super().show()


    class C(A):
        def show(self):
            print("C")
            super().show()


    class D(B, C):
        def show(self):
            print("D")
            super().show()


MRO:

    D
    B
    C
    A
    object


Execution:

    D
    B
    C
    A


This is the real power of super():

    It follows the MRO rather than hard-coding a particular
    parent class.
"""