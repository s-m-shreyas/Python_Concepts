
# Python Concepts

A structured Python learning repository covering Python from fundamentals to object-oriented programming, advanced Python concepts, algorithms, and commonly used libraries.

The repository is designed as a long-term learning reference where each concept is explored through focused, practical, and copy-paste-ready examples.

---

## Repository Goals

This repository is built to:

- Develop strong Python fundamentals
- Understand Python's object model and object-oriented programming deeply
- Explore advanced Python concepts
- Practice algorithms and data structures
- Build familiarity with commonly used Python libraries
- Provide a structured revision reference
- Maintain focused examples for individual concepts
- Support practical learning and interview preparation

---

## Repository Architecture

The repository is divided into five major learning tracks:

    01_fundamentals
            ↓
    02_oops
            ↓
    03_advanced
            ↓
    04_algorithms
            ↓
    05_libraries_and_modules

Each track builds on concepts introduced earlier in the repository.

---

# 01 — Fundamentals

The Fundamentals section establishes the core Python programming model.

## 01 Basics

Introduces the basic building blocks of Python:

- Variables
- Comments
- Type annotations
- `print()`
- `input()`
- Hello World
- Constants
- Naming conventions
- Type hinting

## 02 Data Types & Operators

Covers Python's built-in data types and operators.

### Single-valued Data Types

- Integer
- Float
- Complex

### Multi-valued Data Types

- String
- List
- Tuple
- Set
- Frozenset
- Dictionary
- Bytes
- Bytearray
- Memoryview

### Special Data Types

- `None`
- Boolean

### Type Checking

- Type basics
- `type()`

### Type Behaviour

- Mutability
- Hashability
- Equality vs identity
- Type conversion

### Operators

- Arithmetic operators
- Comparison operators
- Assignment operators
- Augmented assignment operators
- Logical operators
- Bitwise operators
- Membership operators
- Identity operators
- Unary operators
- Ternary operator
- Chained comparisons
- Short-circuit evaluation
- Operator precedence
- Operator associativity

## 03 Indexing & Slicing

Covers:

- Positive indexing
- Negative indexing
- Start/stop/step combinations
- Nested indexing
- Nested slicing
- Slice objects
- Mutable and immutable slicing

## 04 Copy Operations

Covers:

- General assignment and copy behaviour
- Shallow copy
- Deep copy

## 05 Control Statements

### Conditional Statements

- `if`
- `if-else`
- `if-elif-else`
- Nested `if`
- Ternary operator
- `match-case`

### Looping Statements

- `for`
- `while`
- Nested loops
- `break`
- `continue`
- `pass`
- Loop `else`
- `range()`
- `enumerate()`
- `zip()`

## 06 Functions

Covers Python functions from basic definitions through function-level features.

- Function basics
- Function parameters
- Positional arguments
- Keyword arguments
- Default arguments
- `*args`
- `**kwargs`
- Return statements
- Multiple return values
- Scope
- `global`
- `nonlocal`
- Nested functions
- Function annotations
- Docstrings
- Built-in functions

## 07 Modules & Packages

Covers Python's module and package system.

### Modules

- Module basics
- `import`
- `import ... as`
- `from ... import`
- Multiple imports
- Module namespace
- Module attributes
- Module execution

### Module Search & Resolution

- `sys.path`
- Module search path
- Standard library vs custom modules
- Import resolution

### Packages

- Package basics
- Subpackages
- Package imports
- `__init__.py`

### Import Patterns

- Absolute imports
- Relative imports
- Import aliases
- Import conventions

### Special Module Attributes

- `__name__`
- `__main__`
- `__file__`

## 08 Exception Handling

Covers Python's exception-handling system.

- Exception basics
- `try-except`
- Multiple exceptions
- Exception aliases
- `else`
- `finally`
- `raise`
- Custom exceptions
- Exception chaining
- Exception context
- `assert`

## 09 File Handling

Covers working with files in Python.

- File handling basics
- `open()`
- File modes
- Reading files
- Writing files
- Appending files
- File position
- `seek()`
- `tell()`
- `with`
- Text and binary files
- Encoding
- File iteration

---

# 02 — Object-Oriented Programming

The OOP section explores Python's object model and object-oriented programming mechanisms.

## 01 Object Model

Covers:

- Objects and identity
- Object state and behaviour
- Attributes and methods
- Instance attributes
- Class attributes
- Object namespace
- Class namespace

