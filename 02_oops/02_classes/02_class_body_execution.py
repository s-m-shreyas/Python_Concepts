# type: ignore
"""
02_class_body_execution.py

Explains how Python executes a class body.

This file focuses on:

    - The class body as executable code
    - Execution order inside a class body
    - Names created during class-body execution
    - Class namespace creation
    - Expressions evaluated inside the class body
    - Class attributes created during execution
    - Functions created during class-body execution
    - The relationship between class-body execution and the
      resulting class object

Class definition syntax was covered in:

    01_class_definition.py

Object creation is covered separately in:

    03_object_creation.py
"""


# ============================================================
# 1. A CLASS BODY IS EXECUTED
# ============================================================

"""
A common beginner misconception is that the class body is
merely a static blueprint.

In Python, the class body is actually executed when the class
definition is processed.
"""


print("Before class definition")


class Person:
    """Represent a person."""

    print("Inside class body")


print("After class definition")


# ============================================================
# 2. CLASS BODY EXECUTION HAPPENS IN ORDER
# ============================================================

"""
Statements inside the class body execute from top to bottom,
just like statements in other Python scopes.
"""


class Example:
    """Demonstrate class-body execution order."""

    print("First")

    value = 10

    print("Second")

    value = 20

    print("Third")


print(Example.value)


# ============================================================
# 3. EXPRESSIONS IN THE CLASS BODY ARE EVALUATED
# ============================================================

"""
Expressions written inside the class body are evaluated while
the class body is being executed.
"""


class Calculation:
    """Demonstrate class-body expression evaluation."""

    first = 10
    second = 20
    total = first + second


print(Calculation.total)


# ============================================================
# 4. CLASS ATTRIBUTES ARE CREATED DURING CLASS-BODY EXECUTION
# ============================================================

"""
When Python executes:

    value = 100

inside the class body, the name 'value' becomes part of the
namespace being used to construct the class.
"""


class Example:
    """Demonstrate class-body namespace creation."""

    value = 100


print(Example.value)


# ============================================================
# 5. MULTIPLE NAMES CAN BE CREATED
# ============================================================

"""
The class body can create multiple names.
"""


class Product:
    """Represent product information."""

    name = "Laptop"
    category = "Electronics"
    price = 75000.0


print(Product.name)
print(Product.category)
print(Product.price)


# ============================================================
# 6. CLASS BODY CAN USE PREVIOUSLY DEFINED NAMES
# ============================================================

"""
Names created earlier in the class body can be used by later
statements in that same class body.
"""


class Rectangle:
    """Represent rectangle dimensions."""

    length = 10
    width = 5
    area = length * width


print(Rectangle.area)


# ============================================================
# 7. CLASS BODY EXECUTION IS TOP-TO-BOTTOM
# ============================================================

"""
A name generally needs to exist before it can be referenced
by later class-body code.
"""


class Example:
    """Demonstrate top-to-bottom execution."""

    first = 10
    second = first + 5
    third = second + 5


print(Example.first)
print(Example.second)
print(Example.third)


# ============================================================
# 8. FUNCTIONS ARE CREATED DURING CLASS-BODY EXECUTION
# ============================================================

"""
A def statement inside the class body creates a function
object and binds its name in the class namespace.

At this stage, it is useful to think of the function as being
created during execution of the class body.
"""


class Person:
    """Represent a person."""

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


print(Person.greet)


# ============================================================
# 9. CLASS BODY CAN EXECUTE FUNCTION CALLS
# ============================================================

"""
The class body can call functions just like ordinary Python
code.
"""


def create_message() -> str:
    """Return a message."""
    return "Class body executed."


class Example:
    """Demonstrate function calls during class creation."""

    message = create_message()


print(Example.message)


# ============================================================
# 10. CLASS BODY CAN USE IMPORTS
# ============================================================

"""
Import statements can also appear inside a class body.

The imported name becomes part of the class namespace.

This is technically valid, although imports are normally
placed at module level.
"""


class Example:
    """Demonstrate a class-body import."""

    import math

    number = math.sqrt(25)


print(Example.number)


# ============================================================
# 11. CLASS BODY CAN CONTAIN CONDITIONAL STATEMENTS
# ============================================================

"""
Because the class body is executable code, control-flow
statements such as if can appear inside it.
"""


DEBUG_MODE = True


class Configuration:
    """Demonstrate conditional class-body execution."""

    if DEBUG_MODE:
        environment = "development"
    else:
        environment = "production"


print(Configuration.environment)


# ============================================================
# 12. CLASS BODY CAN CONTAIN LOOPS
# ============================================================

"""
Loops can also technically appear inside a class body.

The loop executes while the class body is being evaluated.
"""


class Numbers:
    """Demonstrate a loop inside a class body."""

    values: list[int] = []

    for number in range(1, 4):
        values.append(number)


print(Numbers.values)


# ============================================================
# 13. CLASS BODY CAN CREATE DERIVED VALUES
# ============================================================

"""
Class-level data can be calculated during class-body execution.
"""


class Circle:
    """Store circle-related class data."""

    radius = 10
    diameter = radius * 2


