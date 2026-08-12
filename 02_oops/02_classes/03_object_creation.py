# type: ignore
"""
03_object_creation.py

Introduces object creation from a class.

This file focuses on:

    - Calling a class to create an object
    - Class object vs instance object
    - Object creation flow
    - __new__()
    - __init__()
    - The difference between creation and initialization
    - Constructor terminology in Python
    - Object identity
    - Creating multiple independent instances
    - Passing arguments during object creation

Class definitions were covered in:

    01_class_definition.py

Class-body execution was covered in:

    02_class_body_execution.py

Instance methods are covered separately in:

    04_instance_methods.py
"""


# ============================================================
# 1. CALLING A CLASS CREATES AN INSTANCE
# ============================================================

"""
A class can be called like a function.

For a normal user-defined class:

    Person()

creates an instance of Person.
"""


class Person:
    """Represent a person."""

    pass


person = Person()

print(person)


# ============================================================
# 2. CLASS OBJECT VS INSTANCE OBJECT
# ============================================================

"""
These are two different objects:

    Person
        -> the class object

    Person()
        -> an instance created from that class
"""


class Person:
    """Represent a person."""

    pass


person = Person()

print("Class:", Person)
print("Instance:", person)

print("Are they the same object?", Person is person)


# ============================================================
# 3. TYPE OF THE INSTANCE
# ============================================================

"""
The type of an instance created from Person is Person.
"""


class Person:
    """Represent a person."""

    pass


person = Person()

print(type(person))
print(type(person) is Person)


# ============================================================
# 4. isinstance() CONFIRMS THE RELATIONSHIP
# ============================================================

"""
isinstance() can be used to check whether an object is an
instance of a particular class.
"""


class Person:
    """Represent a person."""

    pass


person = Person()

print(isinstance(person, Person))


# ============================================================
# 5. EACH CALL TO THE CLASS CAN CREATE A NEW INSTANCE
# ============================================================

"""
Calling the class multiple times creates multiple instances.
"""


class Person:
    """Represent a person."""

    pass


first_person = Person()
second_person = Person()
third_person = Person()

print(first_person)
print(second_person)
print(third_person)


# ============================================================
# 6. DIFFERENT INSTANCES HAVE DIFFERENT IDENTITIES
# ============================================================

"""
Each separately created instance is a distinct object with its
own identity.
"""


class Person:
    """Represent a person."""

    pass


first_person = Person()
second_person = Person()

print(id(first_person))
print(id(second_person))

print(first_person is second_person)


# ============================================================
# 7. ASSIGNMENT DOES NOT CREATE A NEW OBJECT
# ============================================================

"""
Assigning an existing instance to another variable does not
create another object.

Both variables refer to the same instance.
"""


class Person:
    """Represent a person."""

    pass


first_person = Person()
second_person = first_person

print(first_person is second_person)

print(id(first_person))
print(id(second_person))


# ============================================================
# 8. OBJECT CREATION WITH __init__()
# ============================================================

"""
A class can define __init__ to initialize an instance after it
has been created.
"""


class Person:
    """Represent a person."""

    def __init__(self) -> None:
        print("__init__ executed")


print("Before creating object")

person = Person()

print("After creating object")


# ============================================================
# 9. __init__ IS INITIALIZATION, NOT THE ACTUAL OBJECT CREATION
# ============================================================

"""
A common simplification is:

    __init__ creates the object.

More precisely:

    __new__()
        creates the instance

    __init__()
        initializes the already-created instance

For normal classes, Python handles the __new__ step
automatically.
"""


class Person:
    """Represent a person."""

    def __init__(self) -> None:
        print("Initializing Person")


person = Person()

print(person)


# ============================================================
# 10. __new__ PARTICIPATES IN OBJECT CREATION
# ============================================================

"""
__new__ is responsible for creating and returning the new
instance.

It is a class-level mechanism and receives the class as its
first argument.

It is an advanced mechanism and should normally not be
overridden unless there is a specific reason.
"""


class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        print("__new__ executed")
        return super().__new__(cls)

    def __init__(self) -> None:
        print("__init__ executed")


person = Person()

print(person)


# ============================================================
# 11. OBJECT CREATION ORDER
# ============================================================

"""
For a normal class call:

    Person()

the simplified flow is:

    1. __new__() is called.
    2. __new__() creates and returns an instance.
    3. __init__() initializes that instance.
    4. The initialized instance is returned to the caller.
"""


class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        print("1. __new__")
        return super().__new__(cls)

    def __init__(self) -> None:
        print("2. __init__")


print("Creating object")

person = Person()

print("Object creation complete")


# ============================================================
# 12. __new__ RECEIVES THE CLASS
# ============================================================

"""
The first parameter of __new__ is conventionally named cls.

It refers to the class for which an instance is being created.
"""


class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        print("Class received by __new__:", cls)
        return super().__new__(cls)


person = Person()


# ============================================================
# 13. __init__ RECEIVES THE INSTANCE
# ============================================================

"""
The first parameter of __init__ is conventionally named self.

It refers to the newly created instance being initialized.
"""


