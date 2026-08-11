# Python Data Types

## Overview

This module introduces Python's built-in data types and the fundamental properties that distinguish them.

The goal is not only to learn the names of Python data types, but also to understand:

* What each type represents
* How values of each type are created
* What operations are applicable
* What built-in functions and methods are available
* How different types behave
* How Python represents and works with different kinds of data

The module is organized by the conceptual role of each type rather than simply listing Python's built-in classes.

---

## Module Structure

```text
02_data_types/
│
├── README.md
│
├── single_valued/
│   ├── 01_integer_type.py
│   ├── 02_float_type.py
│   └── 03_complex_type.py
│
├── multi_valued/
│   ├── 01_string_type.py
│   ├── 02_list_type.py
│   ├── 03_tuple_type.py
│   ├── 04_set_type.py
│   ├── 05_frozenset_type.py
│   ├── 06_dictionary_type.py
│   ├── 07_bytes_type.py
│   ├── 08_bytearray_type.py
│   └── 09_memoryview_type.py
│
├── special_dtype/
│   ├── 01_none_type.py
│   └── 02_boolean_type.py
│
├── type_checking/
│   ├── 01_type_basics.py
│   └── 02_type_function.py
│
└── type_behaviour/
    ├── 01_mutability.py
    ├── 02_hashability.py
    ├── 03_equality_vs_identity.py
    └── 04_type_conversion.py
```

> The exact numbering and directory structure should remain consistent with the current repository architecture.

---

# 1. Single-Valued Data Types

Single-valued data types represent individual scalar values.

```text
single_valued
│
├── integer
├── float
└── complex
```

### Integer

Python's `int` type represents whole numbers.

Examples:

```python
0
10
-25
```

Topics include:

* Integer literals
* Positive, negative, and zero values
* Arithmetic operations
* Division and floor division
* Modulo
* Exponentiation
* Bitwise operations
* Numeric bases
* Integer-specific methods

---

### Float

Python's `float` type represents floating-point numbers.

Examples:

```python
0.0
3.14
-12.5
```

Topics include:

* Floating-point literals
* Decimal representation
* Arithmetic
* Precision considerations
* Special floating-point values
* Useful built-in functions and methods

---

### Complex

Python's `complex` type represents complex numbers.

Examples:

```python
3 + 4j
-2j
```

Topics include:

* Real and imaginary components
* Complex literals
* Arithmetic
* `real`
* `imag`
* `conjugate()`

---

# 2. Multi-Valued Data Types

Multi-valued data types can represent collections or sequences of multiple values.

```text
multi_valued
│
├── string
├── list
├── tuple
├── set
├── frozenset
├── dictionary
├── bytes
├── bytearray
└── memoryview
```

Each type has different characteristics regarding:

* Ordering
* Mutability
* Indexing
* Slicing
* Duplicates
* Hashability
* Key/value relationships
* Element access
* Available operations

These differences are studied individually rather than treating all collections as interchangeable.

---

## String

```python
text: str = "Python"
```

Strings represent text.

Topics include:

* String creation
* Character representation
* String methods
* Searching
* Replacement
* Formatting
* Splitting and joining
* Relevant operations

Indexing and slicing are covered separately in:

```text
03_indexing_and_slicing/
```

---

## List

```python
numbers: list[int] = [10, 20, 30]
```

Lists are ordered, mutable collections.

Topics include:

* Creating lists
* Adding and removing elements
* Searching
* Sorting
* Reversing
* List methods
* Nested lists
* Applicable built-in functions

Copy operations are covered separately where appropriate.

---

## Tuple

```python
coordinates: tuple[int, int] = (10, 20)
```

Tuples are ordered, immutable collections.

Topics include:

* Tuple creation
* Element access
* Tuple methods
* Packing
* Unpacking
* Nested tuples
* Tuple-specific behavior

---

## Set

```python
unique_numbers: set[int] = {1, 2, 3}
```

Sets represent unordered collections of unique elements.

Topics include:

* Creating sets
* Adding and removing elements
* Membership
* Set operations
* Union
* Intersection
* Difference
* Symmetric difference
* Applicable methods

---

## Frozenset

```python
fixed_numbers: frozenset[int] = frozenset({1, 2, 3})
```

`frozenset` represents an immutable set.

It shares many set operations with `set`, but its immutability makes it usable in situations where a normal set cannot be used.

Important properties include:

* Unordered
* Unique elements
* Immutable
* Hashable

---

## Dictionary

```python
student: dict[str, int] = {
    "age": 25,
}
```

Dictionaries store key-value relationships.

Topics include:

* Dictionary creation
* Keys and values
* Adding and updating entries
* Removing entries
* Membership
* Dictionary methods
* Nested dictionaries
* Key/value access
* Dictionary-specific behavior

Specialized dictionary objects such as `defaultdict` are covered later under Python Objects.

---

## Bytes

```python
data: bytes = b"Python"
```

`bytes` represents immutable sequences of bytes.

Topics include:

* Bytes literals
* Byte values
* Encoding-related concepts
* Byte operations
* Bytes methods
* Interaction with binary data

---

## Bytearray

```python
data: bytearray = bytearray(b"Python")
```

`bytearray` represents mutable sequences of bytes.

The module compares its behavior with immutable `bytes`.

---

## Memoryview

```python
data: memoryview = memoryview(b"Python")
```

`memoryview` provides a view of an existing bytes-like object's memory without requiring a new copy of the underlying data.