print(Circle.radius)
print(Circle.diameter)


# ============================================================
# 14. CLASS BODY CAN CALL METHODS OR FUNCTIONS DEFINED EARLIER
# ============================================================

"""
A function defined earlier in the class body can technically
be referenced later in the class body.

However, calling such functions during class creation can be
confusing for beginners, so this example is kept simple.
"""


class Calculator:
    """Demonstrate class-body function usage."""

    @staticmethod
    def add(first: int, second: int) -> int:
        """Return the sum."""
        return first + second

    result = add(10, 20)


print(Calculator.result)


# ============================================================
# 15. CLASS BODY HAS ITS OWN EXECUTION CONTEXT
# ============================================================

"""
The class body is executed in a namespace associated with the
class being created.

Names assigned in the body become candidates for the resulting
class namespace.
"""


class Example:
    """Demonstrate class-body names."""

    first = 10
    second = 20


print(Example.__dict__["first"])
print(Example.__dict__["second"])


# ============================================================
# 16. LOCAL NAMES CREATED IN THE CLASS BODY
# ============================================================

"""
Names created during class-body execution generally become
entries in the class namespace.

This is different from a function body, where local variables
belong to a function invocation.
"""


class Example:
    """Demonstrate names created in a class body."""

    value = 100


print(Example.__dict__)


# ============================================================
# 17. CLASS BODY EXECUTION IS NOT INSTANCE CREATION
# ============================================================

"""
The class body executes when the class itself is defined.

It does NOT execute again simply because an instance is
created.

This distinction is extremely important.
"""


class Person:
    """Demonstrate class-body execution."""

    print("Class body executed")


print("Creating first instance")
first = Person()

print("Creating second instance")
second = Person()


# ============================================================
# 18. CLASS BODY EXECUTES ONCE DURING CLASS CREATION
# ============================================================

"""
In the normal case, the class body executes when the class is
created.

Creating multiple instances does not re-execute the class
body.
"""


class Counter:
    """Demonstrate class-body execution frequency."""

    print("Class body is executing")

    value = 100


first = Counter()
second = Counter()
third = Counter()

print(Counter.value)


# ============================================================
# 19. __init__ DOES NOT EXECUTE DURING CLASS DEFINITION
# ============================================================

"""
The __init__ method is merely defined when the class body is
executed.

Its code runs when an instance is created, not when the class
itself is defined.

Object creation and __init__ are covered more thoroughly in
03_object_creation.py.
"""


class Person:
    """Represent a person."""

    def __init__(self) -> None:
        print("__init__ executed")


print("Class has been defined")

person = Person()


# ============================================================
# 20. FUNCTION DEFINITION VS FUNCTION EXECUTION
# ============================================================

"""
The same distinction applies to ordinary methods.

When Python encounters:

    def greet(...):

during class-body execution, it creates the function object.

The function body itself does not execute at that moment.
"""


class Person:
    """Represent a person."""

    def greet(self) -> str:
        print("greet body executed")
        return "Hello"


print("Class defined")

person = Person()

print("Calling greet")

message = person.greet()

print(message)


# ============================================================
# 21. CLASS BODY CAN REFER TO GLOBAL NAMES
# ============================================================

"""
The class body can access names from the surrounding module
scope when evaluating expressions.
"""


company_name = "ABC"


class Employee:
    """Represent an employee."""

    company = company_name


print(Employee.company)


# ============================================================
# 22. CLASS BODY CAN CREATE NAMES BASED ON GLOBAL DATA
# ============================================================

"""
Global values can therefore participate in class-body
execution.
"""


default_port = 8080


class Server:
    """Represent server configuration."""

    port = default_port


print(Server.port)


# ============================================================
# 23. CLASS BODY AND FUNCTION SCOPE ARE DIFFERENT
# ============================================================

"""
A class body does not behave exactly like a function body.

For example, class-level names can become class attributes and
can be accessed through the resulting class.
"""


class Example:
    """Demonstrate class-level names."""

    value = 100


print(Example.value)


# ============================================================
# 24. A FUNCTION DEFINED INSIDE A CLASS DOES NOT AUTOMATICALLY
#     EXECUTE
# ============================================================

"""
Defining a method creates the function object.

The method body runs only when the method is called.
"""


class Example:
    """Demonstrate method definition."""

    def show(self) -> str:
        print("Method body executed")
        return "Done"


print("Class definition complete")

example = Example()

print("Calling method")

result = example.show()

print(result)


# ============================================================
# 25. CLASS BODY CAN CREATE DATA STRUCTURES
# ============================================================

"""
Class-body execution can create lists, dictionaries, sets,
and other objects.
"""


class Configuration:
    """Store configuration data."""

    supported_formats = ["CSV", "JSON", "XML"]

    default_options = {
        "debug": False,
        "timeout": 30,
    }


print(Configuration.supported_formats)
print(Configuration.default_options)


# ============================================================
# 26. CLASS BODY CAN USE COMPREHENSIONS
# ============================================================

"""
Comprehensions can also be evaluated during class-body
execution.

The comprehension creates an object which can then become a
class attribute.
"""


