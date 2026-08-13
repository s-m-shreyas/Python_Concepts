
# Python Concepts — Roadmap

This roadmap defines the planned learning progression for the Python Concepts repository.

The repository is being developed as a structured Python knowledge base rather than as a collection of disconnected examples.

The overall progression is:

    01_fundamentals
            ↓
    02_oops
            ↓
    03_advanced
            ↓
    04_algorithms
            ↓
    05_libraries_and_modules
            ↓
    Practical Projects


# 1. Fundamentals

Path:

    01_fundamentals/

The Fundamentals track establishes the core Python language.

## 01 Basics

- [x] Variables
- [x] Comments
- [x] Type annotations
- [x] `print()`
- [x] `input()`
- [x] Hello World
- [x] Constants
- [x] Naming conventions
- [x] Type hinting

## 02 Data Types & Operators

- [x] Single-valued data types
- [x] Multi-valued data types
- [x] Special data types
- [x] Type checking
- [x] Type behaviour
- [x] Operators

## 03 Indexing & Slicing

- [x] Positive indexing
- [x] Negative indexing
- [x] Positive start/stop with positive step
- [x] Positive start/stop with negative step
- [x] Negative start/stop with positive step
- [x] Negative start/stop with negative step
- [x] Nested indexing
- [x] Nested slicing
- [x] Slice objects
- [x] Mutable and immutable slicing

## 04 Copy Operations

- [x] General copy behaviour
- [x] Shallow copy
- [x] Deep copy

## 05 Control Flow

### Conditional Statements

- [x] Conditional statements
- [x] `if`
- [x] `if-else`
- [x] `if-elif-else`
- [x] Nested conditionals
- [x] Ternary expressions
- [x] `match-case`

### Looping Statements

- [x] `for`
- [x] `while`
- [x] Nested loops
- [x] `break`
- [x] `continue`
- [x] `pass`
- [x] Loop `else`
- [x] `range()`
- [x] `enumerate()`
- [x] `zip()`

## 06 Functions

- [x] Function basics
- [x] Function parameters
- [x] Positional arguments
- [x] Keyword arguments
- [x] Default arguments
- [x] `*args`
- [x] `**kwargs`
- [x] Return statements
- [x] Multiple return values
- [x] Scope
- [x] `global`
- [x] `nonlocal`
- [x] Nested functions
- [x] Function annotations
- [x] Docstrings
- [x] Built-in functions

## 07 Modules & Packages

### Modules

- [x] Module basics
- [x] `import`
- [x] Import aliases
- [x] `from ... import`
- [x] Multiple object imports
- [x] Module namespace
- [x] Module attributes
- [x] Module execution

### Module Search & Resolution

- [x] `sys.path`
- [x] Module search path
- [x] Standard library vs custom modules
- [x] Import resolution

### Packages

- [x] Package basics
- [x] Subpackages
- [x] Package imports
- [x] `__init__.py`

### Import Patterns

- [x] Absolute imports
- [x] Relative imports
- [x] Import aliases
- [x] Import conventions

### Special Module Attributes

- [x] `__name__`
- [x] Main guard
- [x] `__file__`

## 08 Exception Handling

- [ ] Exception basics
- [ ] `try-except`
- [ ] Multiple exceptions
- [ ] Exception aliases
- [ ] `else`
- [ ] `finally`
- [ ] `raise`
- [ ] Custom exceptions
- [ ] Exception chaining
- [ ] Exception context
- [ ] `assert`

## 09 File Handling

- [ ] File handling basics
- [ ] `open()`
- [ ] File modes
- [ ] Reading files
- [ ] Writing files
- [ ] Appending files
- [ ] File position
- [ ] `seek()`
- [ ] `tell()`
- [ ] `with`
- [ ] Text files
- [ ] Binary files
- [ ] Encoding
- [ ] File iteration


# 2. Object-Oriented Programming

Path:

    02_oops/

The OOP track builds an understanding of Python's object model and object-oriented design.

## 01 Object Model