This becomes particularly relevant when discussing:

* Binary data
* Memory efficiency
* Buffer-oriented operations

---

# 3. Special Data Types

Some Python types have special semantic roles.

```text
special_dtype
│
├── None
└── bool
```

---

## None

`None` represents the absence of a meaningful value.

```python
result = None
```

Common uses include:

* Representing missing results
* Indicating absence
* Default function return behavior
* Optional values

---

## Boolean

`bool` represents logical truth values:

```python
True
False
```

Boolean behavior also has an important relationship with integers, which is explored carefully in the Boolean module.

---

# 4. Type Checking

Understanding what type an object has is fundamental to Python programming.

```text
type_checking
│
├── type basics
└── type()
```

Topics include:

* Objects and their types
* `type()`
* `isinstance()`
* Type relationships
* Basic runtime type inspection

The goal is to understand the difference between asking:

> "What is this object's type?"

and:

> "Is this object an instance of this type?"

---

# 5. Type Behaviour

Individual data types are not enough to understand Python.

Different types behave differently with respect to:

```text
type_behaviour
│
├── mutability
├── hashability
├── equality vs identity
└── type conversion
```

---

## Mutability

Explores whether an object's contents can be changed after creation.

Examples include:

```text
Mutable:
    list
    set
    dict
    bytearray

Immutable:
    int
    float
    complex
    str
    tuple
    frozenset
    bytes
```

The goal is to understand **object behavior**, not merely memorize a classification.

---

## Hashability

Explores which objects can participate in hash-based structures such as dictionary keys and set elements.

This connects directly to:

* `dict`
* `set`
* `frozenset`
* Immutable objects

---

## Equality vs Identity

Two different concepts:

```python
first == second
```

checks value equality.

Whereas:

```python
first is second
```

checks object identity.

The distinction is fundamental to understanding Python's object model.

---

## Type Conversion

Explores converting values between compatible types.

Examples include:

```python
int()
float()
str()
bool()
list()
tuple()
set()
```

The goal is to understand both successful conversions and cases where conversion is invalid.

---

# Default and Non-Default Values

Each applicable data type module includes a dedicated section covering its commonly used **default-like value** and non-default values.

For example:

```python
integer_value: int = 0
```

However, an important distinction is maintained throughout the module:

> Python does not automatically initialize a variable merely because a type annotation is provided.

For example:

```python
number: int
```

does not automatically assign:

```python
number = 0
```

Therefore, the modules distinguish between:

* A commonly used default-like value
* Explicit initialization
* Python's actual runtime behavior

This distinction is particularly important when comparing different data types.

---

# Relationship With Other Modules

This module intentionally does not attempt to teach every Python concept associated with these types.

### Indexing and Slicing

Covered separately in:

```text
03_indexing_and_slicing/
```

This includes:

* Positive indexing
* Negative indexing
* Start/stop slicing
* Positive steps
* Negative steps
* Slice objects
* Slice behavior across applicable types

### Copy Operations

Copying behavior is covered separately where appropriate.

Examples include:

```text
assignment
shallow copy
deep copy
```

### Python Objects

Specialized objects and object categories that are not part of the core data-type curriculum are covered under:

```text
04_python_objects/
```

Examples include:

* `range`
* Iterators
* Generators
* Dictionary view objects
* `defaultdict`
* `Counter`
* `deque`
* File objects
* Function objects
* Context manager objects
* Class and instance objects
* Coroutine objects

---

# Learning Approach

Each data type follows a consistent structure.

Where applicable, a type module covers:

```text
1. Definition
        ↓
2. Default / non-default values
        ↓
3. Creating values
        ↓
4. Type identification
        ↓
5. Core properties
        ↓
6. Applicable operations
        ↓
7. Applicable built-in functions
        ↓
8. Type-specific methods
        ↓
9. Practical examples
        ↓
10. Key takeaways
```

The modules are intentionally designed as **standalone reference files** so that each file can be studied independently without requiring unrelated concepts from later modules.

---

# Standards Used in This Module

All examples follow the repository's coding and teaching standards:

* Use complete, copy-paste-ready files.
* Use precise type annotations where applicable.
* Avoid unnecessary type casts.
* Do not silence type-checker warnings merely to make an example pass.
* Use unique variable names within each file.
* Avoid redefining variables unnecessarily.
* Keep examples conceptually isolated.
* Explain important behavior through comments.
* Show object identity with `id()` or `is` when identity is relevant.
* Use `!r` when displaying representations of objects such as `bytes`.
* Introduce advanced concepts only after their prerequisites have been established.
* Avoid duplicating concepts already properly covered in another module.
* Keep each file focused on its declared type or behavior.
* Include default-like and non-default value examples where applicable.
* Distinguish conventional defaults from Python's actual automatic initialization behavior.
* Keep examples compatible with static type checking wherever practical.

---

# Learning Goal

After completing this module, you should be able to:

1. Identify Python's major built-in data types.
2. Explain the purpose of each type.
3. Create values of each type correctly.
4. Understand the major properties of each type.
5. Select an appropriate data type for a given problem.
6. Use relevant operations and methods.
7. Understand mutability and hashability.
8. Distinguish equality from object identity.
9. Perform appropriate type conversions.
10. Understand how Python's different data types behave as objects.

The objective is not to memorize a list of types.

The objective is to understand **why each type exists, what it represents, how it behaves, and when it should be used.**
