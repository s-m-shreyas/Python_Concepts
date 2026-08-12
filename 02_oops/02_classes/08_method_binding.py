# type: ignore
"""
08_method_binding.py

Demonstrates method binding in Python.

Method binding explains how Python connects a method to an
object when the method is accessed.

The three important cases are:

    - instance methods
    - class methods
    - static methods

For instance methods, Python binds the current instance to
the method as self.

For class methods, Python binds the current class to the
method as cls.

For static methods, Python does not automatically bind either
an instance or a class.
"""


# ============================================================
# 1. INSTANCE METHOD
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        """Display a greeting."""
        print("Hello!")


person = Person()

person.greet()


# ============================================================
# 2. INSTANCE METHOD IS BOUND TO THE INSTANCE
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        """Display a greeting."""
        print(f"Hello from {self}.")


person = Person()

bound_method = person.greet

print(bound_method)

bound_method()


# ============================================================
# 3. ACCESSING THE METHOD THROUGH THE CLASS
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        """Display a greeting."""
        print(f"Hello from {self}.")


person = Person()

class_method = Person.greet

print(class_method)


# ============================================================
# 4. CLASS ACCESS DOES NOT AUTOMATICALLY BIND self
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        """Display a greeting."""
        print(f"Hello from {self}.")


person = Person()

Person.greet(person)


"""
When accessed through the class:

    Person.greet

Python gives us the underlying function without an instance
already being attached to it.

Therefore we explicitly provide the instance:

    Person.greet(person)
"""


# ============================================================
# 5. INSTANCE ACCESS DOES THE BINDING AUTOMATICALLY
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        """Display a greeting."""
        print(f"Hello from {self}.")


person = Person()

person.greet()


"""
Conceptually:

    person.greet()

is equivalent to:

    Person.greet(person)


The important difference is that Python supplies person
automatically when the method is accessed through the instance.
"""


# ============================================================
# 6. BOUND METHOD STORES THE INSTANCE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> None:
        """Display a greeting."""
        print(f"Hello, {self.name}.")


alice = Person("Alice")

greet_method = alice.greet

greet_method()


"""
The bound method remembers:

    function → Person.greet
    instance → alice

So calling:

    greet_method()

already knows which object should become self.
"""


# ============================================================
# 7. DIFFERENT INSTANCES CREATE DIFFERENT BOUND METHODS
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> None:
        """Display a greeting."""
        print(f"Hello, {self.name}.")


alice = Person("Alice")
bob = Person("Bob")

alice_greet = alice.greet
bob_greet = bob.greet

alice_greet()
bob_greet()


"""
The method implementation is the same:

    Person.greet

But the bound instances are different:

    alice_greet → alice
    bob_greet   → bob
"""


# ============================================================
# 8. METHOD BINDING DOES NOT CREATE A NEW INSTANCE
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        """Display a greeting."""
        print("Hello!")


person = Person()

greet_method = person.greet

print(person is person)

greet_method()


"""
Accessing:

    person.greet

does not create another Person instance.

The existing instance is simply associated with the method.
"""


# ============================================================
# 9. INSTANCE METHOD AS A FUNCTION
# ============================================================

class Calculator:
    """Provide calculation operations."""

    def add(self, first: int, second: int) -> int:
        """Return the sum."""
        return first + second


calculator = Calculator()

result_one = calculator.add(10, 20)
result_two = Calculator.add(calculator, 10, 20)

print(result_one)
print(result_two)


"""
These two calls produce the same result:

    calculator.add(10, 20)

    Calculator.add(calculator, 10, 20)

The first uses automatic binding.

The second explicitly supplies the instance.
"""


# ============================================================
# 10. BOUND METHOD VS UNBOUND FUNCTION
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        """Display a greeting."""
        print("Hello!")


person = Person()

bound_method = person.greet
unbound_function = Person.greet

print(bound_method)
print(unbound_function)


"""
Conceptually:

    person.greet
        ↓
    bound method

    Person.greet
        ↓
    function requiring an instance
"""


# ============================================================
# 11. CLASS METHODS ARE ALSO BOUND
# ============================================================

class Person:
    """Represent a person."""

    @classmethod
    def show_class(cls) -> None:
        """Display the current class."""
        print(cls.__name__)


bound_class_method = Person.show_class

bound_class_method()


"""
A class method is automatically bound to the class.

Conceptually:

    Person.show_class()

provides:

    cls = Person
"""


# ============================================================
# 12. CLASS METHOD BINDING THROUGH A SUBCLASS
# ============================================================

class Person:
    """Represent a person."""

    @classmethod
    def show_class(cls) -> None:
        """Display the current class."""
        print(cls.__name__)


class Employee(Person):
    """Represent an employee."""

    pass


Person.show_class()
Employee.show_class()


"""
When accessed through Person:

    cls → Person

When accessed through Employee:

    cls → Employee
"""


# ============================================================
# 13. STATIC METHODS ARE NOT BOUND
# ============================================================

class Calculator:
    """Provide calculation utilities."""

    @staticmethod
    def add(first: int, second: int) -> int:
        """Return the sum."""
        return first + second


calculator = Calculator()