class Numbers:
    """Store generated numbers."""

    squares = [number * number for number in range(1, 6)]


print(Numbers.squares)


# ============================================================
# 27. CLASS BODY CAN CONTAIN COMMENTS
# ============================================================

"""
Comments inside a class body are ignored by Python just like
comments elsewhere.
"""


class Person:
    """Represent a person."""

    # Shared class-level information.
    species = "Human"


print(Person.species)


# ============================================================
# 28. CLASS BODY CAN CONTAIN DOCSTRINGS
# ============================================================

"""
The first string expression in a class body becomes the
class's docstring.
"""


class Person:
    """Represent a human being."""

    pass


print(Person.__doc__)


# ============================================================
# 29. CLASS BODY CREATES THE CLASS NAMESPACE
# ============================================================

"""
Conceptually, the process can be viewed as:

    1. Python encounters the class statement.
    2. A namespace is prepared for the class body.
    3. The class body is executed.
    4. Names created during execution are collected.
    5. The class object is created.
    6. The class name refers to that class object.

This is a simplified conceptual model.

The actual class creation process involves the metaclass
mechanism, which is covered much later.
"""


class Person:
    """Represent a person."""

    species = "Human"

    def greet(self) -> str:
        """Return a greeting."""
        return "Hello!"


print(Person)
print(Person.__dict__["species"])
print(Person.__dict__["greet"])


# ============================================================
# 30. CLASS BODY EXECUTION WITH OBSERVABLE ORDER
# ============================================================

"""
The following example makes the execution order visible.
"""


print("1. Before class")


class Example:
    """Demonstrate class-body execution order."""

    print("2. Inside class - first statement")

    value = 10

    print("3. Inside class - after assignment")

    value = value + 5

    print("4. Inside class - after calculation")


print("5. After class")

print(Example.value)


# ============================================================
# 31. CLASS CREATION VS INSTANCE CREATION
# ============================================================

"""
Keep these events separate:

    Class creation:
        Executes the class body.

    Instance creation:
        Creates an object from the class.

    Initialization:
        __init__ may then initialize that instance.

This distinction will become central in the next file.
"""


class Person:
    """Represent a person."""

    print("Class body executed")

    def __init__(self) -> None:
        print("Instance initialization executed")


print("Class definition finished")

first = Person()

print("First instance created")

second = Person()

print("Second instance created")


# ============================================================
# 32. CONCEPTUAL TIMELINE
# ============================================================

"""
A simplified timeline:

    class Person:
        ...
            |
            v
    Class body executes
            |
            v
    Class object is created
            |
            v
    Person refers to class object
            |
            v
    person = Person()
            |
            v
    Instance is created
            |
            v
    __init__ may execute


The class body and __init__ therefore belong to different
stages.
"""


class Person:
    """Represent a person."""

    print("A - class body")

    def __init__(self) -> None:
        print("B - instance initialization")


print("C - class definition complete")

person = Person()


# ============================================================
# 33. KEY DISTINCTION: CLASS BODY VS METHOD BODY
# ============================================================

"""
Class body:

    Executes while the class is being defined.

Method body:

    Executes when the method is called.

Example:

    class Person:
        print("class body")

        def greet(self):
            print("method body")

The first print happens during class definition.

The second happens only when greet() is called.
"""


class Person:
    """Demonstrate class-body and method-body execution."""

    print("Class body executed")

    def greet(self) -> None:
        print("Method body executed")


print("Class definition complete")

person = Person()

print("Calling method")

person.greet()


# ============================================================
# 34. CONCEPTUAL MODEL
# ============================================================

"""
The complete conceptual model is:

    class Person:
        class_body
            |
            v
        class-body execution
            |
            v
        class namespace
            |
            v
        class object
            |
            v
        Person


Later:

    person = Person()
            |
            v
        instance object
            |
            v
        __init__ / initialization
"""


class Person:
    """Represent a person."""

    species = "Human"

    def __init__(self) -> None:
        self.name = "Shreyas"


person = Person()

print(Person.species)
print(person.name)


# ============================================================
# 35. KEY TAKEAWAYS
# ============================================================

"""
Key concepts:

1. A class body is executable Python code.

2. The class body executes when the class is defined.

3. Statements in the class body execute in order.

4. Expressions in the class body are evaluated.

5. Assignments in the class body create class-level names.

6. Functions defined in the class body become part of the
   class namespace.

7. Method bodies do not execute merely because the method is
   defined.

8. Class-body execution happens when the class is created.

9. Creating an instance does not normally re-execute the
   class body.

10. __init__ does not execute when the class is defined.

11. __init__ is associated with instance creation and
    initialization.

12. Class attributes are established during class-body
    execution.

13. The resulting names become part of the class namespace.

14. The class body can contain normal Python constructs such
    as expressions, function calls, conditionals, and loops.

15. Class-body execution and instance initialization are
    separate stages.

16. The exact mechanics of class creation involve Python's
    metaclass machinery, which is an advanced topic.

The next file:

    03_object_creation.py

will focus specifically on how calling a class creates an
instance and how object creation relates to __new__ and
__init__.
"""