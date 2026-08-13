
# Architecture

This document explains the architecture, organization, and learning progression of the Python Concepts repository.

The repository is intentionally structured as a progressive learning system rather than as a collection of unrelated Python examples.

---

## 1. Architectural Philosophy

The repository follows a **concept-first, progression-based architecture**.

Each major Python area is separated into its own learning track, and each track is further divided into focused topics.

The overall progression is:

    Fundamentals
        ↓
    Object-Oriented Programming
        ↓
    Advanced Python
        ↓
    Algorithms & Data Structures
        ↓
    Libraries & Modules

The purpose of this progression is to build concepts in layers instead of learning advanced features without understanding the underlying Python model.

---

## 2. Top-Level Architecture

The repository is divided into five major tracks:

    python-concepts/
    │
    ├── 01_fundamentals/
    ├── 02_oops/
    ├── 03_advanced/
    ├── 04_algorithms/
    └── 05_libraries_and_modules/

Each track has a different purpose.

---

## 3. Fundamentals

Path:

    01_fundamentals/

The Fundamentals track establishes the core Python language.

It covers:

- Basic Python syntax
- Variables
- Type annotations
- Data types
- Operators
- Indexing and slicing
- Copy operations
- Control flow
- Functions
- Modules
- Packages
- Exception handling
- File handling

The goal of this section is to establish a strong understanding of how Python code behaves before moving into object-oriented and advanced features.

### Internal Structure

    01_fundamentals/
    │
    ├── 01_basics/
    ├── 02_data_types_and_operators/
    ├── 03_indexing_and_slicing/
    ├── 04_copy_operations/
    ├── 05_control_flow/
    ├── 06_functions/
    ├── 07_modules_and_packages/
    ├── 08_exception_handling/
    └── 09_file_handling/

---

## 4. Functions

Path:

    01_fundamentals/06_functions/

Functions remain part of Fundamentals because they are a core Python programming construct.

This section covers:

- Function definition
- Parameters
- Arguments
- Positional arguments
- Keyword arguments
- Default arguments
- `*args`
- `**kwargs`
- Return values
- Scope
- `global`
- `nonlocal`
- Nested functions
- Function annotations
- Docstrings
- Built-in functions

More advanced function concepts such as lambda functions, first-class functions, higher-order functions, and callable objects are separated into the Advanced section.

This distinction keeps the fundamentals focused while allowing advanced function behaviour to be studied separately.

---

## 5. Modules & Packages

Path:

    01_fundamentals/07_modules_and_packages/

This section explains how Python code is organized across files and packages.

It covers:

- Modules
- Imports
- Module namespaces
- Module search paths
- Packages
- Subpackages
- Import patterns
- Special module attributes

The section is intentionally kept under Fundamentals because understanding modules and packages is essential before working with larger Python applications.

---

## 6. Object-Oriented Programming

Path:

    02_oops/

The OOP track introduces Python's object model and object-oriented design.

The section progresses from basic classes and objects toward more advanced object-oriented design concepts.

### Internal Structure

    02_oops/
    │
    ├── 01_object_model/
    ├── 02_classes/
    ├── 03_constructors_and_initialization/
    ├── 04_inheritance/
    ├── 05_polymorphism/
    ├── 06_encapsulation/
    ├── 07_abstraction/
    ├── 08_properties/
    ├── 09_dunder_methods/
    ├── 10_operator_overloading/
    ├── 11_composition/
    ├── 12_class_design/
    └── 13_dataclasses/

The ordering is intentional.

The learner first understands objects and classes, then inheritance and polymorphism, followed by encapsulation, abstraction, special methods, and class design.

---

## 7. Advanced Python

Path:

    03_advanced/

The Advanced section contains concepts that build on the fundamentals and OOP knowledge.

### Internal Structure

    03_advanced/
    │
    ├── 01_advanced_functions/
    ├── 02_comprehensions/
    ├── 03_decorators/
    ├── 04_generators/
    ├── 05_iterators/
    ├── 06_context_managers/
    ├── 07_descriptors/
    ├── 08_metaclasses/
    ├── 09_concurrency/
    └── 10_async_programming/