class Person:
    """Represent a person."""

    def __init__(self) -> None:
        print("Instance received by __init__:", self)


person = Person()


# ============================================================
# 14. __new__ AND __init__ HAVE DIFFERENT RESPONSIBILITIES
# ============================================================

"""
Conceptually:

    __new__()
        -> obtains/creates the instance

    __init__()
        -> configures/initializes the instance
"""


class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        print("Creating instance")
        return super().__new__(cls)

    def __init__(self) -> None:
        print("Initializing instance")
        self.name = "Shreyas"


person = Person()

print(person.name)


# ============================================================
# 15. __init__ CAN RECEIVE ARGUMENTS
# ============================================================

"""
Arguments passed to the class call are forwarded to __init__
after the instance has been created.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person("Shreyas", 29)

print(person.name)
print(person.age)


# ============================================================
# 16. __new__ CAN ALSO RECEIVE ARGUMENTS
# ============================================================

"""
Arguments passed during object creation are also available to
__new__.

Both __new__ and __init__ participate in the creation process,
although they have different responsibilities.
"""


class Person:
    """Represent a person."""

    def __new__(cls, name: str) -> "Person":
        print("Creating object for:", name)
        return super().__new__(cls)

    def __init__(self, name: str) -> None:
        print("Initializing object for:", name)
        self.name = name


person = Person("Shreyas")

print(person.name)


# ============================================================
# 17. __init__ MUST RETURN None
# ============================================================

"""
__init__ is an initializer.

It must return None.

Returning another value from __init__ causes Python to raise
a TypeError during object creation.

Therefore, __init__ should simply initialize the instance.
"""


class Person:
    """Represent a person."""

    def __init__(self) -> None:
        self.name = "Shreyas"


person = Person()

print(person.name)


# ============================================================
# 18. __new__ MUST RETURN AN APPROPRIATE OBJECT
# ============================================================

"""
Unlike __init__, __new__ is responsible for returning the
object that should be initialized.

For normal classes, this is commonly:

    super().__new__(cls)
"""


class Person:
    """Represent a person."""

    def __new__(cls) -> "Person":
        return super().__new__(cls)


person = Person()

print(person)


# ============================================================
# 19. OBJECT CREATION WITHOUT EXPLICIT __new__()
# ============================================================

"""
Most classes do not need to define __new__ themselves.

Python inherits an appropriate implementation from the class
hierarchy.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.name)


# ============================================================
# 20. MOST CLASSES ONLY NEED __init__()
# ============================================================

"""
In everyday Python programming, you will usually write:

    class Person:
        def __init__(self, name):
            self.name = name

and allow Python to handle __new__ automatically.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.name)


# ============================================================
# 21. OBJECT CREATION WITH DEFAULT ARGUMENTS
# ============================================================

"""
Object creation can use normal function argument rules.

Default arguments can therefore be used in __init__.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int = 18) -> None:
        self.name = name
        self.age = age


first = Person("Shreyas", 29)
second = Person("Rahul")

print(first.name, first.age)
print(second.name, second.age)


# ============================================================
# 22. OBJECT CREATION WITH KEYWORD ARGUMENTS
# ============================================================

"""
Arguments can also be passed using keywords when creating
objects.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person(name="Shreyas", age=29)

print(person.name)
print(person.age)


# ============================================================
# 23. OBJECT CREATION WITH POSITIONAL ARGUMENTS
# ============================================================

"""
Arguments can be passed positionally according to the
parameter order defined by __init__.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = Person("Shreyas", 29)

print(person.name)
print(person.age)


# ============================================================
# 24. EACH INSTANCE CAN RECEIVE DIFFERENT INITIAL STATE
# ============================================================

"""
Each call to the class can pass different initialization
values.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


first = Person("Shreyas", 29)
second = Person("Rahul", 30)

print(first.__dict__)
print(second.__dict__)


# ============================================================
# 25. OBJECT CREATION DOES NOT SHARE INSTANCE STATE
# ============================================================

"""
Each object receives its own instance attributes when
initialized.
"""


class Counter:
    """Represent an independent counter."""

    def __init__(self, value: int) -> None:
        self.value = value


first = Counter(0)
second = Counter(10)

first.value += 1

print(first.value)
print(second.value)


# ============================================================
# 26. OBJECT CREATION AND OBJECT IDENTITY
# ============================================================

"""
Every separately created instance has its own identity.
"""


class Person:
    """Represent a person."""

    pass


first = Person()
second = Person()

print(id(first))
print(id(second))

print(first is second)


# ============================================================
# 27. CLASS CALL IS THE NORMAL CREATION INTERFACE
# ============================================================

"""
From the user's perspective, the normal syntax is simply:

    person = Person()

Python's object model handles the underlying __new__ and
__init__ sequence.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person)


# ============================================================
# 28. OBJECT CREATION WITH EXPLICIT __new__ AND __init__
# ============================================================

"""
This example makes the complete sequence visible.

The print statements show that __new__ runs before __init__.
"""