## 02 Classes

Covers:

- Class definition
- Class body execution
- Object creation
- Instance methods
- `self`
- Class methods
- Static methods
- Method binding

## 03 Constructors & Initialization

Covers:

- `__init__`
- Constructor vs initializer
- Instance initialization
- Default initialization
- Parameterized initialization

## 04 Inheritance

Covers:

- Single inheritance
- Multilevel inheritance
- Multiple inheritance
- Hierarchical inheritance
- Method inheritance
- Attribute inheritance
- Method Resolution Order
- `super()`

## 05 Polymorphism

Covers:

- Method overriding
- Duck typing
- Polymorphic functions
- Polymorphism with inheritance

## 06 Encapsulation

Covers:

- Public members
- Protected-member convention
- Private members
- Name mangling

## 07 Abstraction

Covers:

- Abstract base classes
- Abstract methods
- Abstract properties
- Concrete implementations

## 08 Properties

Covers:

- `property()`
- Getters and setters
- Read-only properties
- Property validation

## 09 Dunder Methods

Covers:

- `__str__`
- `__repr__`
- `__eq__`
- `__ne__`
- Comparison methods
- Arithmetic methods
- Container methods
- Callable objects
- `__len__`
- `__bool__`

## 10 Operator Overloading

Covers:

- Operator overloading
- Dunder operator methods
- Arithmetic dunder methods
- Comparison dunder methods
- In-place operators
- Custom operator overloading

## 11 Composition

Covers:

- Has-a relationships
- Composition
- Aggregation
- Composition vs inheritance

## 12 Class Design

Covers:

- Single Responsibility
- Instance vs class responsibility
- Inheritance vs composition
- Interface design

## 13 Dataclasses

Covers:

- Dataclass basics
- Generated methods
- Default values
- `field()`
- `__post_init__`
- Frozen dataclasses
- Dataclass inheritance
- Comparison and ordering

---

# 03 — Advanced Python

The Advanced section covers Python features that build on the fundamentals and OOP model.

## 01 Advanced Functions

Covers:

- Lambda functions
- First-class functions
- Higher-order functions
- Recursive functions
- Callable objects

## 02 Comprehensions

Covers:

- List comprehensions
- Conditional list comprehensions
- Nested list comprehensions
- Set comprehensions
- Dictionary comprehensions
- Conditional comprehensions
- Nested comprehensions
- Comprehensions vs loops
- Comprehension best practices

## 03 Decorators

Covers:

- Decorator basics
- Function decorators
- Decorator execution
- Decorators with arguments
- `functools.wraps`
- Multiple decorators
- Class decorators

## 04 Generators

Covers:

- Generator basics
- `yield`
- Generator functions
- Generator expressions
- Generator state
- `send()`
- `throw()`
- `close()`

## 05 Iterators

Covers:

- Iterable vs iterator
- `iter()`
- `next()`
- Iterator protocol
- Custom iterators
- Iterator state

## 06 Context Managers

Covers:

- Context manager basics
- `with`
- `__enter__`
- `__exit__`
- Custom context managers
- `contextlib`

## 07 Descriptors

Covers:

- Descriptor basics
- `__get__`
- `__set__`
- `__delete__`
- Data descriptors
- Non-data descriptors
- Descriptor use cases

## 08 Metaclasses

Covers:

- Metaclass basics
- Class creation
- Custom metaclasses
- `type`
- Metaclass behaviour

## 09 Concurrency

Covers:

- Concurrency basics
- Threads
- Processes
- Threading
- Multiprocessing
- Synchronization
- Concurrent execution

## 10 Async Programming

Covers:

- Asynchronous programming basics
- `async`
- `await`
- Coroutines
- Event loops
- Async tasks
- Async execution

---

# 04 — Algorithms

The Algorithms section focuses on algorithmic problem solving and data structures.

## 01 Sorting

Implemented sorting algorithms include:

- Selection Sort
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

## 02 Searching

Dedicated section for searching algorithms and implementations.

## 03 Recursion

Dedicated section for recursive problem solving.

## 04 Linked Lists

Dedicated section for linked-list data structures and operations.

## 05 Stacks & Queues

Dedicated section for stack and queue data structures.

## 06 Trees

Dedicated section for tree-based data structures.

## 07 Graphs

Dedicated section for graph data structures and algorithms.

## 08 Hashing