- [x] Objects
- [x] Identity
- [x] Object state
- [x] Object behaviour
- [x] Attributes
- [x] Methods
- [x] Instance attributes
- [x] Class attributes
- [x] Object namespace
- [x] Class namespace

## 02 Classes

- [x] Class definition
- [x] Class body execution
- [x] Object creation
- [x] Instance methods
- [x] `self`
- [x] Class methods
- [x] Static methods
- [x] Method binding

## 03 Constructors & Initialization

- [x] `__init__`
- [x] Constructor vs initializer
- [x] Instance initialization
- [x] Default initialization
- [x] Parameterized initialization

## 04 Inheritance

- [x] Single inheritance
- [x] Multilevel inheritance
- [x] Multiple inheritance
- [x] Hierarchical inheritance
- [x] Method inheritance
- [x] Attribute inheritance
- [x] Method Resolution Order
- [x] `super()`

## 05 Polymorphism

- [x] Method overriding
- [x] Duck typing
- [x] Polymorphic functions
- [x] Polymorphism with inheritance

## 06 Encapsulation

- [x] Public members
- [x] Protected-member convention
- [x] Private members
- [x] Name mangling

## 07 Abstraction

- [x] Abstract base classes
- [x] Abstract methods
- [x] Abstract properties
- [x] Concrete implementations

## 08 Properties

- [x] `property()`
- [x] Getters and setters
- [x] Read-only properties
- [x] Property validation

## 09 Dunder Methods

- [x] `__str__`
- [x] `__repr__`
- [x] `__eq__`
- [x] `__ne__`
- [x] Comparison methods
- [x] Arithmetic methods
- [x] Container methods
- [x] Callable objects
- [x] `__len__`
- [x] `__bool__`

## 10 Operator Overloading

- [x] Operator overloading
- [x] Arithmetic operators
- [x] Comparison operators
- [x] In-place operators
- [x] Custom operator behaviour

## 11 Composition

- [x] Has-a relationship
- [x] Composition
- [x] Aggregation
- [x] Composition vs inheritance

## 12 Class Design

- [x] Single Responsibility
- [x] Instance vs class responsibility
- [x] Inheritance vs composition
- [x] Interface design

## 13 Dataclasses

- [x] Dataclass basics
- [x] Generated methods
- [x] Default values
- [x] `field()`
- [x] `__post_init__`
- [x] Frozen dataclasses
- [x] Dataclass inheritance
- [x] Comparison and ordering


# 3. Advanced Python

Path:

    03_advanced/

The Advanced track introduces powerful Python language features that build upon the fundamentals and OOP concepts.

## 01 Advanced Functions

Status:

    COMPLETED

- [x] Lambda functions
- [x] First-class functions
- [x] Higher-order functions
- [x] Recursive functions
- [x] Callable objects

## 02 Comprehensions

Status:

    NEXT

- [ ] List comprehensions
- [ ] Conditional list comprehensions
- [ ] Nested list comprehensions
- [ ] Set comprehensions
- [ ] Dictionary comprehensions
- [ ] Conditional comprehensions
- [ ] Nested comprehensions
- [ ] Comprehensions vs loops
- [ ] Comprehension best practices

## 03 Decorators

Status:

    PLANNED

- [ ] Decorator basics
- [ ] Function decorators
- [ ] Decorator execution
- [ ] Decorators with arguments
- [ ] `functools.wraps`
- [ ] Multiple decorators
- [ ] Class decorators

## 04 Generators

Status:

    PLANNED

- [ ] Generator basics
- [ ] `yield`
- [ ] Generator functions
- [ ] Generator expressions
- [ ] Generator state
- [ ] `send()`
- [ ] `throw()`
- [ ] `close()`

## 05 Iterators

Status:

    PLANNED

- [ ] Iterable vs iterator
- [ ] `iter()`
- [ ] `next()`
- [ ] Iterator protocol
- [ ] Custom iterators
- [ ] Iterator state

## 06 Context Managers

Status:

    PLANNED

- [ ] Context manager basics
- [ ] `with`
- [ ] `__enter__`
- [ ] `__exit__`
- [ ] Custom context managers
- [ ] `contextlib`