### Why Comprehensions Are Here

Comprehensions are intentionally placed under Advanced rather than Fundamentals.

Basic loops are fundamental Python syntax, while comprehensions provide a more compact and expressive way of constructing collections.

Keeping them in Advanced creates a clear distinction between:

    Basic iteration
        ↓
    Comprehension-based transformation

The Comprehensions section covers:

- List comprehensions
- Conditional comprehensions
- Nested comprehensions
- Set comprehensions
- Dictionary comprehensions
- Comprehensions vs loops
- Comprehension best practices

---

## 8. Advanced Functions

Path:

    03_advanced/01_advanced_functions/

This section extends the function concepts introduced under Fundamentals.

It covers:

- Lambda functions
- First-class functions
- Higher-order functions
- Recursive functions
- Callable objects

The separation prevents the Fundamentals section from becoming overloaded with advanced function behaviour.

---

## 9. Algorithms

Path:

    04_algorithms/

The Algorithms section focuses on algorithmic thinking and data structures.

### Internal Structure

    04_algorithms/
    │
    ├── 01_sorting/
    ├── 02_searching/
    ├── 03_recursion/
    ├── 04_linked_lists/
    ├── 05_stacks_and_queues/
    ├── 06_trees/
    ├── 07_graphs/
    └── 08_hashing/

Algorithms are kept separate from the language-learning tracks because their primary purpose is problem solving rather than learning Python syntax itself.

Python is used as the implementation language.

---

## 10. Libraries & Modules

Path:

    05_libraries_and_modules/

This section focuses on practical Python libraries and modules used in real-world development.

### Internal Structure

    05_libraries_and_modules/
    │
    ├── 01_standard_library/
    ├── 02_numpy/
    ├── 03_pandas/
    ├── 04_matplotlib/
    ├── 05_requests/
    ├── 06_sqlalchemy/
    └── 07_pytest/

The Standard Library section includes:

- `os`
- `sys`
- `pathlib`
- `datetime`
- `json`
- `csv`
- `re`

This section is intentionally placed after the language concepts so that libraries are learned on top of an already-established Python foundation.

---

## 11. File-Level Architecture

Each topic is broken into focused Python files.

Example:

    02_oops/05_polymorphism/
    │
    ├── 01_method_overriding.py
    ├── 02_duck_typing.py
    ├── 03_polymorphic_functions.py
    ├── 04_polymorphism_with_inheritance.py
    └── README.md

Each Python file should primarily teach one concept.

This provides:

- Focused learning
- Easier revision
- Easier debugging
- Easier experimentation
- Easier navigation
- Better reference value

---

## 12. README Architecture

Each major topic folder contains a `README.md`.

The README explains the conceptual structure of that topic and acts as the entry point for studying the examples.

The general pattern is:

    Topic Folder
        │
        ├── README.md
        │
        ├── Concept 01
        ├── Concept 02
        ├── Concept 03
        └── ...

The Python files contain the implementations, while the README provides the conceptual map.

---

## 13. Single-Concept File Principle

A Python example should normally focus on one primary concept.

For example:

    03_positional_arguments.py

should primarily teach positional arguments rather than mixing positional arguments, keyword arguments, default arguments, and `*args` into one unrelated example.

Related concepts may appear when necessary to demonstrate the target concept, but the file should have a clear teaching objective.

---

## 14. Example Design Philosophy

Examples should be:

- Copy-paste ready
- Non-interactive by default
- Easy to execute
- Deterministic
- Conceptually accurate
- Properly typed where appropriate
- Easy to read
- Focused on the concept being demonstrated

`input()` should generally be avoided unless interactive input itself is the concept being demonstrated.

---

## 15. Static Type Checking

Where type annotations are used, examples should remain compatible with common static type checkers such as:

- Pyright
- Pylance
- Mypy