class_access = Calculator.add
instance_access = calculator.add

print(class_access(10, 20))
print(instance_access(10, 20))


"""
Both accesses simply provide the same underlying function.

No instance is automatically supplied.

No class is automatically supplied.
"""


# ============================================================
# 14. THREE METHOD BINDING BEHAVIORS
# ============================================================

"""
Instance method:

    person.greet()

        ↓

    Person.greet(person)

        self → person


Class method:

    Person.show_class()

        ↓

    class method receives Person

        cls → Person


Static method:

    Calculator.add(10, 20)

        ↓

    ordinary function call

        no self
        no cls
"""


# ============================================================
# 15. BOUND METHOD REMEMBERS ITS INSTANCE
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def display(self) -> None:
        """Display the person's name."""
        print(self.name)


person = Person("Alice")

display_method = person.display

display_method()


"""
The bound method retains access to:

    person

Therefore self inside display() refers to:

    person
"""


# ============================================================
# 16. BOUND METHODS CAN BE STORED IN VARIABLES
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> None:
        """Display a greeting."""
        print(f"Hello, {self.name}.")


person = Person("Alice")

greeting = person.greet

greeting()


"""
This is possible because methods are objects in Python.

The bound method can be stored and called later.
"""


# ============================================================
# 17. BOUND METHODS CAN BE PASSED TO FUNCTIONS
# ============================================================

class Person:
    """Represent a person."""

    def greet(self) -> None:
        """Display a greeting."""
        print("Hello!")


def execute_action(action: callable) -> None:
    """Execute a supplied callable."""
    action()


person = Person()

execute_action(person.greet)


"""
person.greet is already bound to person.

Therefore execute_action does not need to know anything
about self.
"""


# ============================================================
# 18. METHOD BINDING AND INSTANCE STATE
# ============================================================

class Counter:
    """Represent a counter."""

    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        """Increase the counter."""
        self.value += 1

    def display(self) -> None:
        """Display the counter."""
        print(self.value)


counter = Counter()

increment = counter.increment
display = counter.display

increment()
increment()

display()


"""
Both bound methods remember the same instance:

    increment → counter
    display   → counter

Therefore both operate on the same instance state.
"""


# ============================================================
# 19. SAME METHOD, DIFFERENT BINDINGS
# ============================================================

class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name

    def display(self) -> None:
        """Display the person's name."""
        print(self.name)


alice = Person("Alice")
bob = Person("Bob")

alice_display = alice.display
bob_display = bob.display

alice_display()
bob_display()


"""
Same function:

    Person.display

Different bindings:

    alice_display → Alice
    bob_display   → Bob
"""


# ============================================================
# 20. METHOD BINDING EXPLAINS self
# ============================================================

"""
This is the deeper reason self works.

When you write:

    person.greet()

Python finds the greet method on Person and binds
the person instance to it.

Therefore inside the method:

    self

refers to:

    person


So self is not magically created inside the method.

It is the parameter that receives the instance supplied
through method binding.
"""


# ============================================================
# 21. METHOD BINDING EXPLAINS cls
# ============================================================

"""
The same idea applies to class methods.

For:

    Person.show_class()

Python binds the class:

    Person

to the class method.

Therefore:

    cls

refers to:

    Person
"""


# ============================================================
# 22. STATIC METHODS BREAK AUTOMATIC BINDING
# ============================================================

"""
A static method does not receive automatic binding.

For:

    Calculator.add

Python does not attach:

    self

or:

    cls

The result behaves like a normal function stored inside
the class namespace.
"""


# ============================================================
# 23. COMPARING THE THREE
# ============================================================

class Example:
    """Demonstrate all three method types."""

    def instance_method(self) -> None:
        """Demonstrate instance method."""
        print(f"Instance: {self}")

    @classmethod
    def class_method(cls) -> None:
        """Demonstrate class method."""
        print(f"Class: {cls}")

    @staticmethod
    def static_method() -> None:
        """Demonstrate static method."""
        print("No automatic object or class binding.")


example = Example()

example.instance_method()
Example.class_method()
Example.static_method()


# ============================================================
# 24. METHOD BINDING AND DOT NOTATION
# ============================================================

"""
The dot operator is important.

When Python evaluates:

    object.method

it performs attribute lookup and, for a normal instance
method, creates a bound method associated with that object.

Therefore:

    object.method()

can be understood conceptually as:

    Class.method(object)


This is why the first parameter of an instance method receives
the current object.
"""


# ============================================================
# 25. KEY TAKEAWAY
# ============================================================

"""
Method binding explains how Python supplies self or cls.

Instance method:

    class Example:

        def method(self):
            ...


    example.method()

    ↓

    Example.method(example)

    self → example


Class method:

    class Example:

        @classmethod
        def method(cls):
            ...


    Example.method()

    ↓

    cls → Example


Static method:

    class Example:

        @staticmethod
        def method():
            ...


    Example.method()

    ↓

    no automatic self
    no automatic cls


The central idea:

    Instance method
        → bound to an instance

    Class method
        → bound to a class

    Static method
        → not automatically bound


This binding behavior is the mechanism behind the
self and cls parameters.
"""