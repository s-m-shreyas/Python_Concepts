
# Constructors and Initialization

This folder covers how Python objects are created and initialized, with a focus on `__init__()`, instance state, default initialization, and parameterized initialization.

## Files

- `01_init_method.py` — Introduction to the `__init__()` method
- `02_constructor_vs_initializer.py` — Constructor vs. initializer
- `03_instance_initialization.py` — Instance attribute initialization
- `04_default_initialization.py` — Default instance initialization
- `05_initialization_with_parameters.py` — Parameterized instance initialization

## Learning Flow

Object Creation → `__init__()` → Instance Initialization → Default Initialization → Parameterized Initialization

## Topics Covered

- `__init__()` and its purpose
- Object creation vs. object initialization
- Instance attributes
- The `self` reference during initialization
- Instance state
- Independent state between objects
- Default instance values
- Parameterized initialization
- Required and optional initialization parameters
- Parameter validation during initialization
- Derived instance attributes
- Mutable instance attributes
- Avoiding shared mutable class attributes
- Inspecting initialized instance state with `__dict__`
- Relationship between initialization parameters and instance attributes

## Core Concepts

### `__init__()`

`__init__()` is the standard initialization method used to establish the initial state of an object after the instance has been created.

Example:

    class Person:
        def __init__(self) -> None:
            self.name = "Unknown"
            self.age = 0

When `Person()` is evaluated, Python creates the instance and then executes `__init__()` to initialize its state.

### Constructor vs. Initializer

Object creation and object initialization are related but distinct operations.

Conceptually:

    Class()
       ↓
    Object creation
       ↓
    Instance exists
       ↓
    __init__()
       ↓
    Instance initialization
       ↓
    Initialized object

`__init__()` initializes an instance; it is not responsible for actually creating the instance.

### Instance Initialization

Instance initialization establishes attributes belonging to a particular object.

Example:

    class Person:
        def __init__(self) -> None:
            self.name = "Alice"
            self.age = 30

The use of `self` ensures that the attributes belong to the current instance.

### Default Initialization

An object can begin with predefined values.

Example:

    class Account:
        def __init__(self) -> None:
            self.balance = 0.0
            self.active = True

Every new `Account` starts with these values, while each instance maintains independent state.

### Parameterized Initialization

Values can be supplied when creating an object.

Example:

    class Person:
        def __init__(self, name: str, age: int) -> None:
            self.name = name
            self.age = age

    person = Person("Alice", 30)

The supplied values become part of the instance's initial state.

## Parameter vs. Instance Attribute

Consider:

    def __init__(self, name: str) -> None:
        self.name = name

There are two different concepts here:

    name
        ↓
    Parameter
        ↓
    Temporary/local value available during __init__()

    self.name
        ↓
    Instance attribute
        ↓
    Persistent state belonging to the object

The parameter does not automatically become an attribute. The assignment to `self.name` explicitly stores the value in the instance.

## Instance Independence

Each instance normally receives its own instance state.

Example:

    class Person:
        def __init__(self, name: str) -> None:
            self.name = name

    person_1 = Person("Alice")
    person_2 = Person("Bob")

Conceptually:

    person_1
        └── name → "Alice"

    person_2
        └── name → "Bob"

Changing `person_1.name` does not change `person_2.name`.

## Mutable Instance State

Mutable objects such as lists and dictionaries should normally be created inside `__init__()` when they represent per-instance state.

Correct:

    class Student:
        def __init__(self) -> None:
            self.subjects = []

Each `Student` receives a separate list.

Avoid unintentionally sharing mutable state through a class attribute:

    class Student:
        subjects = []

This creates one shared list at the class level.

## Initialization and Validation

Initialization can validate supplied values before storing them.

Example:

    class Product:
        def __init__(self, price: float) -> None:
            if price < 0:
                raise ValueError("Price cannot be negative.")

            self.price = price

This allows an object to establish valid initial state.

## Initialization and Derived State

Not every instance attribute has to directly correspond to an initialization parameter.

Example:

    class Rectangle:
        def __init__(self, width: float, height: float) -> None:
            self.width = width
            self.height = height
            self.area = width * height

Here:

- `width` is initialized from a parameter.
- `height` is initialized from a parameter.
- `area` is derived from the other attributes.

## Inspecting Instance State

For normal classes that use an instance dictionary, initialized state can be inspected with:

    person.__dict__

Example:

    class Person:
        def __init__(self, name: str, age: int) -> None:
            self.name = name
            self.age = age

    person = Person("Alice", 30)

    print(person.__dict__)

Result:

    {'name': 'Alice', 'age': 30}

`__dict__` is the instance's attribute storage dictionary for classes that provide one. It is not available for every possible Python object.

## Initialization Flow

For default initialization:

    Person()
       ↓
    Instance created
       ↓
    __init__() executes
       ↓
    self.name = "Unknown"
    self.age = 0
       ↓
    Initialized instance

For parameterized initialization:

    Person("Alice", 30)
       ↓
    __init__(self, name, age)
       ↓
    name = "Alice"
    age = 30
       ↓
    self.name = name
    self.age = age
       ↓
    Initialized instance

## Important Principles

1. `__init__()` initializes an already-created instance.
2. Instance attributes are normally assigned through `self`.
3. Each instance maintains its own instance state.
4. Default initialization establishes predictable starting state.
5. Parameters allow different instances to begin with different values.
6. Parameters and instance attributes are separate concepts.
7. Initialization can validate or transform incoming values.
8. Derived attributes can be calculated during initialization.
9. Mutable per-instance state should normally be created inside `__init__()`.
10. Initialization establishes starting state; it does not inherently make an object immutable.

## Recommended Study Order

Study the files in numerical order:

    01 → 02 → 03 → 04 → 05

The progression is:

    __init__()
        ↓
    Constructor vs. Initializer
        ↓
    Instance Initialization
        ↓
    Default Initialization
        ↓
    Parameterized Initialization

## Goal

By the end of this folder, you should understand how Python creates an instance, how `__init__()` establishes its initial state, how instance attributes differ from initialization parameters, and how different objects of the same class can begin with different independent states.