## 07 Descriptors

Status:

    PLANNED

- [ ] Descriptor basics
- [ ] `__get__`
- [ ] `__set__`
- [ ] `__delete__`
- [ ] Data descriptors
- [ ] Non-data descriptors
- [ ] Descriptor use cases

## 08 Metaclasses

Status:

    PLANNED

- [ ] Metaclass basics
- [ ] Class creation
- [ ] Custom metaclasses
- [ ] `type`
- [ ] Metaclass behaviour

## 09 Concurrency

Status:

    PLANNED

- [ ] Concurrency basics
- [ ] Threads
- [ ] Processes
- [ ] Threading
- [ ] Multiprocessing
- [ ] Synchronization
- [ ] Concurrent execution

## 10 Async Programming

Status:

    PLANNED

- [ ] Asynchronous programming basics
- [ ] `async`
- [ ] `await`
- [ ] Coroutines
- [ ] Event loops
- [ ] Async tasks
- [ ] Async execution


# 4. Algorithms

Path:

    04_algorithms/

The Algorithms track develops algorithmic thinking and data-structure knowledge.

## 01 Sorting

- [x] Selection Sort
- [x] Bubble Sort
- [x] Insertion Sort
- [x] Merge Sort
- [x] Quick Sort
- [x] Heap Sort

## 02 Searching

- [ ] Linear Search
- [ ] Binary Search
- [ ] Searching variations
- [ ] Search complexity

## 03 Recursion

- [ ] Recursion basics
- [ ] Recursive problem solving
- [ ] Base cases
- [ ] Recursive call stack
- [ ] Recursive algorithms

## 04 Linked Lists

- [ ] Linked-list basics
- [ ] Node implementation
- [ ] Traversal
- [ ] Insertion
- [ ] Deletion
- [ ] Searching

## 05 Stacks & Queues

- [ ] Stack
- [ ] Queue
- [ ] Deque
- [ ] Stack operations
- [ ] Queue operations

## 06 Trees

- [ ] Tree basics
- [ ] Binary trees
- [ ] Binary search trees
- [ ] Tree traversal
- [ ] Tree operations

## 07 Graphs

- [ ] Graph basics
- [ ] Graph representations
- [ ] Breadth-first search
- [ ] Depth-first search
- [ ] Graph traversal

## 08 Hashing

- [ ] Hashing basics
- [ ] Hash functions
- [ ] Hash tables
- [ ] Collision concepts
- [ ] Hash-based algorithms


# 5. Libraries & Modules

Path:

    05_libraries_and_modules/

The Libraries section focuses on applying Python through the standard library and widely used third-party packages.

## 01 Standard Library

- [ ] `os`
- [ ] `sys`
- [ ] `pathlib`
- [ ] `datetime`
- [ ] `json`
- [ ] `csv`
- [ ] `re`

## 02 NumPy

- [ ] NumPy fundamentals
- [ ] Arrays
- [ ] Array operations
- [ ] Indexing
- [ ] Broadcasting
- [ ] Common NumPy functionality

## 03 Pandas

- [ ] Series
- [ ] DataFrames
- [ ] Indexing
- [ ] Selection
- [ ] Filtering
- [ ] Grouping
- [ ] Aggregation
- [ ] Joining
- [ ] Reshaping
- [ ] Input and output

## 04 Matplotlib

- [ ] Plotting basics
- [ ] Line plots
- [ ] Bar charts
- [ ] Scatter plots
- [ ] Histograms
- [ ] Figure and axes
- [ ] Plot customization

## 05 Requests

- [ ] HTTP basics
- [ ] GET requests
- [ ] POST requests
- [ ] Request parameters
- [ ] Headers
- [ ] Responses
- [ ] JSON APIs
- [ ] Error handling

## 06 SQLAlchemy

- [ ] SQLAlchemy basics
- [ ] Engine
- [ ] Connections
- [ ] SQL execution
- [ ] Metadata
- [ ] ORM basics
- [ ] Models
- [ ] Sessions

## 07 Pytest