Avoid unnecessary type-checker warnings.

When Python's runtime behaviour is correct but a static checker cannot infer the intended type, an explicit and beginner-friendly approach may be used rather than changing the conceptual example unnecessarily.

---

## 16. Documentation Architecture

The repository contains several project-level documentation files.

### README.md

Provides the overall introduction, repository purpose, structure, and learning progress.

### ARCHITECTURE.md

Explains how the repository is organized and why the different learning tracks exist.

### ROADMAP.md

Tracks the planned learning progression and future development.

### STYLE_GUIDE.md

Defines coding and documentation conventions used throughout the repository.

### folder_tree.txt

Provides a quick reference of the repository's directory structure.

---

## 17. Learning Dependency Model

The repository follows a dependency-based learning model.

The general relationship is:

    Python Syntax
          ↓
    Data & Control Flow
          ↓
    Functions
          ↓
    Modules & Packages
          ↓
    Object-Oriented Programming
          ↓
    Advanced Python
          ↓
    Algorithms
          ↓
    Libraries
          ↓
    Practical Projects

Not every concept strictly depends on the previous section, but the ordering provides a recommended learning path.

---

## 18. Separation of Concepts

The repository intentionally avoids mixing fundamentally different learning objectives.

For example:

    Fundamentals
        = How Python works at the language level

    OOP
        = How Python models objects and designs classes

    Advanced
        = Powerful language features and advanced execution models

    Algorithms
        = Problem solving and data structures

    Libraries
        = Applying Python through external and standard-library tools

This separation keeps the repository understandable as it grows.

---

## 19. Growth Strategy

The repository is designed to grow incrementally.

New concepts should be added to the appropriate existing category rather than creating unnecessary new top-level categories.

A new section should only be introduced when:

- The concept represents a meaningful learning area
- Existing categories cannot represent it cleanly
- The separation improves navigation
- The new section has enough related material to justify its existence

---

## 20. Long-Term Structure

The intended long-term structure is:

    01_fundamentals
            │
            ├── Language Fundamentals
            ├── Data & Operators
            ├── Control Flow
            ├── Functions
            ├── Modules & Packages
            ├── Exceptions
            └── File Handling
                    │
                    ↓
    02_oops
            │
            ├── Object Model
            ├── Classes
            ├── Inheritance
            ├── Polymorphism
            ├── Encapsulation
            ├── Abstraction
            └── Class Design
                    │
                    ↓
    03_advanced
            │
            ├── Advanced Functions
            ├── Comprehensions
            ├── Decorators
            ├── Generators
            ├── Iterators
            ├── Context Managers
            ├── Descriptors
            ├── Metaclasses
            ├── Concurrency
            └── Async Programming
                    │
                    ↓
    04_algorithms
            │
            ├── Sorting
            ├── Searching
            ├── Recursion
            ├── Linked Lists
            ├── Stacks & Queues
            ├── Trees
            ├── Graphs
            └── Hashing
                    │
                    ↓
    05_libraries_and_modules
            │
            ├── Standard Library
            ├── NumPy
            ├── Pandas
            ├── Matplotlib
            ├── Requests
            ├── SQLAlchemy
            └── Pytest

---

## 21. Core Principle

The repository is not intended to be a random collection of Python snippets.

It is designed as a structured Python knowledge base where:

    Concepts
        ↓
    Examples
        ↓
    Practice
        ↓
    Revision
        ↓
    Deeper Understanding
        ↓
    Practical Application

Each addition should strengthen this overall structure rather than simply increase the number of files.

---

## 22. Final Architectural Rule

When adding a new concept, ask:

1. What concept does this teach?
2. Which learning track does it belong to?
3. Does an existing folder already represent it?
4. Should it be a separate file or part of an existing concept?
5. Does it depend on another concept?
6. Can the example remain focused and copy-paste ready?
7. Does adding it make the repository easier or harder to navigate?

The goal is not maximum number of files.

The goal is a **clear, scalable, logically organized Python learning system**.
```