class Person:
    """Represent a person."""

    def __new__(cls, name: str) -> "Person":
        print("1. __new__")
        return super().__new__(cls)

    def __init__(self, name: str) -> None:
        print("2. __init__")
        self.name = name


person = Person("Shreyas")

print("3. Object available to caller")
print(person.name)


# ============================================================
# 29. __new__ RETURNS THE INSTANCE PASSED TO __init__
# ============================================================

"""
When __new__ returns an instance of the class, Python then
calls __init__ on that returned instance.
"""


class Person:
    """Represent a person."""

    def __new__(cls, name: str) -> "Person":
        instance = super().__new__(cls)
        print("Created:", instance)
        return instance

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.name)


# ============================================================
# 30. __new__ CAN PREVENT __init__ FROM RUNNING
# ============================================================

"""
This is an advanced behavior.

If __new__ returns an object that is not an instance of the
class being constructed, Python does not call that class's
__init__ in the normal way.

This example is included to show why __new__ is fundamentally
different from __init__.
"""


class Person:
    """Demonstrate __new__ behavior."""

    def __new__(cls) -> object:
        return "not a Person"


result = Person()

print(result)
print(type(result))


# ============================================================
# 31. CONSTRUCTOR TERMINOLOGY
# ============================================================

"""
Python terminology can be confusing because __init__ is often
called a "constructor" informally.

More precisely:

    __new__()
        -> creates or obtains the instance

    __init__()
        -> initializes the instance

Therefore, __init__ is technically an initializer rather than
the mechanism that creates the object itself.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.name)


# ============================================================
# 32. OBJECT CREATION VS INITIALIZATION
# ============================================================

"""
Think of object creation as two conceptual stages:

    Stage 1:
        Obtain/create the object.

    Stage 2:
        Initialize its state.

In Python:

    __new__()
        -> Stage 1

    __init__()
        -> Stage 2
"""


class Account:
    """Represent a bank account."""

    def __new__(cls, owner: str) -> "Account":
        print("Stage 1: creating account object")
        return super().__new__(cls)

    def __init__(self, owner: str) -> None:
        print("Stage 2: initializing account")
        self.owner = owner


account = Account("Shreyas")

print(account.owner)


# ============================================================
# 33. MULTIPLE OBJECTS MEAN MULTIPLE INITIALIZATIONS
# ============================================================

"""
Each new instance receives its own initialization call.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        print(f"Initializing {name}")
        self.name = name


first = Person("Shreyas")
second = Person("Rahul")
third = Person("Arjun")


# ============================================================
# 34. REASSIGNMENT DOES NOT RECREATE THE OBJECT
# ============================================================

"""
Reassigning an attribute does not recreate the object.

Only the object's state changes.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

original_id = id(person)

person.name = "Arjun"

print(person.name)
print(id(person) == original_id)


# ============================================================
# 35. CLASS CALL WITH NO __init__
# ============================================================

"""
If a class does not define its own __init__, an inherited
initializer is used.

For a simple class, no custom initialization may be necessary.
"""


class Person:
    """Represent a person."""

    pass


person = Person()

print(person)


# ============================================================
# 36. OBJECT CREATION FLOW
# ============================================================

"""
A simplified normal flow is:

    Person("Shreyas")
            |
            v
        __new__(Person)
            |
            v
      new Person instance
            |
            v
      __init__(instance, "Shreyas")
            |
            v
      initialized instance
            |
            v
       caller receives it


This is a conceptual model. The actual implementation is
controlled by the class's metaclass and object model.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


person = Person("Shreyas")

print(person.name)


# ============================================================
# 37. CONCEPTUAL MODEL: CLASS -> OBJECT
# ============================================================

"""
The relationship can now be visualized as:

    Person
      |
      | call
      v
    Person()
      |
      | object creation
      v
    instance
      |
      | initialization
      v
    initialized instance


The class defines the structure and behavior.

Each call produces an individual object.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


first = Person("Shreyas")
second = Person("Rahul")

print(first.name)
print(second.name)


# ============================================================
# 38. KEY TAKEAWAYS
# ============================================================

"""
Key concepts:

1. A class can be called to create an instance.

2. Person and Person() represent different things.

3. Person is the class object.

4. Person() produces an instance.

5. Each separate class call can create a separate instance.

6. Each instance has its own identity.

7. Assignment to another variable does not create a new object.

8. __new__ participates in creating or obtaining the instance.

9. __init__ initializes the already-created instance.

10. __new__ receives the class as its first argument, normally
    named cls.

11. __init__ receives the instance as its first argument,
    normally named self.

12. __new__ must return an appropriate object.

13. __init__ must return None.

14. Most everyday classes do not need to override __new__.

15. Most everyday classes use __init__ to initialize state.

16. Arguments passed to the class call are used during the
    initialization process.

17. Object creation and object initialization are conceptually
    separate stages.

18. __init__ is technically an initializer, although it is
    often informally called a constructor.

19. The complete object-creation mechanism is more advanced
    than simply calling __init__.

The next file:

    04_instance_methods.py

will focus specifically on methods that operate on individual
instances.
"""