Dedicated section for hashing concepts and implementations.

---

# 05 — Libraries & Modules

The final learning track focuses on practical Python libraries and modules.

## 01 Standard Library

Currently organized into:

- `os`
- `sys`
- `pathlib`
- `datetime`
- `json`
- `csv`
- `re`

## 02 NumPy

Dedicated section for NumPy.

## 03 Pandas

Dedicated section for Pandas.

## 04 Matplotlib

Dedicated section for Matplotlib.

## 05 Requests

Dedicated section for Requests.

## 06 SQLAlchemy

Dedicated section for SQLAlchemy.

## 07 Pytest

Dedicated section for Pytest.

---

# Code Organization Philosophy

The repository follows a concept-first structure.

Instead of putting many unrelated concepts into one large Python file, individual concepts are separated into focused files.

For example:

    06_functions/
    │
    ├── 01_function_basics.py
    ├── 02_function_parameters.py
    ├── 03_positional_arguments.py
    ├── 04_keyword_arguments.py
    ├── 05_default_arguments.py
    ├── ...
    ├── 16_builtin_functions.py
    └── README.md

This makes it easier to:

- Study one concept at a time
- Run individual examples
- Locate specific concepts quickly
- Compare related concepts
- Revise efficiently
- Build understanding progressively

---

# Coding Standards

The examples follow a consistent coding style throughout the repository.

General principles include:

- One primary concept per file
- Descriptive names
- Clear structure
- Type annotations where appropriate
- Copy-paste-ready examples
- Non-interactive examples unless interaction is the concept
- Beginner-friendly comments
- Explicit examples
- Static type-checker-friendly code where practical
- Conceptual accuracy over unnecessary complexity

Detailed conventions are documented in:

    STYLE_GUIDE.md

---

# Learning Progress

The repository is developed progressively.

## Fundamentals

- [x] Basics
- [x] Data Types & Operators
- [x] Indexing & Slicing
- [x] Copy Operations
- [x] Control Statements
- [x] Functions
- [x] Modules & Packages
- [x] Exception Handling
- [x] File Handling

## Object-Oriented Programming

- [x] Object Model
- [x] Classes
- [x] Constructors & Initialization
- [x] Inheritance
- [x] Polymorphism
- [x] Encapsulation
- [x] Abstraction
- [x] Properties
- [x] Dunder Methods
- [x] Operator Overloading
- [x] Composition
- [x] Class Design
- [x] Dataclasses

## Advanced Python

- [x] Advanced Functions
- [x] Comprehensions
- [ ] Decorators
- [ ] Generators
- [ ] Iterators
- [ ] Context Managers
- [ ] Descriptors
- [ ] Metaclasses
- [ ] Concurrency
- [ ] Async Programming

## Algorithms

- [x] Sorting
- [ ] Searching
- [ ] Recursion
- [ ] Linked Lists
- [ ] Stacks & Queues
- [ ] Trees
- [ ] Graphs
- [ ] Hashing

## Libraries & Modules

- [ ] Standard Library
- [ ] NumPy
- [ ] Pandas
- [ ] Matplotlib
- [ ] Requests
- [ ] SQLAlchemy
- [ ] Pytest

---

# Roadmap

The overall learning progression is:

    Python Fundamentals
            ↓
    Object-Oriented Programming
            ↓
    Advanced Python
            ↓
    Algorithms & Data Structures
            ↓
    Libraries & Modules
            ↓
    Practical Projects

The repository is intended to evolve continuously as new concepts are studied and implemented.

---

# Requirements

Current target Python version:

    Python 3.12+

---

# How to Use

Clone the repository:

    git clone https://github.com/shreyas-global-7/Python_Concepts.git

Navigate into the repository:

    cd Python_Concepts

Navigate to any concept directory:

    cd 02_oops/05_polymorphism

Run an example:

    python 01_method_overriding.py

Individual examples may be run independently where the concept permits it.

---

# YouTube

A future YouTube channel will complement this repository with concept explanations, demonstrations, and walkthroughs.

The repository will provide the implementation and reference material, while the videos will provide the visual explanation layer.

**YouTube channel: Coming soon.**

---

# Author

**S. M. Shreyas**

- GitHub: https://github.com/s-m-shreyas
- LinkedIn: https://linkedin.com/in/s-m-shreyas

---

# License

This repository is created primarily for educational and learning purposes.
```