- [ ] Testing basics
- [ ] Test functions
- [ ] Assertions
- [ ] Fixtures
- [ ] Parametrization
- [ ] Test organization
- [ ] Common testing patterns


# 6. Repository Completion Strategy

The repository will be developed in stages.

## Stage 1 — Core Python

    01_fundamentals/

Goal:

Build a strong understanding of Python's syntax, data model, control flow, functions, modules, exceptions, and files.

Status:

    IN PROGRESS

Completed:

- Basics
- Data Types & Operators
- Indexing & Slicing
- Copy Operations
- Control Flow
- Functions
- Modules & Packages

Remaining:

- Exception Handling
- File Handling

## Stage 2 — Object-Oriented Python

    02_oops/

Goal:

Understand Python's object model and develop strong OOP design knowledge.

Status:

    COMPLETED

## Stage 3 — Advanced Python

    03_advanced/

Goal:

Understand Python's powerful language features and execution models.

Status:

    IN PROGRESS

Completed:

- Advanced Functions

Next:

- Comprehensions

Remaining:

- Decorators
- Generators
- Iterators
- Context Managers
- Descriptors
- Metaclasses
- Concurrency
- Async Programming

## Stage 4 — Algorithms

    04_algorithms/

Goal:

Develop algorithmic thinking, data-structure knowledge, and implementation skills.

Status:

    IN PROGRESS

Completed:

- Sorting

Remaining:

- Searching
- Recursion
- Linked Lists
- Stacks & Queues
- Trees
- Graphs
- Hashing

## Stage 5 — Libraries

    05_libraries_and_modules/

Goal:

Apply Python knowledge using practical libraries and modules.

Status:

    PLANNED


# 7. Learning Order

The recommended learning order is:

    01_fundamentals
        ↓
    02_oops
        ↓
    03_advanced
        ↓
    04_algorithms
        ↓
    05_libraries_and_modules

Within each section, topics should generally be studied from top to bottom.

Individual topics may be revisited whenever deeper understanding is required.


# 8. Implementation Philosophy

Each concept should be implemented rather than merely documented.

The preferred workflow is:

    Understand the concept
            ↓
    Define the scope
            ↓
    Create focused files
            ↓
    Implement examples
            ↓
    Test execution
            ↓
    Review typing and correctness
            ↓
    Document the concept
            ↓
    Mark progress
            ↓
    Commit changes

This keeps the repository both educational and technically reliable.


# 9. Definition of Completion

A topic should generally be considered complete when:

- The concept has been clearly defined
- Important variations have been covered
- Examples are implemented
- Examples execute correctly
- Edge cases are considered where relevant
- Type annotations are appropriate
- The folder README is complete
- The code follows the repository style guide
- The topic is reflected in the roadmap

Completion does not mean the concept can never be revisited.

The repository is intended to evolve as understanding improves.


# 10. Long-Term Direction

After the major learning tracks are completed, the repository can serve as the foundation for practical Python projects.

The intended progression is:

    Learn
      ↓
    Implement
      ↓
    Revise
      ↓
    Apply
      ↓
    Build Projects
      ↓
    Document Projects
      ↓
    Use Projects as Portfolio Material

The repository therefore acts as the Python knowledge foundation for future practical work.


# 11. Current Priority

The immediate development priority is:

    03_advanced/
        └── 02_comprehensions/

The Advanced Functions section has already been completed.

The next implementation phase is Comprehensions, followed by:

    03_decorators/
        ↓
    04_generators/
        ↓
    05_iterators/
        ↓
    06_context_managers/
        ↓
    07_descriptors/
        ↓
    08_metaclasses/
        ↓
    09_concurrency/
        ↓
    10_async_programming/


# 12. Roadmap Principle

The roadmap is a guide, not a rigid restriction.

Topics may be:

- Expanded
- Reordered
- Split into additional files
- Combined when appropriate
- Reclassified if their conceptual level changes

Any structural change should improve clarity rather than simply increase repository size.

The ultimate goal is:

    A structured
    scalable
    technically accurate
    easy-to-navigate
    practical
    long-term Python knowledge repository.

